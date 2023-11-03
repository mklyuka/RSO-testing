from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
link = 'http://localhost:8080/'
browser = webdriver.Chrome()
browser.get(link)
 
time.sleep(7)
 
browser.quit()