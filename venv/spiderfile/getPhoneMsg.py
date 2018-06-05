# 获取短信验证
#手机需要开发模式打开USB连接电脑
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import re
datestr=''
parm = {"platformName": "Android",
        "deviceName": "mbj-mi", #value随便写
        "appPackage": "com.samsung.android.messaging",#app包名，可以上小米商店查看
        "appActivity": "com.android.mms.ui.ConversationComposer", #通过包名查看程序的入口
        "newCommandTimeout": "180000",#session不操作超时时间，默认60S
        "noReset": "True"  # 加这个参数可以免登陆，只要手机上已经登陆即可
        }

driver = webdriver.Remote('http://localhost:4723/wd/hub', parm)

def spider():
    print("spider开始...")
    back = driver.find_element_by_id("com.samsung.android.messaging:id/actionbar_arrow")
    back.click()
    driver.implicitly_wait(2)
    num = driver.find_element_by_id("com.samsung.android.messaging:id/from")
    print(num.text)
    subject = driver.find_element_by_id("com.samsung.android.messaging:id/subject")
    print(subject.text)
    code=re.search('\d{4,6}',subject.text)
    print("code="+code.group())
    print("spider结束")
    return code.group()
spider()


