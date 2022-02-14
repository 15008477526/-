'''
@author:魏江霖
@time:2019/9/15

'''
from page.register import Register,register_url
from common.base import open_browser
from common.operate_excel import OperationExcel
import unittest
from common.random_faker import randomData
oper=OperationExcel('./data/register.xls')




class TestRegister(unittest.TestCase):
    '''测试注册'''
    def setUp(self):
        driver = open_browser('chrome')  # 打开浏览器
        self.register = Register(driver)
        self.register.open_url(register_url)  # 打开网址

    def tearDown(self):
        self.register.close()


    def test_case_1(self):

        data = randomData()
        # 输入用户名
        self.register.input_username(data[0])
        # 输入email
        self.register.input_email(data[3])

        password =data[4]
        # 输入密码
        self.register.input_password(password)
        # 确认密码
        self.register.input_confirm_password(password)
        # 手机输入
        self.register.input_phone(data[4])
        # 密码提示问题
        self.register.click_password_question()
        # 密码问题
        self.register.input_question(data[4])

        # 点击立即注册
        self.register.click_register()
        # 点击忘记密码
        # self.register.click_forget()
        oper.write_data(data)