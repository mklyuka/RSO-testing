from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
link = 'http://localhost:8080/'
browser = webdriver.Chrome()
 
try:
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Имя"]#name')
    name.send_keys('ВинДизель')

    password = browser.find_element(By.CSS_SELECTOR, '[placeholder="Пароль"]#password')
    password.send_keys('Qwerty123')


finally:
    time.sleep(5)
    browser.quit()