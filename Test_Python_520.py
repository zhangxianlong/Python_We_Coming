# coding:utf-8

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
import  time

"""
1 、进入雪球首页，进入基金的新闻页（不是第一个基金按钮），对他以及它右侧的每个新闻栏目，
执行上滑5次，进入下个栏目用从右边到左边滑动
2、滑动使用相对坐标，不使用绝对坐标
"""

class Test_Python_520(object):

    #获取启动的appium的driver实例，用于后续每个case的driver
    def setup_method(self):
        #重启APP
        self.driver=self.restart_app()
        #进入基金这个栏目
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']").click()

    #基金从上往下滑五次
    def test_Fund_TowardsDown(self):
       for i in range(7):
            #由下向上滑动
            for i in range(5):
                Test_Python_520.towards(self,0.8,0.8,0.2,0.2)
            #由右向左滑动
                Test_Python_520.towards(self,0.8,0.8,0.2,0.8)

    #封装的一个方法：实现屏幕滑动
    def towards(self,w1,h1,w2,h2):
        #获取当前屏幕的大小
        rect=self.driver.get_window_rect()
        time.sleep(2)
        action = TouchAction(self.driver)
        #TouchAction方法：press类似按压屏幕，release类似取消按压屏幕，Perform类似发送指令
        action.press(x=rect['width']*w1, y=rect['height']*h1).move_to(x=rect['width']*w2, y=rect['height']*h2).release().perform()
        time.sleep(2)

    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        caps['noReset']=True
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver


