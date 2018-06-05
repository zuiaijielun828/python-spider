#壹钱包抢购-网页版开始
# !/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time
#6.6
url='https://m.yqb.com/mall/detail/376561?productId=376561&sceneMode=omp&yqb_disambiguity_uid=881950501212101101'
options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}#不加载图片
options.add_experimental_option("prefs",prefs)
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 7.0; STF-AL10 Build/HUAWEISTF-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043508 Safari/537.36 V1_AND_SQ_7.2.0_730_YYB_D QQ/7.2.0.3270 NetType/4G WebP/0.3.0 Pixel/1080"')

def checkisneed():
    t = time.gmtime()
    min=58
    sec=10
    print("开始校验时间,现在是:"+str(t.tm_min)+'分:'+str(t.tm_sec)+'秒')
    print("目标时间是:" + str(min) + '分后开始尝试请求')
    if t.tm_min<min:
        print('XXX现在是:'+str(t.tm_min)+'分,时间未到，休息30秒')
        time.sleep(30)
        return 'need'
    return 'no'
def checktime(browser):
    while checkisneed()=='need':
        browser.get(url)
def req(browser):
    browser.get(url)
    checktime(browser) #校验时间
    print('开始尝试...')
    wait = WebDriverWait(browser, 1)
    while True:
        try:
            browser.get(url)
            buy = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#shop_detail .button-wrapper button[data-event='马上抢']")))
            buy.click()
            queren = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#shop_detail .button-wrapper button[data-event='马上抢']")))
            queren.click()
            time.sleep(1)
            queren1 = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#buybutbox .button-wrapper button[data-event='确认']")))
            queren1.click()
            print("购买成功,请继续完成支付~")
            break
        except Exception as e:
            print(str(e))
def main():
    browser = webdriver.Chrome(chrome_options=options)
    for i in range(1):
        req(browser)
main()
#壹钱包抢购-网页版结束