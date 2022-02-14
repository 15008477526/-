'''

'''

import unittest
from common.base import Base,open_browser
from page.login_page_01 import LoginPage # 导入登陆模块
from page.first_page_02 import Browse   # 导入点击首页
from page.browse_page_03 import Browse_page  # 导入选择手机该商品
from  page.buy_now_page_04 import BuyNowPage     # 导入点击立即购买
from page.purchase_page_05 import Purchase   # 导入 加入购物车
from page.settlement_page_06 import Settlement   # 导入 点击去结算
from page.place_order_07 import SubmitOrder   # 导入 点击提交订单
from time import sleep
from page.user_center_08 import UserCenter  # 点击个人中心
from page.my_order_09 import MyOrder     # 点击我的订单
from page.cancel_page import Cancel  # 点击取消订单
from page.Repurchase_page import Repurchase
from page.order_number import OrderNumber

# 验证选择申通快递,天工收银支付
class Test_case(unittest.TestCase):
    def setUp(self):
        self.driver = open_browser('chrome')    # 实例化 浏览器
        self.login = LoginPage(self.driver)     # 实例化 登陆
        self.login.open_url('http://ecshop.itsoso.cn/user.php')     # 输入网址
        self.login.input_username('zqs')    # 输入账号
        self.login.input_password('zqs950927')    # 输入密码
        self.login.click_submit()   # 点击立即登录
        self.bro = Browse(self.driver)  # 实例化 点击首页按钮
        self.bro.click_first()  # 点击首页按钮
        self.phone = Browse_page(self.driver)   # 实例化 选择手机该商品
        self.phone.click_phone()    # 选择手机
        self.buy = BuyNowPage(self.driver)  # 实例化 点击立即购买
        self.buy.buy_now()  # 点击 立即购买
        self.pur = Purchase(self.driver)   # 实例化 加入购物车
        self.pur.purchase()     # 加入购物车
        self.sett = Settlement(self.driver)     # 实例化 点击去结算
        self.sett.settlement_o1()   # 点击 去结算按钮
        self.submit = SubmitOrder(self.driver)     # 实例化 点击提交订单
        # self.pla.place_order()  # 点击 提交订单按钮
        self.user = UserCenter(self.driver)     # 实例化点击用户中心
        self.order = MyOrder(self.driver)   #  实例化 点击我的订单
        self.cancel = Cancel(self.driver)   # 实例化 点击取消订单
        self.Re = Repurchase(self.driver)   # 实例化 点击再次购买
        self.num = OrderNumber(self.driver) # 实例化 点击订单号
        self.base = Base(self.driver)   # 实例化Base

    def test_case_01(self):
        self.submit.sto()  # 选择申通快递
        # sleep(2)
        self.submit.tien_gong()    # 选择天工收银支付
        # sleep(2)
        self.submit.place_order()  # 点击提交订单
        # sleep(2)
        self.locator = ('css selector','h6')
        sto = self.submit.is_text_in_element(self.locator,'感谢您在')
        self.assertTrue(sto,msg='用例执行失败')

    def test_case_02(self):
        self.submit.post()     # 选择邮局平邮
        # sleep(2)
        self.submit.scroll_element(('css selector','input[value = "1"]')) # 滚动到指定元素
        # sleep(2)
        self.submit.balance()      # 选择余额支付
        # sleep(2)
        self.submit.place_order()  # 点击提交订单
        # sleep(2)
        self.locator = ('css selector', 'h6')
        post = self.submit.is_text_in_element(self.locator, '感谢您在')
        self.assertTrue(post, msg='用例执行失败')

    def test_case_03(self):
        self.submit.to_pay()   # 选择运费到付
        # sleep(2)
        self.submit.bank()     # 选择银行转账
        # sleep(2)
        self.submit.place_order()  # 点击提交订单
        # sleep(2)
        self.locator = ('css selector', 'h6')
        to_pay = self.submit.is_text_in_element(self.locator, '感谢您在')
        self.assertTrue(to_pay, msg='用例执行失败')

    def test_case_04(self):
        self.submit.sto()     # 选择申通快递
        # sleep(3)
        self.submit.scroll_element(('css selector', 'input[value = "3"]'))
        self.submit.reach()    # 选择货到付款
        # sleep(2)
        self.submit.place_order()  # 点击提交订单
        # sleep(3)
        self.locator = ('css selector', 'h6')
        reach = self.submit.is_text_in_element(self.locator, '感谢您在')
        self.assertTrue(reach, msg='提交订单失败')

    def test_case_05(self):
        '''验证个人中心按钮是否跳转到正确页面'''
        self.submit.place_order()
        self.user.usercenter()  # 验证点击用户中心按钮
        # sleep(2)
        url = self.driver.current_url    # 获取当前页面网址
        self.assertEqual('http://ecshop.itsoso.cn/user.php',url,msg='网址不相同')

    def test_case_06(self):
        '''验证我的订单按钮是否可以正确跳转'''
        self.submit.place_order()
        self.user.usercenter()
        self.order.My_Order()
        url = self.driver.current_url   # 获取当前页面网址
        self.assertEqual('http://ecshop.itsoso.cn/user.php?act=order_list',url,msg='网址不相同')

    def test_case_07(self):
        '''验证取消订单按钮能否正常点击'''
        self.submit.place_order()
        self.user.usercenter()
        self.order.My_Order()
        self.cancel.cancel()
        # sleep(2)
        self.assertTrue(self.cancel.get_alter(),msg='用例执行失败')

    def test_case_08(self):
        '''验证再次购买按钮能否正常点击'''
        self.submit.place_order()
        self.user.usercenter()
        self.order.My_Order()
        self.Re.repurchase()
        sleep(2)    # 等待页面加载
        url = self.driver.current_url   # 获取当前页面网址
        self.assertEqual('http://ecshop.itsoso.cn/flow.php?step=cart&type=5',url)

    def test_case_09(self):
        '''验证点击订单号能否查看到订单详细信息'''
        self.submit.place_order()
        self.user.usercenter()
        self.order.My_Order()
        url1 = self.driver.current_url
        self.num.ordernumber()
        sleep(2)
        url = self.driver.current_url # 获取当前页面网址
        self.assertTrue(url != url1 ,msg='用例执行失败')

    def test_case_10(self):
        '''验证下单是否成功'''
        self.submit.sto()  # 选择申通快递
        self.submit.balance()  # 选择余额支付
        self.submit.place_order()  # 点击提交订单
        sleep(1)
        self.locator = ('css selector','h6>font') # 获取当前页面订单号
        text = self.submit.find_element(self.locator).text
        self.user.usercenter() # 点击用户中心按钮
        self.order.My_Order()   # 点击我的订单
        text1 = self.submit.find_element(('class name','f6')).text # 获取我的订单中第一个订单号
        self.assertEqual(text,text1,msg='订单号不相同')


if __name__ == '__main__':
    unittest.main()




