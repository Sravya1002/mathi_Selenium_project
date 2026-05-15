# Homepage.py - Validating the Title and URL

"""
Homepage - Python selenium codes for performing automation
"""
# Import all the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create classes and methods
class GuviHome:
    def __init__(self, url):
        self.url = url  # binding the url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # creating a driver object

    def start_automation(self):
        try:
            self.driver.get(self.url)  # launches the page with url
            self.driver.maximize_window()  # maximizes window
            return True
        except:
            print("Error: Unable to start the automation")
            return False

    def shutdown(self):
        self.driver.quit()  # closes all browser instances

    def fetch_title(self):
        if self.start_automation():
            return self.driver.title
        else:
            print("Error: Unable to fetch the title!")
            return False

    def fetch_url(self):
        if self.start_automation():
            return self.driver.current_url
        else:
            print("Error: Unable to fetch the url!")
            return False
