from page.B_main_page import MainPage


class PointsRewardPage(MainPage):
    """积分商城页面"""

    points_goods_loc = ('id','com.tpshop.malls:id/integral_buy_btn') # 所有立即购买元素

    def click_point_good(self):
        """随机点击一个积分商品进行购买"""
        self.random_click(self.points_goods_loc)
