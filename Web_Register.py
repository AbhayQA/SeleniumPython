from selenium import webdriver
import time
#driver and browser setup
driver = webdriver.Chrome(executable_path="C:/chromedriver")
browser = driver.get('https://www.appannie.com/')
driver.maximize_window()
#Start of register flow from home page
registerLink = driver.find_element_by_class_name('login-button')
registerLink.click()
driver.implicitly_wait(5)
#Enter details to complete registration process
emailField = driver.find_element_by_id('email')
emailField.send_keys('test@gmail.com')
passwordField = driver.find_element_by_id('password')
passwordField.send_keys('Hello123')
firstName = driver.find_element_by_id('firstname')
firstName.send_keys('Automation')
lastName = driver.find_element_by_id('lastname')
lastName.send_keys('Python')
jobFunction = driver.find_element_by_class_name('select-arrow')
jobFunction.click()
options = driver.find_element_by_class_name('select-option')
options.click()
#Quitting flow without completing registration flow
time.sleep(5)
driver.quit()
