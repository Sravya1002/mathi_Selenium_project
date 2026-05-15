# iframes are windows inside a window. These are tags used for creating a small window within page.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/iframes.html')
driver.maximize_window()

# locate and print content of Iframe header paragraph
print(driver.find_element(By.XPATH,'//div[@id="main"]/div/p').text)

# locate and print header Testing Arena and its context located within second window
iframe_loc = driver.find_element(By.XPATH,"//iframe[@src='index.html']")
driver.switch_to.frame(iframe_loc)
print(driver.find_element(By.XPATH,'//section[@id="banner"]/div/header/h1').text)
print(driver.find_element(By.XPATH,"(//p[@style='text-transform: none;'])[1]").text)

# locate and print automation testing text written at the top of the page
driver.switch_to.default_content()
print(driver.find_element(By.XPATH,'//div[@id="main"]/div/p').text)
header_elements = driver.find_elements(By.XPATH,"//header[@id='header']/a/strong")
for each_header in header_elements:
    print(each_header.text)
    break
driver.quit()



