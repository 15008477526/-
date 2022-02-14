from page.B_main_page import MainPage


class GroupPurchasePage(MainPage):
    """今日团购页面"""

    group_purchase_goods_loc = ('id', 'com.tpshop.malls:id/product_pic_img')  # 所有团购商品

    def click_sony_mobile(self):
        """点击索尼手机"""
        elements = self.find_elements(self.group_purchase_goods_loc)
        elements[0].click()


if __name__ == '__main__':
    from common.base_app import open_app
    from time import sleep

    driver = open_app()  # 打开TPShop,进入登录页面
    gp = GroupPurchasePage(driver)
    gp.input_account_num('13730626896')  # 输入账号
    gp.input_password('123456')  # 输入密码
    gp.wait_page()  # 等待页面加载
    gp.click_confirm_login()  # 点击登录
    gp.wait_page()  # 等待页面加载
    sleep(2)
    gp.click_group_purchase()  # 点击团购
    gp.wait_page()
    gp.click_sony_mobile() # 点击索尼手机
