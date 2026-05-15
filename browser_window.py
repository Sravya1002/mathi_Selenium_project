import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/browserTabs.html')
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()

# getting id of parent window and storing inside parent_window variable
parent_window = driver.current_window_handle

# getting id of all opened window handles and storing inside tabs variable
tabs = driver.window_handles
print(len(tabs))
print(tabs)
for each_tab in tabs:
    driver.switch_to.window(each_tab)
    time.sleep(2)
    print(driver.title)
    print(driver.current_url)

driver.switch_to.window(parent_window)


