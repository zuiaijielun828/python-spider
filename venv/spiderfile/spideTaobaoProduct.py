#爬淘宝开始：
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
wait = WebDriverWait(browser,20)
def getPage():
    try:
        base_url='https://s.taobao.com/search?'
        params = {
            'q': 'python书籍'
        }
        url = base_url + urlencode(params)
        browser.get(url)
        #CSS_SELECTOR  [标签].class  #id  多个class必须带标签名
        pageInput=wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,'input.input.J_Input')))
        comfirmButton=wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,'span.btn.J_Submit')))
        #print(pageInput.get_attribute('type'))
        #print(comfirmButton.get_attribute('role'))
        html=browser.page_source
        #print(html[0:3000])
        getInfo(html)
        for i in range(3,3):
            pageInput.clear()
            pageInput.send_keys(i)
            time.sleep(1)
            comfirmButton.click()
            wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR,'span.num'), str(i)))#页码高亮选中
            wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(i)))#按钮可点
            html = browser.page_source
            print('第'+i+'页获取成功')
            time.sleep(60)
            #getInfo(html)
    except BaseException as e:
        print('发生错误:e='+str(e))

def getInfo(html):
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
    print(product)
def main():
    getPage()
    #browser.close()
main()
#结束
