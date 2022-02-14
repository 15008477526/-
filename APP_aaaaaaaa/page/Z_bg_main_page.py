from common.base_web import BaseWeb


class BgMainPage(BaseWeb):
    """后台主页面"""

    bg_mall_loc = ('link text', '商城')  # 后台商城
    bg_order_loc = ('link text', '订单')  # 后台订单
    bg_delivery_order_loc = ('css selector', 'a[data-param="delivery_list|Order"]')  # 后台发货单
    bg_order_sn_loc = ('id', 'order_sn')  # 订单编号
    bg_order_search_loc = ('css selector', 'input[value="搜索"]')  # 搜索按钮
    bg_to_delivery_loc = ('link text', '去发货')  # 去发货
    bg_delivery_order_mobile_loc = ('xpath', '//div[@class="addr-note"]/dl[4]/dd')  # 发货订单的手机号
    bg_shipping_companies_loc = ('css selector', '#shipping_code>option')  # 物流公司
    bg_shipping_order_loc = ('css selector', '#invoice_no"]')  # 物流单号  ???
    bg_send_type_loc = ('css selector', '#send_type>option')  # 发货方式
    bg_confirm_delivery_loc = ('class name', 'ncap-btn-send')  # 确认发货
    bg_goods_button_loc = ('link text', '商品')  # 商品按钮
    bg_comment_list_loc = ('css selector', 'a[data-param="index|Comment"]')  # 评论列表
    bg_search_user_loc = ('css selector', 'input[placeholder="搜索用户"]')  # 搜索用户输入框
    bg_comment_search_loc = ('css selector', 'input[value="搜索"]')  # 评论搜索
    bg_comment_content_loc = ('css selector', '#flexigrid>table>tbody>tr>td:nth-of-type(3)>div')  # 评论内容

    def click_bg_mall(self):
        """点击后台<商城>"""
        self.click(self.bg_mall_loc)

    def click_bg_order(self):
        """点击后台<订单>"""
        self.click(self.bg_order_loc)

    def click_bg_delivery_order(self):
        """点击后台<发货单>"""
        self.click(self.bg_delivery_order_loc)

    def input_bg_order_sn(self, sn):
        """输入订单编号"""
        self.send_keys(self.bg_order_sn_loc, sn)

    def click_bg_order_search(self):
        """点击搜索订单按钮"""
        self.click(self.bg_order_search_loc)

    def click_bg_to_delivery(self):
        """点击去发货"""
        self.click(self.bg_to_delivery_loc)

    def get_bg_delivery_order_mobile(self):
        """获取订单的手机号"""
        return self.get_element_text(self.bg_delivery_order_mobile_loc)

    def select_bg_shipping_company(self):
        """随机选择一个物流公司"""
        self.select_by_num(self.bg_shipping_companies_loc)

    def input_bg_shipping_order(self, num):
        """随机输入一个运单号"""
        self.send_keys(self.bg_shipping_order_loc, num)

    def select_bg_send_type(self):
        """选择发货方式--无需物流"""
        self.select_by_num(self.bg_send_type_loc)

    def click_bg_confirm_delivery(self):
        """点击<确认发货>"""
        self.click(self.bg_confirm_delivery_loc)

    def click_bg_goods_button(self):
        """点击商品按钮"""
        self.click(self.bg_goods_button_loc)

    def click_bg_comment_list(self):
        """点击<评论列表>"""
        self.click(self.bg_comment_list_loc)

    def input_bg_search_user(self, user):
        """输入搜索的用户名"""
        self.send_keys(self.bg_search_user_loc, user)

    def click_bg_comment_search(self):
        """点击评论搜索按钮"""
        self.click(self.bg_comment_search_loc)

    def get_bg_comment_content(self):
        return self.get_element_text(self.bg_comment_content_loc)

if __name__ == '__main__':
    from common.base_web import open_browser
    from common.random_data import RandomData

    driver = open_browser()  # 实例化浏览器
    rd = RandomData()  # 实例化随机类
    bg = BgMainPage(driver)  # 实例化BgMainPage
    bg.login_by_cookie()  # 绕过验证码登录后台,进入后台主页
    bg.click_bg_mall()  # 点击商城
    """part1"""
    # bg.click_bg_order()  # 点击订单
    # bg.click_bg_delivery_order()  # 点击发货单
    # bg.switch_to_frame('workspace')  # 进入workspace frame
    # bg.input_bg_order_sn('201910101938283929')  # 输入订单编号
    # bg.click_bg_order_search()  # 点击搜索
    # bg.click_bg_to_delivery()  # 点击去发货
    # bg.select_bg_send_type()  # 选择"无需物流发货"
    # bg.click_bg_confirm_delivery()  # 点击确认发货
    # bg.switch_to_parent_frame() # 跳出当前frame
    # bg.click_bg_goods_button() # 点击商品按钮
    """part2"""
    bg.click_bg_comment_list()  # 点击评论列表
    bg.switch_to_frame('workspace')  # 进入workspace frame
    bg.input_bg_search_user('jumon666')  # 输入搜索的用户名
    bg.click_bg_comment_search()  # 点击搜索评论
    bg_content = bg.get_bg_comment_content() # 获取后台的订单评论内容
    print(bg_content)