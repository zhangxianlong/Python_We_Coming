# coding:utf-8

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest

"""
1、完成雪球登录场景的测试，要带有setup_class setup_method
2、微信 验证码 密码 错误的用户名 错误的密码 至少编写5条用例
"""

class Test_Python_530(object):

    # 获取启动的appium的driver实例，用于后续每个case的driver
    def setup_class(self):
        #重启APP
        self.driver=self.restart_app()

    def setup_method(self):
        self.driver.find_element_by_id("tv_login").click()

    #手机及其他登录方式->错误验证码登录
    def test_login_iphone_sendcode(self):
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        self.driver.find_element_by_id("register_phone_number").send_keys("15600812257")
        self.driver.find_element_by_id("register_code_text").click()
        self.driver.find_element_by_id("register_code").send_keys("1234")
        self.driver.find_element_by_id("button_next").click()
        str = self.driver.find_element_by_id("md_content").text
        self.driver.find_element_by_id("md_buttonDefaultPositive").click()
        assert str =="验证码错误"

    # 手机及其他登录方式->邮箱手机号密码登录->错误密码登录
    def test_login_iphone_password(self):
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        self.driver.find_element_by_id("tv_login_with_account").click()
        self.driver.find_element_by_id("login_account").send_keys("15600812257")
        self.driver.find_element_by_id("login_password").send_keys("123456")
        self.driver.find_element_by_id("button_next").click()
        str = self.driver.find_element_by_id("md_content").text
        self.driver.find_element_by_id("md_buttonDefaultPositive").click()
        assert str =="用户名或密码错误"

    #手机及其他登录方式->邮箱手机号密码登录->错误邮箱号登录
    def test_login_iphone_email(self):
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        self.driver.find_element_by_id("tv_login_with_account").click()
        self.driver.find_element_by_id("login_account").send_keys("qwewqe@21323.com")
        self.driver.find_element_by_id("login_password").send_keys("123456")
        self.driver.find_element_by_id("button_next").click()
        str = self.driver.find_element_by_id("md_content").text
        self.driver.find_element_by_id("md_buttonDefaultPositive").click()
        assert str =="用户名或密码错误"

    #手机及其他登录方式->邮箱手机号密码登录->错误手机号登录
    def test_login_iphone_username(self):
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        self.driver.find_element_by_id("tv_login_with_account").click()
        self.driver.find_element_by_id("login_account").send_keys("qweqwrw")
        self.driver.find_element_by_id("login_password").send_keys("123456")
        self.driver.find_element_by_id("button_next").click()
        str = self.driver.find_element_by_id("md_content").text
        self.driver.find_element_by_id("md_buttonDefaultPositive").click()
        assert str =="手机号码填写错误"

    #微信登录->未安装微信
    def test_login_wechat(self):
        self.driver.find_element_by_id("rl_login_by_wx").click()
        # 用于生成xpath定位 相当于 "//*[@text='您尚未安装微信，请先安装微信']"
        toast_message = "您尚未安装微信，请先安装微信"
        message = '//*[@text=\'{}\']'.format(toast_message)
        #获取toast提示内容
        toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
        print(toast_element.text)
        assert toast_element.text == "您尚未安装微信，请先安装微信"

    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        caps['noReset']=True
        caps['automationName'] = "uiautomator2"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(100)      #隐式等待，直到找到目标为止
        driver.find_element_by_id("user_profile_icon").click()
        return driver

    #判断元素是否存在
    def is_element_exist(self,element):
        source = self.driver.page_source
        print(source)
        if element in source:
            return True
        else:
            return False

    def teardown_method(self):
        if self.is_element_exist("第三方登录"):
            self.driver.find_element_by_id("iv_action_back").click()
        else:
            self.driver.find_element_by_id("iv_close").click()

    def teardown_class(self):
        self.driver.quit()
