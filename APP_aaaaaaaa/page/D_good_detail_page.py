from page.C_1_search_page import SearchPage  # 普通商品搜索页面
from page.C_2_group_purchase_page import GroupPurchasePage  # 团购商品页面
from page.C_3_promotion_page import PromotionPage # 促销商品页面
from page.C_4_points_reward_page import PointsRewardPage # 积分商城页面


class GoodDetailPage(SearchPage, GroupPurchasePage, PromotionPage,PointsRewardPage):
    """商品详情页面"""

    buy_loc = ('id', 'com.tpshop.malls:id/promptly_buy_tv')  # 立即购买
    confirm_buy_RS_loc = ('id', 'com.tpshop.malls:id/confirm_tv')  # 确认购买
    exchange_loc = ('id','com.tpshop.malls:id/buy_cart_tv') # 立即兑换(积分商品)
    good_detail_back_loc = ('id','com.tpshop.malls:id/back_ll') # 返回

    def click_buy(self):
        """点击<立即购买>"""
        self.click(self.buy_loc)

    def click_confrim_buy(self):
        """点击<确认购买>"""
        self.click(self.confirm_buy_RS_loc)

    def click_exchange(self):
        """点击<立即兑换>"""
        self.click(self.exchange_loc)

    def click_good_detail_back(self):
        """点击返回"""
        self.click(self.good_detail_back_loc)

if __name__ == '__main__':
    from common.base_app import open_app
    from time import sleep

    driver = open_app()  # 打开TPShop,进入登录页面
    RS = GoodDetailPage(driver)
    RS.input_account_num('13730626896')  # 输入账号
    RS.input_password('123456')  # 输入密码
    RS.wait_page()  # 等待页面加载
    RS.click_confirm_login()  # 点击登录
    RS.wait_page()  # 等待页面加载
    sleep(2)
    """普通商品"""
    # RS.click_search()  # 点击搜索框
    # RS.input_search_content('容声冰箱')  # 搜索容声冰箱
    # RS.click_search_button()  # 点击搜索按钮
    # RS.click_RSfridge()  # 点击容声冰箱
    """团购商品"""
    # RS.click_group_purchase()  # 点击团购
    # RS.wait_page()  # 等待页面加载
    # sleep(1)
    # RS.click_sony_mobile()  # 点击索尼手机
    """促销商品"""
    # RS.click_promotion() # 点击促销商品
    # RS.wait_page() # 等待页面加载
    # sleep(1)
    # RS.click_pomelo() # 点击Pomelo
    """积分商品"""
    RS.click_points_reward() # 点击积分商城
    RS.wait_page() # 等待页面加载
    sleep(1)
    RS.click_point_good() # 随机选择一个积分商品进行购买
    RS.wait_page()  # 等待页面加载
    sleep(2)
    RS.click_exchange() # 点击立即兑换


    
    # RS.click_buy()  # 点击立即购买
    RS.click_confrim_buy()  # 点击确认购买
    sleep(3)
    RS.quit()
