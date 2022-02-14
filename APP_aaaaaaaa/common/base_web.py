from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from random import choice
from time import sleep


def open_browser(browser: str = "chrome"):
    """打开浏览器"""
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()

    elif browser.lower() == "ie":
        driver = webdriver.Ie()

    else:
        print("输入的浏览器名称错误")
        driver = None
        return driver

    return driver


class BaseWeb(object):
    def __init__(self, driver):
        self.driver = driver

    # 打开网址并最大化浏览器窗口
    def get_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    # 打开网址
    def get_url_no_max(self,url):
        self.driver.get(url)

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 定位单个元素
    def find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # 定位多个元素
    def find_elements(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    # 判断文本是否包含于元素
    def is_text_in_element(self, locator, text, timeout=2):
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    # 判断value是否包含于元素value
    def is_value_in_element(self, locator, value, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, value))
        except:
            return False

    # 点击元素
    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    # 元素输入
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        # ActionChains(self.driver).double_click(element).perform()
        element.clear()
        element.send_keys(text)

    # 判断元素是否已选
    def ele_is_selected(self, locator):
        try:
            result = self.find_element(locator).is_selected()
            if result:
                return result
        except:
            return False

    # 确认弹窗
    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    # 获取重名标签的个数
    def get_length_of_elements(self, locator):
        length = len(self.find_elements(locator))
        return length

    # 鼠标悬停
    def move_to_element(self, locator):
        self.driver.move_to_element(self.find_element(locator))

    # 通过选项顺序选择下拉菜单选项
    def select_by_num(self, locator):
        selects = self.find_elements(locator)
        del selects[0]
        select = choice(selects)
        select.click()
        sleep(1)

    # 通过选项顺序选择下拉菜单选项
    def select_by_num_1(self, locator):
        selects = self.find_elements(locator)
        del selects[0]
        del selects[-1]
        del selects[-2]
        select = choice(selects)
        select.click()
        sleep(1)

    # 聚焦元素
    def focus_element(self, locator):
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, self.find_element(locator))

    # 切换iframe
    def switch_to_frame(self, i):
        self.driver.switch_to.frame(i)

    # 退出当前层iframe
    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    # 随机选择下拉菜单的一个选项
    def select_by_random(self, locator):
        options = self.find_elements(locator)
        option = choice(options)
        option.click()

    # 上传文件
    def upload_file(self, locator, file_path):
        element = self.find_element(locator)
        element.send_keys(file_path)
        sleep(1)

    # 滚动页面到顶部
    def scroll_to_top(self):
        js = 'window.scrollTo(0,0)'
        self.driver.execute_script(js)

    # 全选复选框
    def click_all_checkboxes(self, locator):
        boxes = self.find_elements(locator)
        for box in boxes:
            if not box.is_selected():
                box.click()

    # 鼠标双击
    def double_click(self, locator):
        element = self.find_element(locator)
        ActionChains(self.driver).double_click(element).perform()

    # 确认弹窗
    def alert_accept(self, locator):
        self.find_element(locator).click()
        sleep(1)
        self.driver.switch_to.alert.accept()

    # 返回前一个页面
    def back(self):
        self.driver.back()

    # 切换到最外层frame
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    # 刷新页面
    def refresh(self):
        self.driver.refresh()

    # 获取所有窗口句柄
    def window_handles(self):
        return self.driver.window_handles

    # 切换窗口句柄
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    # 获取元素文本
    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def login_by_cookie(self):
        """使用cookie绕过验证码登录"""
        url = 'http://b2t.tp-shop.cn/index.php/Admin/Admin/login'
        self.get_url_no_max(url)
        cookies = [{'name': 'PHPSESSID', 'value': 'rugv9sn5ku58v9nu5ii87ltum7'},
                   {'name': 'admin_type', 'value': '1'},
                   {'name': 'workspaceParam', 'value': 'welcome%7CIndex'}
                   ]

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()


if __name__ == '__main__':
    """测试代码"""
    from time import sleep

    base = BaseWeb(open_browser())
    base.get_url("http://192.168.244.130/ecshop/user.php?act=address_list")
    base.send_keys(("name", "username"), "admin")
    base.send_keys(("name", "password"), "123456")
    base.click(("class name", "us_Submit"))
    # select = base.get_length_of_elements(("css selector", "#selCountries_0"))
    # print(base._Base__find_element(("css selector", "#selCountries_3")).get_attribute("outerHTML"))
    sleep(3)
    print(base.is_text_in_element(("class name", "f4_b"), "admin"))
