from page.E_confirm_order_page import ConfirmOrderPage


class MyOrderPage(ConfirmOrderPage):
    """我的订单页面"""

    order_sn_loc = ('id', 'com.tpshop.malls:id/order_sn_tv')  # 订单编号
    to_be_received_loc = ('id','com.tpshop.malls:id/status_receive_tv') # 待收货
    back_loc = ('id','com.tpshop.malls:id/title_back_img') # 返回图标
    confirm_received_loc = ('id','com.tpshop.malls:id/id_index_gallery_item_button') # 确认收货
    positive_button_loc = ('id','com.tpshop.malls:id/positiveButton') # "确定"按钮
    cart_loc = ('id','com.tpshop.malls:id/bottom_cart_img') # 购物车

    def get_order_sn(self):
        """获取订单编号"""
        return self.get_ele_text(self.order_sn_loc)

    def click_to_be_received(self):
        """点击<待收货>"""
        self.click(self.to_be_received_loc)

    def click_confirm_received(self):
        """点击<确认收货>"""
        self.click(self.confirm_received_loc)

    def click_positive_Button(self):
        """点击<确定>"""
        self.click(self.positive_button_loc)

    def click_back(self):
        """点击返回图标"""
        self.click(self.back_loc)

    def click_cart(self):
        """点击购物车"""
        self.click(self.cart_loc)

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
    confirm.click_buy()  # 点击立即购买
    confirm.click_confrim_buy()  # 点击确认购买
    confirm.click_address_RS()  # 点击选择收货地址
    confirm.choose_consignee_RS()  # 选择收货人
    confirm.click_order_balance_RS()  # 点击使用余额
    confirm.wait_page()  # 等待页面加载
    confirm.click_sub_order_RS()  # 点击提交订单
    confirm.input_pay_pwd_RS('123456')  # 输入支付密码
    confirm.click_confirm_pay_pwd_RS()  # 确认支付密码
    order = MyOrderPage(driver)
    sn = order.get_order_sn()  # 获取订单编号
    print(sn)
    sleep(3)
    confirm.quit()
