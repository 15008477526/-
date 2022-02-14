from page.D_good_detail_page import GoodDetailPage


class ConfirmOrderPage(GoodDetailPage):
    """确认订单--容声冰箱"""

    select_address_RS_loc = ('id', 'com.tpshop.malls:id/order_address_tv')  # 选择收货地址
    consignee_RS_loc = ('id', 'com.tpshop.malls:id/address_consignee_tv')  # 收货人地址第一个
    use_order_balance_loc = ('id', 'com.tpshop.malls:id/order_balance_sth')  # 使用余额
    sub_order_RS_loc = ('id', 'com.tpshop.malls:id/submit_tv')  # 提交订单
    pay_pwd_RS_loc = ('id', 'com.tpshop.malls:id/pwd_et')  # 支付密码
    confirm_pay_pwd_RS_loc = ('id', 'com.tpshop.malls:id/sure_tv')  # 确认支付密码
    order_balance_loc = ('id', 'com.tpshop.malls:id/order_balance_tv')  # 余额
    balance_fee_loc = ('id', 'com.tpshop.malls:id/balance_fee_tv')  # 支付的余额
    points_fee_loc = ('id','com.tpshop.malls:id/has_point_tv') # 使用的积分

    def click_address_RS(self):
        """点击选择收货地址"""
        self.click(self.select_address_RS_loc)

    def choose_consignee_RS(self):
        """选择收货人"""
        self.click(self.consignee_RS_loc)

    def click_order_balance_RS(self):
        """点击使用余额"""
        self.click(self.use_order_balance_loc)

    def click_sub_order_RS(self):
        """点击提交订单"""
        self.click(self.sub_order_RS_loc)

    def input_pay_pwd_RS(self, text):
        """输入支付密码"""
        self.send_keys(self.pay_pwd_RS_loc, text)

    def click_confirm_pay_pwd_RS(self):
        """确认支付密码"""
        self.click(self.confirm_pay_pwd_RS_loc)

    def get_order_balance(self):
        """获取订单显示的当前余额"""
        return self.get_ele_text(self.order_balance_loc)

    def get_balance_fee(self):
        """获取支付的余额"""
        return self.get_ele_text(self.balance_fee_loc)

    def get_points_fee(self):
        """获取使用的积分"""
        return self.get_ele_text(self.points_fee_loc)

if __name__ == '__main__':
    from common.base_app import open_app
    from time import sleep

    driver = open_app()  # 打开TPShop,进入登录页面
    confirm = ConfirmOrderPage(driver)
    confirm.input_account_num('13730626896')  # 输入账号
    confirm.input_password('123456')  # 输入密码
    confirm.click_confirm_login()  # 点击登录
    confirm.wait_page()  # 等待页面加载
    confirm.click_search()  # 点击搜索框
    confirm.input_search_content('容声冰箱')  # 搜索容声冰箱
    confirm.click_search_button()  # 点击搜索按钮
    confirm.wait_page()  # 等待页面加载
    sleep(2)
    confirm.click_RSfridge()  # 点击容声冰箱
    confirm.wait_page()  # 等待页面加载
    sleep(3)
    confirm.click_buy_RS()  # 点击立即购买
    confirm.click_confrim_buy_RS()  # 点击确认购买
    confirm.click_address_RS()  # 点击选择收货地址
    confirm.choose_consignee_RS()  # 选择收货人
    confirm.click_order_balance_RS()  # 点击使用余额
    confirm.wait_page()  # 等待页面加载
    confirm.click_sub_order_RS()  # 点击提交订单
    confirm.input_pay_pwd_RS('123456')  # 输入支付密码
    confirm.click_confirm_pay_pwd_RS()  # 确认支付密码
    sleep(3)
    confirm.quit()
