"""@author:郁华夏"""

from page.A_login_page import LoginPage


class MainPage(LoginPage):
    """首页"""
    main_loc = ('id', 'com.tpshop.malls:id/home_tv')  # 首页
    mine_loc = ('id', 'com.tpshop.malls:id/mine_tv')  # 我的
    search_loc = ('id', 'com.tpshop.malls:id/default_search_et')  # 搜索
    group_purchase_loc = ('xpath', '//*[@text="团购"]')  # 团购
    promotion_loc = ('xpath', '//*[@text="商品促销"]')  # 商品促销
    points_reward_loc = ('xpath', '//*[@text="积分商城"]')  # 积分商城
    group_booking_loc = ('xpath', '//*[@text="我要拼团"]')  # 我要拼团

    def click_main(self):
        """点击<首页>"""
        self.click(self.main_loc)

    def click_mine(self):
        """点击<我的>"""
        self.click(self.mine_loc)

    def click_search(self):
        """点击搜索框,进入搜索页面"""
        self.click(self.search_loc)

    def click_group_purchase(self):
        """点击<团购>"""
        self.click(self.group_purchase_loc)

    def click_promotion(self):
        """点击<商品促销>"""
        self.click(self.promotion_loc)

    def click_points_reward(self):
        """点击<积分商城>"""
        self.click(self.points_reward_loc)

    def click_group_booking(self):
        """点击<我要拼团>"""
        self.click(self.group_booking_loc)


if __name__ == '__main__':
    from common.base_app import open_app
    from time import sleep

    driver = open_app()  # 打开TPShop,进入登录页面
    main = MainPage(driver)
    main.input_account_num('13730626896')  # 输入账号
    main.input_password('123456')  # 输入密码
    main.wait_page()  # 等待页面加载
    main.click_confirm_login()  # 点击登录
    main.click_search()  # 点击搜索框
    sleep(2)
    main.quit()
