from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
link = 'https://demo.applitools.com/'
browser = webdriver.Chrome()
browser.get(link)
 
time.sleep(2)
 
username = browser.find_element(By.ID, 'username')
username.send_keys('Maksim')
 
time.sleep(2)
 
password = browser.find_element(By.ID, 'password')
password.send_keys('Qwerty1!')
 
time.sleep(2)
 
button = browser.find_element(By.ID, 'log-in')
button.click()
 
time.sleep(2)
 
browser.quit()