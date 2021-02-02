from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#import os

username = "admin"
password = "password"

driverLocation = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\lib\\chromedriver.exe"
#os.environ["webdriver.chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation)
driver.get("https://automationintesting.online/#/admin")
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("doLogin").click()

element = driver.find_element_by_id("createRoom")
print(element.is_enabled())