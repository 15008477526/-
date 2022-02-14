from page.B_main_page import MainPage


class SearchPage(MainPage):
    """搜索页面"""

    search_content_loc = ('id', 'com.tpshop.malls:id/search_et')  # 搜索内容
    search_button_loc = ('id', 'com.tpshop.malls:id/search_btn')  # 搜索按钮
    search_good_loc = ('id', 'com.tpshop.malls:id/product_pic_img')  # 搜索到的商品
    serach_back_loc = ('id','com.tpshop.malls:id/title_back_img') # 点击返回

    def input_search_content(self, text):
        """输入搜索内容"""
        self.send_keys(self.search_content_loc, text)

    def click_search_button(self):
        """点击搜索按钮"""
        self.click(self.search_button_loc)

    def click_search_good(self):
        """点击搜索到的商品"""
        self.click(self.search_good_loc)

    def click_search_back(self):
        """点击返回"""
        self.click_search_back()

if __name__ == '__main__':
    from common.base_app import open_app
    from time import sleep

    driver = open_app()  # 打开TPShop,进入登录页面
    search = SearchPage(driver)
    search.input_account_num('13730626896')  # 输入账号
    search.input_password('123456')  # 输入密码
    search.wait_page()  # 等待页面加载
    search.click_confirm_login()  # 点击登录
    search.wait_page()  # 等待页面加载
    search.click_search()  # 点击搜索框
    search.input_search_content('容声冰箱')  # 搜索容声冰箱
    search.click_search_button()  # 点击搜索按钮
    sleep(1)
    search.click_RSfridge()  # 点击容声冰箱
    sleep(1)
    search.quit()
