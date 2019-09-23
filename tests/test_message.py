import pytest
import src.message as message

class TestMessage:
    def test_create_message(self):
        message_obj = message.Message()
        assert message_obj.channel == ""
        assert message_obj.text == ("Category\n"
                     ">%s\n"
                     "Summarized article sent to Google NLP\n"
                     ">>>%s")

    def test_update_message(self):
        message_obj = message.Message()
        message_obj.update_text_categorized("test/category", "Test Original Text")
        assert message_obj.text == ("Category\n"
                     ">test/category\n"
                     "Summarized article sent to Google NLP\n"
                     ">>>Test Original Text")