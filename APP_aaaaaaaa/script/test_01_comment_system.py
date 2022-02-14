import pytest
from common.base_web import open_browser
from page.Z_bg_main_page import BgMainPage
from common.base_app import open_app
from page.I_appraisal_show_page import AppraisalShowPage
from time import sleep
from common.random_data import RandomData

app_account = '13730626896'  # app端账号
app_password = '123456'  # app端密码


class TestCommentSystem(object):
    """商品评论测试类"""

    def setup_class(self):
        app_driver = open_app()  # 打开TPShop App
        self.as_app = AppraisalShowPage(app_driver)  # 实例化MyOrderPage
        self.rd = RandomData()

    def teardown_class(self):
        self.as_app.quit()  # 关闭app

    def test_appraisal_system(self):
        """商品评论测试用例"""
        """移动端--购买商品"""
        # self.as_app.input_account_num(app_account)  # 输入账号
        # self.as_app.input_password(app_password)  # 输入密码
        # self.as_app.click_confirm_login()  # 点击登录
        self.as_app.wait_page()  # 等待页面加载
        self.as_app.click_search()  # 点击搜索框
        self.as_app.input_search_content('二锅头')  # 搜索商品
        self.as_app.click_search_button()  # 点击搜索按钮
        self.as_app.wait_page()  # 等待页面加载
        sleep(1)
        self.as_app.click_search_good()  # 点击搜索到的商品
        self.as_app.wait_page()  # 等待页面加载
        sleep(2)
        self.as_app.click_buy()  # 点击立即购买
        self.as_app.click_confrim_buy()  # 点击确认购买
        self.as_app.wait_page()  # 等待页面加载
        sleep(5)
        self.as_app.click_address_RS()  # 点击选择收货地址
        self.as_app.wait_page()  # 等待页面加载
        self.as_app.choose_consignee_RS()  # 选择收货人
        self.as_app.wait_page()  # 等待页面加载
        self.as_app.click_order_balance_RS()  # 点击使用余额
        self.as_app.wait_page()  # 等待页面加载
        self.as_app.click_sub_order_RS()  # 点击提交订单
        self.as_app.input_pay_pwd_RS('123456')  # 输入支付密码
        self.as_app.click_confirm_pay_pwd_RS()  # 确认支付密码
        self.as_app.wait_page()
        sleep(2)
        sn = self.as_app.get_order_sn()  # 获取订单编号

        """web后台--发货"""
        web_driver = open_browser()  # 打开谷歌浏览器
        as_web = BgMainPage(web_driver)  # 实例化BgManiPage
        as_web.login_by_cookie()  # 绕过验证码登录后台,进入后台主页
        as_web.click_bg_mall()  # 点击商城
        as_web.click_bg_order()  # 点击订单
        as_web.click_bg_delivery_order()  # 点击发货单
        as_web.switch_to_frame('workspace')  # 进入workspace frame
        as_web.input_bg_order_sn(sn)  # 输入订单编号
        as_web.click_bg_order_search()  # 点击搜索
        as_web.click_bg_to_delivery()  # 点击去发货
        as_web.select_bg_send_type()  # 选择"无需物流发货"
        as_web.click_bg_confirm_delivery()  # 点击"确认"发货
        as_web.switch_to_parent_frame()  # 跳出当前frame
        as_web.click_bg_goods_button()  # 点击"商品"按钮

        """移动端--商品评价"""
        sleep(5)
        self.as_app.click_to_be_received()  # 点击"待收货"
        self.as_app.wait_page()  # 等待页面加载
        self.as_app.click_confirm_received()  # 点击"确认收货"
        self.as_app.click_positive_Button()  # 点击"确定"
        self.as_app.wait_page()
        sleep(3)
        self.as_app.click_back()  # 返回,回到商品详情
        sleep(1)
        self.as_app.click_cart()  # 点击购物车
        self.as_app.wait_page()  # 等待页面加载
        self.as_app.click_mine()  # 点击"我的"
        self.as_app.click_to_appraisal()  # 点击待评价
        self.as_app.wait_page()  # 等待页面加载
        sleep(1)
        self.as_app.click_appraisal_show_link()  # 点击最新的已完成订单去评价
        self.as_app.wait_page()  # 等待页面加载
        content = self.rd.random_sentence()  # 随机输入一句话作为评论内容
        self.as_app.input_comment_content(content)
        self.as_app.click_anonymous() # 取消匿名
        self.as_app.click_comment_class() # 点击评价星级
        self.as_app.click_submit_comment()  # 提交评论
        sleep(2)

        """web后台--获取后台评价内容"""
        as_web.click_bg_comment_list()  # 点击评论列表
        as_web.switch_to_frame('workspace')  # 进入workspace frame
        as_web.input_bg_search_user('jumon666')  # 输入搜索的用户名
        as_web.click_bg_comment_search()  # 点击搜索评论
        bg_content = as_web.get_bg_comment_content()  # 获取后台的订单评论内容
        assert content == bg_content  # 断言:同一订单的前后台评论内容一致
        sleep(2)
        as_web.quit()


if __name__ == '__main__':
    pytest.main(['-s', 'test_01_comment_system.py'])
