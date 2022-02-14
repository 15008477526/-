'''
@author:雷雨



'''
import time
import unittest
from common.random_faker import randomData
from page.add_address import AddDress, add_address_url
from page.modify_address import ModifyAddress, url
from common.base import open_browser
from page.login_page import LoginPage


class TestModify(unittest.TestCase):
    def setUp(self):
        self.driver = open_browser('firefox')  # 打开浏览器
        self.modify = LoginPage(self.driver)  # 实例化LoginPage
        self.modify.open_url(add_address_url)  # 打开登录地址
        self.login = AddDress(self.driver)  # 实例化
        self.modify = ModifyAddress(self.driver)  # 实例化
        self.modify.input_username('123456')  # 登录用户账号
        self.modify.input_password('123456')  # 登录密码
        self.modify.click_submit()  # 点击登录按钮
        self.random_list = randomData()



    def tearDown(self):
        self.driver.quit()
    # @unittest.skip("")

    # 添加
    def test_case(self):
        # 收货地址
        self.login.recevied_good()
        # 省
        self.login.add_province()
        # 市
        self.login.add_city()
        # 区
        self.login.add_area()
        '''输入框'''
        self.login.add_input_name(self.random_list[0])  # 收件人
        self.login.add_input_address(self.random_list[1])  # 详细地址
        self.login.add_input_handest(self.random_list[3])  # 手机
        self.login.add_input_tel(self.random_list[3])  # 电话
        self.login.add_input_email(self.random_list[2])  # 邮箱
        self.login.add_input_postcode(self.random_list[4])  # 邮编
        self.login.click_add()  # 点击增加
        time.sleep(2)
        self.login.click(self.login.user_loc)
        self.login.recevied_good()

        '''断言'''
        a = self.login.find_elements(("name", "consignee"))
        c = []
        for i in a:
            c.append(i.get_attribute("value"))
        name = self.random_list[0]
        self.assertTrue(name in c, msg="添加失败")

        # 删除
    def test_case_17(self):
        self.login.recevied_good()   # 点击收货地址
        a=self.modify.find_element(("id","consignee_0"))
        name=a.get_attribute("value")
        self.modify.click_delete() # 点击删除
        self.modify.tankuang()    #确定删除

        '''断言'''
        a = self.modify.find_elements(("name", "consignee"))
        c = []
        for i in a:
            c.append(i.get_attribute("value"))

        self.assertTrue(name in c, msg="删除失败")

        #  修改
    def test_case_16(self):
        self.login.recevied_good()

        '''下拉框'''
        self.modify.province()  # 省
        self.modify.city()    # 市
        self.modify.area()    # 区
        self.modify.input_name(self.random_list[0])    # 收件人
        a = self.modify.find_element(("id", "consignee_0"))
        name = a.get_attribute("value")
        self.modify.input_address(self.random_list[1])       # 详细地址
        self.modify.input_handest(self.random_list[3])   # 手机
        self.modify.input_tel(self.random_list[3])      #电话
        self.modify.input_email(self.random_list[2])    # 邮箱
        self.modify.input_postcode(self.random_list[4])   #  邮编
        self.modify.click_sure()  # 点击修改

        '''断言'''
        a = self.login.find_elements(("name", "consignee"))
        c = []
        for i in a:
            c.append(i.get_attribute("value"))
        self.assertTrue(name in c, msg="修改失败")