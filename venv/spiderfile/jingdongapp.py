# python驱动app
#手机需要开发模式打开USB连接电脑，并启动appium
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

parm = {"platformName": "Android",
        "deviceName": "mbj-mi", #value随便写
        "appPackage": "com.jingdong.app.mall",#app包名，也可以使用adb logcat ActivityManager:I *:s 然后启动应用，查看日志找cmp=ComponentInfo{com.jingdong.app.mall/com.jingdong.app.mall.main.MainActivity}} 分别是包名和入口
        "appActivity": "com.jingdong.app.mall.main.MainActivity", #通过包名查看程序的入口
        "newCommandTimeout": "180000",#session不操作超时时间，默认60S
        "noReset": "True", #加这个参数可以免登陆，只要手机上已经登陆即可
        "unicodeKeyboard":"True"#支持输入中文，否则只能输入英文字母，数字也无法输入
        }

driver = webdriver.Remote('http://localhost:4723/wd/hub', parm)
wait = WebDriverWait(driver, 5)
def inputSearchKey(searchKey):
    gouwu = wait.until(ec.presence_of_element_located((By.ID,"com.jingdong.app.mall:id/a2h")))
    gouwu.click()
    input = wait.until(ec.presence_of_element_located((By.ID, "com.jd.lib.search:id/search_text")))
    input.set_text(searchKey) #send_keys('iphone')无法输入，用set_text可以输入。
    search = driver.find_element_by_id("com.jd.lib.search:id/search_btn")
    search.click()
    page=driver.page_source #电脑测返回的是执行js后的代码，手机端是执行前的，可借助mitmdump -s xxx.py代理使用脚本拦截请求即可拿到response，通过解析response获取数据 。
    soup = BeautifulSoup(page, 'lxml')
    #print(soup.prettify())
    for i in range(3):
        prods = driver.find_elements_by_id("com.jd.lib.search:id/product_item_name")#通过appium后台日志也能拿到response
        prices = driver.find_elements_by_id("com.jd.lib.search:id/product_item_jdPrice")
        for i in range(len(prices)-2):
            if prods[i].location['y'] > prices[i].location['y']:
                print('书名:《' + prods[i].text + '》;   :' + prices[i+1].text)
            else:
                print('书名:《' + prods[i].text + '》;   :' + prices[i].text)
            prods[i].click()
            time.sleep(2)
            driver.swipe(36, 800, 36, 100)
            #逐个抓评价省略
            driver.back()
        driver.swipe(36, 1300, 36, 100)
        time.sleep(2)

def main():
    print("spider开始...")
    inputSearchKey("python3网络爬虫实战教程")
    print("spider结束")

main()