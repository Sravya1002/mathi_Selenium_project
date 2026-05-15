# Login_page.py - Validating the user_name and password

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Browser:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def launch_application(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            return True
        except Exception as e:
            print(f"Error in launching website!!, {e}")
            return False

    def get_title(self):
        if self.launch_application():
            return self.driver.title
        else:
            raise Exception("Error!! page title cannot be found due to browser issue")

    def login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(10)
        self.driver.save_screenshot('Login_page.png')

    def close_browser(self):
        self.driver.quit()