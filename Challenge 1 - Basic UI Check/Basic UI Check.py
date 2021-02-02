# importing webdriver
from selenium import webdriver

# credentials
username = "admin"
password = "password"

# chromedriver path and variable declaration
driverLocation = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\lib\\chromedriver.exe"
driver = webdriver.Chrome(driverLocation)

# get to required place
driver.get("https://automationintesting.online/#/admin")

# logging in after inputting username and password
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("doLogin").click()

# setting a delay for page to load properly
driver.implicitly_wait(5)

# validate the Create button
webElement = driver.find_element_by_id("createRoom")
print("This is " + str(webElement))
driver.implicitly_wait(10) # this delay is before closing

# closing the annoying chrome
driver.close()