# -*- coding: utf-8 -*-
"""
Python Slack Message class for use with the pythOnBoarding bot
"""
# TODO: Fix hack with yaml library for handling unicode encoding issues
import yaml


class Message(object):
    """
    Instantiates a Message object to create and manage
    Slack onboarding messages.
    """
    def __init__(self):
        super(Message, self).__init__()
        self.channel = ""
        self.text = ("Category\n"
                     ">%s\n"
                     "Summarized article sent to Google NLP\n"
                     ">>>%s")

    def update_text_categorized(self, category, summarized_text):
        """
        Update the original text from instantiation with the
        category from google, and the summarized text from sumy

        Parameters
        **********
        category : str
            The category, response from Google's NLP API
        summarized_text : str
            The summarized text from sumy that corresponds to the
            category parameter
        
        """
        self.text = self.text % (category, summarized_text)