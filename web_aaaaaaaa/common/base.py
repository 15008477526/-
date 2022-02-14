'''
'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from faker import Faker

# 打开浏览器
def open_browser(browser='chrome'):

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "ie":
        driver = webdriver.Ie()
    # elif browser == "safari":
    #     driver = webdriver.safari()
    else:
        print('输入有误,请重新输入')
        driver = None
    return driver


class Base(object):

    def __init__(self,driver):
        """
        初始化浏览器
        :param driver:
        """
        self.driver = driver

    # 打开网址
    def open_url(self,url):

        self.driver.get(url)
        # 浏览器最大化
        self.driver.maximize_window()

    # 定位单个元素
    def find_element(self,locator,timeout=10):

        try:
            element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        except:
            print(f"元素{locator}没找到")
            element = None
        return element


    # 定位一组元素
    def find_elements(self,locator,timeout=10):

        try:
            elements = WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
        except:
            print(f"元素{locator}没找到")
            elements = None
        return elements

    # 点击元素
    def click(self,locator):
        try:
            element = self.find_element(locator)
            element.click()
        except Exception as e:
            print(f'报错,{e}')

    # 输入操作
    def send_keys(self,locator,text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f'报错,{e}')

    # 判断文本是否在元素中
    def is_text_in_element(self,locator,text,timeout=10):
        try:
            result=WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element(locator,text))
            return  result
        except:
            print(f"元素{locator}没找到")
            return False

    # 判断文本是否在元素的value中
    def is_value_in_element(self,locator,value,timeout=10):
        try:
            result = WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element_value(locator,value))
            return result
        except:
            print(f"元素{locator}没找到")
            return False

    # 判断元素是否被选中
    def is_selected(self,locator):
        element =self.find_element(locator)
        try:
            result = element.is_selected()
            return result
        except:
            return False


    # 关闭浏览器
    def close(self):

        self.driver.quit()

    # 鼠标双击操作
    def double_click(self,locator):
        element = self.find_element(locator)
        ActionChains(self.driver).double_click(element).perform()

    def back(self):
        '''返回'''
        self.driver.back()

    # 下拉框选择
    def clickSelect(self,select_loc):
        import random
        try:
            # 先找到select标签
            select = self.find_element(select_loc)
            # 标签下所有option选项列表
            select_list=select.find_elements_by_tag_name("option")
            num=random.randint(1,len(select_list)-1)
            # 通过索引来随机选取
            Select(select).select_by_index(num)
        except:
            print("")

    # 进入iframe id/name/元素定位
    def switch_to_frame(self,i):
        self.driver.switch_to.frame(i)

    # 退出到父iframe
    def quit_patent_frame(self):
        self.driver.switch_to.parent_frame()

    # 跳出到最外层
    def quit_frame(self):
        self.driver.switch_to.default_content()

    # 复选框选择方法
    def select_checkbox(self):
        try:
            boxes =self.driver.find_elements_by_css_selector('input[type="checkbox"]')
            for box in boxes:
                if box.is_selected():
                    box.click()
                else:
                    pass
        except:
            print('有错了')



    # 滚动条下拉至底
    def scroll_down(self):
        js_down='window.scrollTo(0,10000);'
        self.driver.execute_script(js_down)

    # 滚动条至顶
    def scroll_up(self):
        js_up='window.scrollTo(0,0);'
        self.driver.execute_script(js_up)

    # 滚动至某一元素
    def scroll_element(self,locator):
        js_one='arguments[0].scrollIntoView();'
        self.driver.execute_script(js_one,self.find_element(locator))

    # 获取当前页面网址
    def get_current_url(self):
        url = self.driver.current_url
        return url

    def click_elements(self, locator, index):
        """点击多一个元素"""
        elements = self.find_elements(locator)
        elements[index].click()

    def displayed(self, locator):
        """判断元素是否存在"""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False

    # 获取弹窗
    def get_alter(self):
        alter = self.driver.switch_to.alert
        if len(alter.text):
            return True
        else:
            return False


if __name__ == '__main__':
    import time
    driver = open_browser("chrome")
    base = Base(driver)
    base.open_url("http://www.baidu.com/")
    # 搜索框定位器
    search_loc = ("id","kw")
    # 按钮定位器
    button_loc = ("id","su")
    # 搜索框输入
    # base.send_keys(search_loc,"lol")
    # # 点击百度一下
    # base.click(button_loc)

    # 判断文本是否在元素的value属性值中
    value ='百度一下'
    result =base.is_value_in_element(button_loc,value)
    print(result)
    time.sleep(3)
    base.close()
