from selenium import webdriver
import time
#driver and browser setup
driver = webdriver.Chrome(executable_path="C:/chromedriver")
browser = driver.get('https://www.appannie.com/')
driver.maximize_window()
#Start of login flow from home page
loginLink = driver.find_element_by_id('login-button')
loginLink.click()
driver.implicitly_wait(5)
#Enter login credentials
emailField = driver.find_element_by_id('email')
emailField.send_keys('test@gmail.com')
passwordField = driver.find_element_by_id('password')
passwordField.send_keys('pswpsw123')
#Click on home page - Error will be thrown as login detail is not valid
options = driver.find_element_by_id('submit')
options.click()
time.sleep(5)
driver.quit()
