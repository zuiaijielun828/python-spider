from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urlencode
import time
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq


browser = webdriver.Chrome()
wait = WebDriverWait(browser,30)
def getPage():
    try:
        browser.get('https://detail.tmall.com/item.htm?id=10527459158&amp;ns=1&amp;abbucket=0#description')
        time.sleep(20)
        #累计评价按钮
        pageInput = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "a[data-index='1']")))
        print(pageInput.text)
        time.sleep(20)
        pageInput.click()
        time.sleep(20)
        getInfo(browser.page_source)
    except BaseException as e:
        print('发生错误:e='+str(e))

def getInfo(html):
    print(html)
    doc = pq(html)
    items = doc('.tm-rate-fulltxt').items()
    for item in items:
        print(item.text())

def main():
    getPage()
    browser.close()
main()