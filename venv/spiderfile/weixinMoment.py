# python驱动app
#手机需要开发模式打开USB连接电脑
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

parm = {"platformName": "Android", "deviceName": "mbj-mi", "appPackage": "com.tencent.mm",
        "appActivity": "ui.LauncherUI", "noReset": "True"  # 加这个参数可以免登陆，只要手机上已经登陆即可
        }
print("login 开始")
driver = webdriver.Remote('http://localhost:4723/wd/hub', parm)
mynames=[]
contents=[]
def loginweixin():

    #el1 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
    #el1.click()
    #el1.click()
    wait = WebDriverWait(driver, 30)
    #login = wait.until(ec.presence_of_element_located((By.ID, "com.tencent.mm:id/cfy")))
    #login = driver.find_element_by_id("com.tencent.mm:id/cfy")
    #login.click()
    #phone = wait.until(ec.presence_of_element_located((By.ID, "com.tencent.mm:id/h2")))
    #phone = driver.find_element_by_id("com.tencent.mm:id/h2")
    #phone.set_text('18686681293')
    time.sleep(5)
    el7 = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"当前所在页面,与梦因你而美…的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")
    el7.click()
    time.sleep(2)
    el8 = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"当前所在页面,与梦因你而美…的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
    el8.click()
    print("login OK")

def spiderMoments():
    time.sleep(3)
    driver.swipe(36, 500, 36, 125) #切换到内容位置
    #:通过appuim的日志，根据汉字内容查询标签，以及id等属性
    names=driver.find_elements_by_id('com.tencent.mm:id/apv')
    contents = driver.find_elements_by_id('com.tencent.mm:id/deq')
    for i in range(len(names)):
        if i<len(names)-1:
            print('name='+names[i].text)
        if i< len(contents):
            print('contents=' + contents[i].text)
    for q in range(3):
        driver.swipe(18, 900, 18, 140)
        time.sleep(3)
        names=driver.find_elements_by_id('com.tencent.mm:id/apv')
        contents = driver.find_elements_by_id('com.tencent.mm:id/deq')
        for i in range(len(names)):
            if i > 0:
                print('name=' + names[i].text)
            if i < len(contents):
                print('contents=' + contents[i].text)




loginweixin()
spiderMoments()