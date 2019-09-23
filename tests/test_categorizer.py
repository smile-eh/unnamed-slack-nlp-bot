import pytest
from src.categorizer import get_summarized_article, get_category, domain_in_blacklist

class TestCategorizer:
    def test_summary(self):
        # TODO Update mocking for sumy response
        assert 1==1

    def test_category(self):
        # TODO Update mocking for google response
        assert 1==1

    def test_domain_in_blacklist(self):
        assert domain_in_blacklist("youtube.com") == True
        assert domain_in_blacklist("bloomberg.com") == True
        assert domain_in_blacklist("sec.gov") == True
        assert domain_in_blacklist("dannymoerkerke.com") == True
        assert domain_in_blacklist("localizingjapan.com") == True
        assert domain_in_blacklist("ianix.com") == True
        assert domain_in_blacklist("cnn.com") == False
        assert domain_in_blacklist("medium.com") == False

        