from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from sumy.utils import get_stop_words

import requests
import six
import json

LANGUAGE = "english"
SENTENCES_COUNT = 5
POST_COUNT = 30


def get_summarized_article(url):
    """
    From a url, get a summarization of the page/article
    Parameters
        ----------
        url : str
            the address of the article/text to summarize

    Returns
        ----------
        summarized_text : str
            the summarized text of the article at the supplied url
    """
    summarized_text = ""
    try:
        if domain_in_blacklist(url) == False:
            parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
            # or for plain text files
            # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = LsaSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)

            text = ""

            for sentence in summarizer(parser.document, SENTENCES_COUNT):
                text = text + " " + str(sentence)
            summarized_text = text
        else:
            summarized_text = None
    except Exception as ke:
        print("**********")
        print("Exception in Categorizer!")
        print("**********")
        print("")
        print(ke)
        summarized_text = None
    return summarized_text


def get_category(text):
    """
    From a block of text, get the categorization of that text
    Parameters
        ----------
        text : str
            the article/text to categorize

    Returns
        ----------
        category : str
            the category of the text contents
    """
    if text:
        client = language.LanguageServiceClient()

        if isinstance(text, six.binary_type):
            text = text.decode("utf-8")

        document = types.Document(
            content=text.encode("utf-8"), type=enums.Document.Type.PLAIN_TEXT
        )

        categories = client.classify_text(document).categories

        if categories:
            return categories[0].name
    return None


def domain_in_blacklist(url):
    """
    determines if the provided url is in a blacklist
    Parameters
        ----------
        url : str
            the url to check for blacklisting
    """
    blacklist = [
        "youtube.com",
        "bloomberg.com",
        "sec.gov",
        "dannymoerkerke.com",
        "localizingjapan.com",
        "ianix.com",
    ]
    for domain in blacklist:
        if domain in url:
            return True
    return False