from page.H_appraisal_center_page import AppraisalCenterPage


class AppraisalShowPage(AppraisalCenterPage):
    """评价晒单页面"""

    comment_content_loc = ('id', 'com.tpshop.malls:id/comment_content_et')  # 评价内容
    anonymous_loc = ('id', 'com.tpshop.malls:id/anonymous_rb')  # 匿名
    submit_comment_loc = ('xpath', '//*[@text="提交"]')  # 提交评价
    comment_classes_loc = ('id', 'com.tpshop.malls:id/star5_btn')  # 商品评价星级

    def input_comment_content(self, text):
        """输入评论内容"""
        self.send_keys(self.comment_content_loc, text)

    def click_anonymous(self):
        """取消匿名"""
        self.click(self.anonymous_loc)

    def click_submit_comment(self):
        """提交评价"""
        self.click(self.submit_comment_loc)

    def click_comment_class(self):
        """点击5星评价"""
        self.iterate_and_click(self.comment_classes_loc)