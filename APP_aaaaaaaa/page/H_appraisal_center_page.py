from page.G_personal_center_page import PersonalCenterPage


class AppraisalCenterPage(PersonalCenterPage):
    """评价中心页面"""

    appraisal_show_loc = ('id', 'com.tpshop.malls:id/order_show_btn')  # 评价晒单链接

    def click_appraisal_show_link(self):
        """点击评价晒单"""
        self.click(self.appraisal_show_loc)
