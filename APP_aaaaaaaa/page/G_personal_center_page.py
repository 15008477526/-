from page.F_my_order import MyOrderPage


class PersonalCenterPage(MyOrderPage):
    """个人中心页面"""

    to_appraisal_loc = ('xpath', '//*[@text="待评价"]')
    mine_balance_loc = ('id', 'com.tpshop.malls:id/balance_tv')  # 我的--余额
    mine_points_loc = ('id', 'com.tpshop.malls:id/point_tv')  # 我的--积分

    def click_to_appraisal(self):
        """点击待评价"""
        self.click(self.to_appraisal_loc)

    def get_mine_balance(self):
        """获取我的--余额"""
        return self.get_ele_text(self.mine_balance_loc)

    def get_mine_ponits(self):
        """获取我的--积分"""
        return self.get_ele_text(self.mine_points_loc)
