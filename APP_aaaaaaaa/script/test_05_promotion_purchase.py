import pytest
from common.base_app import open_app
from page.H_appraisal_center_page import PersonalCenterPage
from time import sleep

app_account = '13730626896'  # app端账号
app_password = '123456'  # app端密码


class TestPromotionPurchase(object):
    """促销商品购买测试类"""

    def setup_class(self):
        app_driver = open_app()  # 打开TPShop App
        self.pp_app = PersonalCenterPage(app_driver)  # 实例化MyOrderPage

    def teardown_class(self):
        self.pp_app.quit()  # 关闭app

    def test_promotion_purchase(self):
        """促销商品购买测试用例"""
        # self.pp_app.input_account_num(app_account)  # 输入账号
        # self.pp_app.input_password(app_password)  # 输入密码
        # self.pp_app.click_confirm_login()  # 点击登录
        self.pp_app.wait_page()  # 等待页面加载
        sleep(1)
        self.pp_app.click_promotion()  # 点击促销商品
        self.pp_app.wait_page()  # 等待页面加载
        sleep(1)
        self.pp_app.click_pomelo()  # 点击Pomelo
        self.pp_app.wait_page()  # 等待页面加载
        sleep(2)
        self.pp_app.click_buy()  # 点击立即购买
        self.pp_app.click_confrim_buy()  # 点击确认购买
        self.pp_app.wait_page()  # 等待页面加载
        sleep(5)
        self.pp_app.click_address_RS()  # 点击选择收货地址
        self.pp_app.wait_page()  # 等待页面加载
        self.pp_app.choose_consignee_RS()  # 选择收货人
        self.pp_app.wait_page()  # 等待页面加载
        sleep(1)
        order_balance = float(self.pp_app.get_order_balance())  # 获取订单页面的当前余额
        print(order_balance)
        self.pp_app.click_order_balance_RS()  # 点击使用余额
        self.pp_app.wait_page()  # 等待页面加载
        sleep(1)
        tmp = self.pp_app.get_balance_fee()  # 获取支付的余额
        balance_fee = float(tmp.lstrip('¥'))
        print(balance_fee)
        self.pp_app.click_sub_order_RS()  # 点击提交订单
        self.pp_app.input_pay_pwd_RS('123456')  # 输入支付密码
        self.pp_app.click_confirm_pay_pwd_RS()  # 确认支付密码
        self.pp_app.wait_page()
        sleep(3)
        self.pp_app.click_back()  # 点击返回,回到商品详情
        sleep(1)
        self.pp_app.click_cart()  # 点击购物车
        self.pp_app.wait_page()  # 等待页面加载
        self.pp_app.click_mine()  # 点击"我的"
        self.pp_app.wait_page()
        sleep(1)
        mine_balance = float(self.pp_app.get_mine_balance())  # 获取我的--余额
        print(mine_balance)
        assert round(order_balance) - round(balance_fee) == round(mine_balance)


if __name__ == '__main__':
    pytest.main(['-s', 'test_05_promotion_purchase.py'])