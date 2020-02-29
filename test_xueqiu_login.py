import time
from cmath import rect
from platform import release

import action as action
from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class TestXueqiuAndroid(object):
    driver=WebDriver
    @classmethod
    def setup_class(cls):
        print("setup class在当前类下的所有用例执行之前只执行一次")
        cls.driver=cls.install_app()

        el1=cls.driver.find_element_by_id("user_profile_icon")
        el1.click()

    def setup_method(self):
        print("setup method在每个测试用例执行之前执行一次")
        #获取启动的appium的driver实例，用于后续每个case的driver
        self.driver= TestXueqiuAndroid.driver

        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_login").click()

    def test_login_phone(self):
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others").click()
        # el3.click()
    #
    def test_login_password(self):
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others").click()
        self.driver.find_element_by_xpath("//*[@text='邮箱手机号密码登录']").click()



    #
    # def test_login_error_password(self):
    #     el1 = TestXueqiuAndroid.driver.find_element_by_id("com.xueqiu.android:id/tab_icon")
    #     el1.click()
    #     el2 = TestXueqiuAndroid.driver.find_element_by_id("com.xueqiu.android:id/tv_login_phone")
    #     el2.click()
    #     el3 = TestXueqiuAndroid.driver.find_element_by_id("com.xueqiu.android:id/weixin_login")
    #     el3.click()

    # def test_login_password(self):
    #     el3 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others")
    #     el3.click()
    #     self.driver.find_element_by_xpath("//*[@text='邮箱手机号密码登录']").click()

    def teardown_method(self):
        #不加也没关系，如果不quit，启动appium会自动quit之前的session
        self.driver.quit()


    @classmethod
    def install_app(cls) -> WebDriver:
        caps = {}
        #如果有必要，进行第一次安装
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0.1"
        caps["deviceName"] = "e398de2d"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #解决第一次启动的问题
        caps["autoGrantPermissions"] = "true"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    @classmethod
    def restart_app(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0.1"
        caps["deviceName"] = "e398de2d"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #caps["autoGrantPermissions"] = "true"
        caps["noReset"] = True
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

