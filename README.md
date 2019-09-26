# unnamed-slack-nlp-bot
A bot that reads articles posted to Slack and performs simple nlp classification then replies with the results. The bot will use the Google NLP API to classify content from Slack.

This guide will tell you how to run a slack bot locally for development and then deploy a live testing version on Heroku. It will assume that you are starting from nothing, and only have this repo. Beginners may be able to understand the concepts, but it's mainly for intermediate level users.

# Setting up the project locally

## Prerequisites

### Accounts

 - Slack, with admin permissions for the workspace
 - Github (deployment only)
 - Heroku (deployment only)
 - Google Cloud

### Software

 - Linux or Mac suggested
 - **[Git](https://git-scm.com/)**, for code version control.
 - **[Ngrok](https://ngrok.com/)**, for tunnelling local connections to slack during development.
 - **[Python](https://www.python.org/downloads/)**, the programming language.
 - **[Pip](https://pip.pypa.io/en/stable/installing/)**, the Python package manager.
 - **[Conda](https://anaconda.org/anaconda/conda)**, the virtual environment manager.

#### Technical Information

This project uses [Python](https://www.python.org/downloads/), specifically version 3.3+ so you'll need to make sure you are using the correct version of Python. We'll also use a number of python packages you can install through [pip.](https://pip.pypa.io/en/stable/installing/)

Once you've installed Python, pip, you can install all additional dependent libraries using pip and the `requirements.txt` file included in this project, including [Flask](http://flask.pocoo.org/), a web development micro framework for Python and [python-slackclient](http://python-slackclient.readthedocs.io/en/latest/), a Slack client for Python. :snake:

## Run Locally

### Git

Download the code and move into the folder

```sh
# Get the code
git clone https://github.com/smile-eh/unnamed-slack-nlp-bot.git

# Move into the code
cd unnamed-slack-nlp-bot
```

### Anaconda

Using `conda`, run the following commands from the root of your project directory:

```sh
# Make conda environment
conda create -n unnamed-slack-nlp-bot python=3.7
```

If prompted, enter `Y` to accept the new packages being installed.

Activate your new virtual environment, then install all the Python packages this project will need:

```sh
# Start the new environment
source activate unnamed-slack-nlp-bot

# Install the packages
python -m pip install -r requirements.txt
```

### Sumy

One of the packages that we just installed using `pip` is used for summarizing content when given a URL, such as an article. We have to download some language information before we can use it:

```sh
python -m nltk.downloader 'punkt'
```

### Keys

### Set up Slack App

Create a [new Slack workspace](https://slack.com/create) for testing. Make sure to create a channel called `unnamed-bot`.

Once logged in to your new workspace as an admin, create a [Slack App](https://api.slack.com/apps?new_app=1). Enter an App Name, and select the Slack workspace you just created.

#### Webhooks

From the main page, under Add features and functionality, click on `Incoming Webhooks`.

Turn webhooks on, then scroll down and click on `Add New Webhook to Workspace`.

When on the identity confirmation page, where you can select a channel to post to, select `unnamed-bot` then click allow. If you do not see it, make sure to return to Slack and create a channel with that name.



Slack Apps are how access to the Slack developer API is controlled. This access is controlled through API keys.



Make Google App
-Explain Google NLPs role and key system

Run key script

### Start server

### Ngrok

Slack will be delivering events to your app's server so your server needs to be able to receive incoming HTTPS traffic from Slack.

If you are running this project locally, you'll need to set up tunnels for Slack to connect to your endpoints. [Ngrok](https://ngrok.com/) is an easy to use tunneling tool that supports HTTPS, which is required by Slack.

In another terminal window enter this command to start the tunneling:

```sh
ngrok http 5000
```

## Deploy to Heroku

Google Cloud buildpack

Slack Keys

Python buildpack

Procfile

## Further Reading and Getting Help

### Documentation

##### Slack Documentation
* [Getting started with Slack apps](https://api.slack.com/slack-apps)
* [Slack Events API documentation](https://api.slack.com/events)
* [Slack Web API documentation](https://api.slack.com/web)

##### Documentation for Tools
* [Conda](https://conda.io/projects/conda/en/latest/)
* [flask](http://flask.pocoo.org/)
* [python-slackclient](http://python-slackclient.readthedocs.io/en/latest/)
* [ngrok](https://ngrok.com/docs)

### Feedback
I'd love to improve this project, if you have any suggestions or fixes please file an issue, or submit a PR!