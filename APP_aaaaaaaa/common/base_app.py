"""@author:郁华夏"""

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import random

desired_caps = {
    'platformName': 'android',
    'platformVersion': '5.1.1',
    'deviceName': '36b7119e',
    'appPackage': 'com.tpshop.malls',
    'appActivity': '.SPMainActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True
}


def open_app():
    """打开app"""
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


class BaseApp(object):
    def __init__(self, driver):
        self.driver = driver

    def quit(self):
        """关闭app"""
        self.driver.quit()

    def wait_page(self):
        """等待页面加载完成"""
        try:
            ac = self.driver.current_activity
            self.driver.wait_activity(ac, 5, 0.5)
        except:
            return False

    def find_element(self, locator):
        """定位单个元素"""
        try:
            if locator[0] == 'id':
                return self.driver.find_element_by_id(locator[1])
            elif locator[0] == 'class':
                return self.driver.find_element_by_class_name(locator[1])
            elif locator[0] == 'xpath':
                return self.driver.find_element_by_xpath(locator[1])
            elif locator[0] == 'content-desc':
                return self.driver.find_element_by_accessibility_id(locator[1])
        except:
            return False

    def find_elements(self, locator):
        """定位多个元素"""
        try:
            if locator[0] == 'id':
                return self.driver.find_elements_by_id(locator[1])
            elif locator[0] == 'class':
                return self.driver.find_elements_by_class_name(locator[1])
            elif locator[0] == 'xpath':
                return self.driver.find_elements_by_xpath(locator[1])
            elif locator[0] == 'content-desc':
                return self.driver.find_elements_by_accessibility_id(locator[1])
        except:
            return False

    def click(self, locator):
        """点击"""
        element = self.find_element(locator)
        try:
            element.click()
        except:
            return False

    def send_keys(self, locator, text):
        """输入"""
        element = self.find_element(locator)
        try:
            element.clear()
            element.send_keys(text)
        except:
            return False

    def get_ele_text(self, locator):
        """获取元素文本"""
        element = self.find_element(locator)
        result = element.text
        return result

    def random_click(self, locator):
        """随机点击一个元素"""
        elements = self.find_elements(locator)
        element = random.choice(elements)
        element.click()

    def tap(self, horizon, vertical):
        TouchAction(self.driver).tap(x=horizon, y=vertical).perform()

    def iterate_and_click(self, locator):
        elements = self.find_elements(locator)
        for element in elements:
            element.click()
