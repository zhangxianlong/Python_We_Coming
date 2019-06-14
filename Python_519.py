#coding=utf-8
from appium import webdriver
"""
打开雪球 添加自选股 输入alibaba 添加到自选股
"""

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"                   # 让Appium自动确定应用程序需要哪些权限，并在安装时将其授予应用程序
caps["autoGrantPermissions"] = "true"
caps["unicodeKeyboard"] = "true"                        #支持中文输入
caps["resetKeyboard"] = "true"                          #隐藏键盘

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(20)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("alibaba")
if driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView"):
    print ("已经添加到自选了")
else:
    el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView")
    el5.click()

driver.quit()

