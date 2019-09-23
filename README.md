# unnamed-slack-nlp-bot
A bot that reads articles posted to Slack and performs simple nlp classification then replies with the results.

Set the contents of environment_variables.sh then run before starting the app.


#### Technical Requirements

This project uses [Python](https://www.python.org/downloads/), specifically version 3.3+ so you'll need to make sure you are using the correct version of Python. We'll also use a number of python packages you can install through [pip.](https://pip.pypa.io/en/stable/installing/)

###### Here's a list of what we'll need:

- **[Python](https://www.python.org/downloads/)**, the programming language.
- **[Pip](https://pip.pypa.io/en/stable/installing/)**, the Python package manager.
- **[Conda](https://anaconda.org/anaconda/conda)**, the virtual environment manager.


Once you've installed Python, pip, you can install all additional
dependent libraries using pip and the `requirements.txt` file included in this
project, including [Flask](http://flask.pocoo.org/), a web development micro
framework for Python and [python-slackclient](http://python-slackclient.readthedocs.io/en/latest/), a
Slack client for Python. :snake:

If you're using `conda` run the following commands from the root of your
project directory:

```bash
conda create -n unnamed-slack-nlp-bot python=3.7
```

If prompted, enter y to accept the new packages being installed.

Then activate your new virtual environment:

```bash
source activate unnamed-slack-nlp-bot
```

After that, you can install all the Python packages this project will need with
this command:

```bash
pip install -r requirements.txt
```

###### Server Requirements

Slack will be delivering events to your app's server so your server needs to be able to receive incoming HTTPS traffic from Slack.

If you are running this project locally, you'll need to set up tunnels for Slack to connect to your endpoints. [Ngrok](https://ngrok.com/) is an easy to use tunneling tool that supports HTTPS, which is required by Slack.


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