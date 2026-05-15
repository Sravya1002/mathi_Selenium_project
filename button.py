import time
from selenium  import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.devtools.v145.dom import move_to
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/buttons.html')

action =ActionChains(driver)
move_to_bttn = driver.find_element(By.ID,"btn_three")
action.move_to_element(move_to_bttn).click().perform()
time.sleep(2)
driver.switch_to.alert.accept()
print(driver.find_element(By.ID,"btn_four").is_enabled())
time.sleep(2)