'''
调用Page文件夹
'''
from common.base import Base
from page.login_page import LoginPage,login_url
from common.base import open_browser
import unittest,ddt
from common.operate_excel import OperationExcel
opera =OperationExcel('./data/data.xls')
# 打开已注册的表
data =opera.get_data_by_index()


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        driver=open_browser('chrome')  # 打开浏览器
        self.bs = Base(driver)
        self.login =LoginPage(driver)
        self.login.open_url(login_url) # 打开网址

    def tearDown(self):
        self.login.close()

    @ddt.data(*data)
    def test_case(self,data):
        '''测试登录'''
        from time import sleep
        # 输入用户名
        self.login.input_username(data['username'])
        # 输入密码
        self.login.input_password(data['password'])
        # 点击记住密码
        self.login.click_remember()
        # 点击登录按钮
        self.login.click_submit()
        sleep(2)
        # 实际结果
        # result =self.is_login_succeed(data['username'])
        # 看退出按钮是否可见
        result =self.bs.displayed(self.login.quit_loc)
        # self.assertEqual(result,data['expect'],msg='用例执行失败')
        self.assertTrue(result,msg='用例执行失败')


    def is_login_succeed(self,text):
        return self.login.is_text_in_element(self.login.user_loc,text)

if __name__ == '__main__':
    unittest.main(verbosity=2)
