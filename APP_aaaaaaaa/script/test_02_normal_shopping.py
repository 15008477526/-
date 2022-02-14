import pytest
from common.base_app import open_app
from page.H_appraisal_center_page import PersonalCenterPage
from time import sleep

app_account = '13730626896'  # app端账号
app_password = '123456'  # app端密码


class TestNormalShopping(object):
    """普通商品购买测试类"""

    def setup_class(self):
        app_driver = open_app()  # 打开TPShop App
        self.ns_app = PersonalCenterPage(app_driver)  # 实例化MyOrderPage

    def teardown_class(self):
        self.ns_app.quit()  # 关闭app

    def test_normal_shopping(self):
        """购买普通商品测试用例"""
        # self.ns_app.input_account_num(app_account)  # 输入账号
        # self.ns_app.input_password(app_password)  # 输入密码
        # self.ns_app.click_confirm_login()  # 点击登录
        self.ns_app.wait_page()  # 等待页面加载
        self.ns_app.click_search()  # 点击搜索框
        self.ns_app.input_search_content('航空母舰')  # 搜索商品
        self.ns_app.click_search_button()  # 点击搜索按钮
        self.ns_app.wait_page()  # 等待页面加载
        sleep(1)
        self.ns_app.click_search_good()  # 点击容声冰箱
        self.ns_app.wait_page()  # 等待页面加载
        sleep(1)
        self.ns_app.click_buy()  # 点击立即购买
        self.ns_app.click_confrim_buy()  # 点击确认购买
        self.ns_app.wait_page()  # 等待页面加载
        sleep(5)
        self.ns_app.click_address_RS()  # 点击选择收货地址
        self.ns_app.wait_page()  # 等待页面加载
        self.ns_app.choose_consignee_RS()  # 选择收货人
        self.ns_app.wait_page()  # 等待页面加载
        sleep(1)
        order_balance = float(self.ns_app.get_order_balance())  # 获取订单页面的当前余额
        print(order_balance)
        self.ns_app.click_order_balance_RS()  # 点击使用余额
        self.ns_app.wait_page()  # 等待页面加载
        sleep(1)
        tmp = self.ns_app.get_balance_fee()  # 获取支付的余额
        balance_fee = float(tmp.lstrip('¥'))
        print(balance_fee)
        self.ns_app.click_sub_order_RS()  # 点击提交订单
        self.ns_app.input_pay_pwd_RS('123456')  # 输入支付密码
        self.ns_app.click_confirm_pay_pwd_RS()  # 确认支付密码
        self.ns_app.wait_page()
        sleep(3)
        self.ns_app.click_back()  # 点击返回,回到商品详情
        sleep(1)
        self.ns_app.click_cart()  # 点击购物车
        self.ns_app.wait_page()  # 等待页面加载
        self.ns_app.click_mine()  # 点击"我的"
        self.ns_app.wait_page()
        sleep(1)
        mine_balance = float(self.ns_app.get_mine_balance())  # 获取我的--余额
        print(mine_balance)
        assert round(order_balance) - round(balance_fee) == round(mine_balance)

        # sleep(2)
        # sn = self.ns_app.get_order_sn()  # 获取订单编号
        # print(sn)
        # """web端部分"""
        # web_driver = open_browser()  # 打开谷歌浏览器
        # ns_web = BgMainPage(web_driver)  # 实例化BgManiPage
        # ns_web.login_by_cookie()  # 绕过验证码登录后台,进入后台主页
        # ns_web.click_bg_mall()  # 点击商城
        # ns_web.click_bg_order()  # 点击订单
        # ns_web.click_bg_delivery_order()  # 点击发货单
        # ns_web.switch_to_frame('workspace')  # 进入workspace frame
        # ns_web.input_bg_order_sn(sn)  # 输入订单编号
        # ns_web.click_bg_order_search()  # 点击搜索
        # ns_web.click_bg_to_delivery()  # 点击去发货
        # bg_mobile = ns_web.get_bg_delivery_order_mobile()  # 获取发货订单的手机号
        # assert bg_mobile == app_account  # 断言:后台订单的手机号 = 登录手机号
        # ns_web.quit() # 退出浏览器


if __name__ == '__main__':
    pytest.main(['-s', 'test_02_normal_shopping.py'])
