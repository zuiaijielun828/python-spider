# python驱动app
#手机需要开发模式打开USB连接电脑
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

datestr=''
parm = {"platformName": "Android",
        "deviceName": "mbj-mi", #value随便写
        "appPackage": "com.paic.zhifu.wallet.activity",#app包名，可以上小米商店查看
        "appActivity": "modules.guide.LoadingActivity", #通过包名查看程序的入口
        "newCommandTimeout": "180000",#session不操作超时时间，默认60S
        "noReset": "True"  # 加这个参数可以免登陆，只要手机上已经登陆即可
        }

driver = webdriver.Remote('http://localhost:4723/wd/hub', parm)

def spider():
    global datestr
    wait = WebDriverWait(driver, 30)
    gouwu=wait.until(ec.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ImageView")))
    for i in driver.find_elements_by_class_name('android.widget.TextView'):
        if i.text == '购物':
            #print(driver.page_source)
            i.click()
            time.sleep(3)
            break
    findbuy()
    print("spider 结束")
def findbuy():
    driver.swipe(36, 500, 36, 100)
    while True:
        find='no'
        for i in driver.find_elements_by_class_name('android.widget.TextView'):
            if i.text == datestr:
                find='yes'
                buy(i)
                break
        if find=='yes':
            break
        driver.swipe(36, 600, 36, 100)
def getdatestr():
    global datestr
    t=time.gmtime()
    month='%02d'%t.tm_mon
    dat = '%02d' % t.tm_mday
    date=month+'月'+dat+'日'
    datestr=date+'10:00抢'
    print('目标日期:'+datestr)

def buy(one):
    global datestr
    x=one.location['x']
    y=one.location['y']
    checktime()
    one.click()

    while True:
        print("try...")
        try:
            tmp2 = driver.find_element_by_android_uiautomator('new UiSelector().text("马上抢")')
            dobuy(tmp2)
            #break
        except BaseException as e:
            pass
        driver.back()#还未开始，返回重新进
        driver.tap([(x,y)])#重新进入页面

def checktime():
    t = time.gmtime()
    min=55
    sec=10
    print("开始校验时间,现在是:"+str(t.tm_min)+'分:'+str(t.tm_sec)+'秒')
    print("目标时间是:" + str(min) + '分:' + str(sec) + '秒后开始尝试请求')
    while not (t.tm_min==min and t.tm_sec>sec):
        time.sleep(1)
        t = time.gmtime()
def dobuy(tmp2):
    print("...buy...")
    tmp2.click()
    try:
        queding = driver.find_element_by_android_uiautomator('new UiSelector().text("确定")')
        queding.click()
        queren = driver.find_element_by_android_uiautomator('new UiSelector().text("确认")')
        queren.click()
        print("buy 成功~~~~")
    except BaseException as e:
        pass

def main():
    global datestr
    print("spider 开始...")
    #datestr='06月02日10:00抢'
    getdatestr()
    spider()
main()

