'''
商品浏览
'''

from common.base import Base
from time import sleep
url = "http://ecshop.itsoso.cn/"

class Goodslist_Page(Base):
    """封装表现层:制作定位器"""
    # 首页元素的定位
    first_page_loc = ("link text", "首页")
    send_loc = ("name", "keywords")
    search_loc = ("value", "搜索")


    def click_first(self):
        """点击首页"""
        self.click(self.first_page_loc)

    def get_goods_text(self, locator):
        """获取商品文本"""
        goods_elements = self.find_elements(locator)
        texts = []
        for goods_element in goods_elements:
            text = goods_element.text  # 获取单个商品的文本
            texts.append(text)
        return texts

    def click_texts(self, locator1,locator2):
        """

        :param locator1: 商品类的元素定位器
        :param locator2: 商品列表的定位器
        :return:
        """
        # 取出商品类的所有文本
        texts = self.get_goods_text(locator1)
        for text in texts:
            good_loc = ("link text", text)
            self.click(good_loc)
            self.click_all_element(locator2)

    def get_goods_title(self, locator):
        """获取商品标题"""
        goods_elements = self.find_elements(locator)
        # 获取商品标题
        titles = []  # 准备一个列表装商品标题
        for goods_element in goods_elements:
            # title就是表示元素的属性值
            title = goods_element.get_attribute("title")
            titles.append(title)
        return titles

    def click_all_element(self, locator):
        """点击所有元素"""
        titles = self.get_goods_title(locator)
        for title in titles:
            # 重新制作单个商品的定位器
            goods_loc = ("css selector", f"a[title='{title}']")
            self.click(goods_loc)
            self.back()
        self.next_page()

    def next_page(self):
        # 下一页的定位器
        next_loc = ("link text", "下一页")
        # 点击下一页
        # 判断有没有下一页的元素,有就点击元素,没有就返回首页
        while True:
            if self.displayed(next_loc):
                self.click(next_loc)
            else:
                self.click(self.first_page_loc)
                break


    def input_goods(self,text):
        """输入搜索商品名"""
        self.send_keys(self.send_loc,text)

    def click_search(self):
        """点击搜索按钮"""
        self.click(self.search_loc)

if __name__ == '__main__':
    from common.base import open_browser

    driver = open_browser()
    goods = Goodslist_Page(driver)  # 实例化login page
    goods.open_url(url)  # 打开网址
    goods.click_first()  # 点击首页
    categary_loc = ("css selector", "div.cat-box>div.cat1>a")  # 商品类的定位器
    goods_loc = ("css selector", "div.goods-title>a")  # 商品列表的定位器
    goods.click_texts(categary_loc, goods_loc)  # 点击商品类
