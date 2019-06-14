# coding:utf-8

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC

"""
1、模拟器上，APP的webview页面测试
2、交易->基金->已有蛋卷账户登录->密码登陆,输入错误的用户名和密码，点击安全登陆
"""

class Test_Python_602(object):

    # 获取启动的appium的driver实例，用于后续每个case的driver
    def setup_class(self):
        #重启APP
        self.driver=self.restart_app()

    def setup_method(self):
        #等待交易按钮出现
        WebDriverWait(self.driver,40).until(EC.presence_of_element_located((MobileBy.XPATH,"//*[@text='交易']")))
        # 点击底部按钮【交易】
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='交易']").click()

    def test_fund_login(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/page_type_fund").click()
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[@content-desc='已有蛋卷基金账户登录']")))
        self.driver.find_element_by_accessibility_id("已有蛋卷基金账户登录").click()
        self.driver.find_element_by_accessibility_id("使用密码登录").click()
        self.driver.find_element_by_id("telno").send_keys("16777777777")
        self.driver.find_element_by_id("pass").send_keys("123456")
        self.driver.find_element_by_accessibility_id("安全登录").click()
        str = self.driver.find_element_by_id("android:id/button1").text
        self.driver.find_element_by_id("android:id/button1").click()
        assert str == "确定"

    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        caps['noReset'] = True
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

