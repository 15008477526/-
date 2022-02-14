import pytest
from common.base_app import open_app
from page.H_appraisal_center_page import PersonalCenterPage
from time import sleep

app_account = '13730626896'  # app端账号
app_password = '123456'  # app端密码


class TestPointsReward(object):
    """积分商品购买测试类"""

    def setup_class(self):
        app_driver = open_app()  # 打开TPShop App
        self.pr_app = PersonalCenterPage(app_driver)  # 实例化MyOrderPage

    def teardown_class(self):
        self.pr_app.quit()  # 关闭app

    def test_points_reward(self):
        """积分商品购买测试用例"""
        # self.pr_app.input_account_num(app_account)  # 输入账号
        # self.pr_app.input_password(app_password)  # 输入密码
        # self.pr_app.click_confirm_login()  # 点击登录
        # self.pr_app.wait_page()  # 等待页面加载
        # sleep(1)
        self.pr_app.click_mine()  # 点击"我的"
        ori_balance = float(self.pr_app.get_mine_balance())  # 获取初始余额
        ori_points = float(self.pr_app.get_mine_ponits())  # 获取初始积分
        print(ori_balance)
        print(ori_points)
        self.pr_app.click_main()  # 点击首页
        self.pr_app.wait_page()  # 等待页面加载
        sleep(1)
        self.pr_app.click_points_reward()  # 点击积分商城
        self.pr_app.wait_page()  # 等待页面加载
        sleep(1)
        self.pr_app.click_point_good()  # 随机选择一个积分商品进行购买
        self.pr_app.wait_page()  # 等待页面加载
        sleep(2)
        self.pr_app.click_exchange()  # 点击立即兑换
        self.pr_app.click_confrim_buy()  # 点击确认
        self.pr_app.wait_page()  # 等待页面加载
        sleep(5)
        self.pr_app.click_address_RS()  # 点击选择收货地址
        self.pr_app.wait_page()  # 等待页面加载
        self.pr_app.choose_consignee_RS()  # 选择收货人
        self.pr_app.wait_page()  # 等待页面加载
        sleep(1)
        # order_balance = self.pr_app.get_order_balance()  # 获取订单页面的当前余额
        # print(order_balance)
        self.pr_app.click_order_balance_RS()  # 点击使用余额
        self.pr_app.wait_page()  # 等待页面加载
        sleep(1)
        tmp = self.pr_app.get_balance_fee()  # 获取支付的余额
        balance_fee = float(tmp.lstrip('¥'))
        points_fee = float(self.pr_app.get_points_fee())  # 获取使用的积分
        print(balance_fee)
        self.pr_app.click_sub_order_RS()  # 点击提交订单
        self.pr_app.input_pay_pwd_RS('123456')  # 输入支付密码
        self.pr_app.click_confirm_pay_pwd_RS()  # 确认支付密码
        self.pr_app.wait_page()
        sleep(3)
        self.pr_app.click_back()  # 点击返回,回到商品详情
        sleep(1)
        self.pr_app.click_cart()  # 点击购物车
        self.pr_app.wait_page()  # 等待页面加载
        self.pr_app.click_mine()  # 点击"我的"
        self.pr_app.wait_page()
        sleep(1)
        mine_balance = float(self.pr_app.get_mine_balance())  # 获取支付后的余额
        mine_points = float(self.pr_app.get_mine_ponits())  # 获取支付后的积分
        print(mine_balance)
        assert round(ori_balance) - round(balance_fee) == round(mine_balance) and ori_points - points_fee == mine_points


if __name__ == '__main__':
    pytest.main(['-s', 'test_03_points_reward.py'])
