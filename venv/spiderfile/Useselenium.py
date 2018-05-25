# selenium使用：
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome()
try:
    browser.get('https://www.taobao.com/')
    input = browser.find_element_by_id('q')
    input.send_keys('Hello world~!')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'mainsrp-pager')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    time.sleep(15)
    browser.close()