# -*- coding: utf-8 -*-
"""
Python Slack Bot class for use with the pythOnBoarding app
"""
import os
import src.message as message

from slackclient import SlackClient

# To remember which teams have authorized your app and what tokens are
# associated with each team, we can store this information in memory on
# as a global object. When your bot is out of development, it's best to
# save this in a more persistent memory store.
authed_teams = {}

# Development Slack API keys
# DO NOT COMMIT TO GIT!
SLACK_CLIENT_ID = ""
SLACK_CLIENT_SECRET = ""
SLACK_VERIFICATION_TOKEN = ""
SLACK_BOT_OAUTH = ""


class Bot(object):
    """ Instantiates a Bot object to handle Slack onboarding interactions."""
    def __init__(self, is_dev = False):
        super(Bot, self).__init__()
        self.name = "unnamed-slack-nlp-bot"
        self.emoji = ":robot_face:"
        # When we instantiate a new bot object, we can access the app
        # credentials we set earlier in our local development environment.
        if is_dev:
            self.oauth = {"client_id": SLACK_CLIENT_ID,
                        "client_secret": SLACK_CLIENT_SECRET,
                        # Scopes provide and limit permissions to what our app
                        # can access. It's important to use the most restricted
                        # scope that your app will need.
                        "scope": "bot"}
            self.verification = SLACK_VERIFICATION_TOKEN
            # NOTE: Python-slack requires a client connection to generate
            # an OAuth token. We can connect to the client without authenticating
            # by passing an empty string as a token and then reinstantiating the
            # client with a valid OAuth token once we have one.
            self.client = SlackClient(SLACK_BOT_OAUTH)
        else:
            self.oauth = {"client_id": os.environ.get("SLACK_CLIENT_ID"),
                        "client_secret": os.environ.get("SLACK_CLIENT_SECRET"),
                        "scope": "bot"}
            self.verification = os.environ.get("SLACK_VERIFICATION_TOKEN")
            self.client = SlackClient(os.environ.get("SLACK_BOT_OAUTH"))

        # We'll use this dictionary to store the state of each message object.
        # In a production environment you'll likely want to store this more
        # persistently in  a database.
        self.messages = {}

    def auth(self, code):
        """
        Authenticate with OAuth and assign correct scopes.
        Save a dictionary of authed team information in memory on the bot
        object.

        Parameters
        ----------
        code : str
            temporary authorization code sent by Slack to be exchanged for an
            OAuth token

        """
        # After the user has authorized this app for use in their Slack team,
        # Slack returns a temporary authorization code that we'll exchange for
        # an OAuth token using the oauth.access endpoint
        auth_response = self.client.api_call(
                                "oauth.access",
                                client_id=self.oauth["client_id"],
                                client_secret=self.oauth["client_secret"],
                                code=code
                                )
        # To keep track of authorized teams and their associated OAuth tokens,
        # we will save the team ID and bot tokens to the global
        # authed_teams object
        team_id = auth_response["team_id"]
        authed_teams[team_id] = {"bot_token":
                                 auth_response["bot"]["bot_access_token"]}
        # Then we'll reconnect to the Slack Client with the correct team's
        # bot token
        self.client = SlackClient(authed_teams[team_id]["bot_token"])
    
    def categorized_message(self, category, thread_id, channel, summarized_text):
        """
        Respond to a message containing an article with the
        category and summarized text of that article.

        Responds in the same channel, and if possible starts a thread to reply in

        Parameters
        ----------
        category : str
            The category that the article belongs to
        thread_id : str
            The thread ID of the parent that originally sent the article
        channel : str
            The channel that the message was sent in
            This bot must have correct permissions in slack for this channel
                channels:write
                channels:read
                channels:history
                chat:write:bot 
                incoming-webhook 
                links:read 
        original_text : str
            The summarized text of the article returned from sumy
        """

        # We've imported a Message class from `message.py` that we can use
        # to create message objects for each message we send to thread. 

        # First, we'll check to see if there's already messages our bot knows
        # of for the thread.
        if self.messages.get(thread_id):
            # If we've already replied to this thread - return without re-sending a message
            return
        else:
            # If there aren't any message for that thread, we'll add a dictionary
            # of messages for that thread on our Bot's messages attribute
            self.messages[thread_id] = message.Message()
        
        # Alias for easier accessing
        message_obj = self.messages[thread_id]

        # Update the channel
        message_obj.channel = channel

        # Update the text with the category and summarized text
        message_obj.update_text_categorized(category=category, summarized_text=summarized_text)

        # Send the message with the bots new text
        post_message = self.client.api_call("chat.postMessage",
                        channel=message_obj.channel,
                        username=self.name,
                        icon_emoji=self.emoji,
                        text=message_obj.text,
                        thread_ts=thread_id
                    )