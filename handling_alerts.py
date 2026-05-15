import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/popups.html')
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[onclick='alertTrigger()']").click()
driver.switch_to.alert.accept()