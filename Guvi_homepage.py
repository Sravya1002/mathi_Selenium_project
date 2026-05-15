from unittest import expectedFailure
from homepage import GuviHome

# Test data
url = "https://www.guvi.in/"
myGuviAutomation = GuviHome(url)

class TestGuviAutomation:
    def test_positive_url(self):
        expected_url = "https://www.guvi.in/"
        actual_url = myGuviAutomation.fetch_url()
        assert expected_url == actual_url
        print("SUCCESS: Test Positive URL Passed")

    def test_negative_url(self):
        expected_url = "https://www.mentor.in/"
        actual_url = myGuviAutomation.fetch_url()
        assert expected_url != actual_url
        print("SUCCESS: Test Negative URL Passed")

    def test_positive_title(self):
        expected_title = "GUVI | Learn to code in your native language"
        actual_title = myGuviAutomation.fetch_title()
        assert expected_title == actual_title
        print("SUCCESS: Test Positive Title Passed")

    def test_negative_title(self):
        expected_title = "My GUVI"
        actual_title = myGuviAutomation.fetch_title()
        assert expected_title != actual_title
        print("SUCCESS: Test Negative Title Passed")
