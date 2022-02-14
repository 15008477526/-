'''
浏览所有商品
'''
import unittest
from common.base import open_browser
from page.goods_list_page import Goodslist_Page,url


class TestGoodsList(unittest.TestCase):
    '''测试浏览所有商品'''
    def test_case_01(self):

        driver = open_browser()
        goods = Goodslist_Page(driver)  # 实例化login page
        goods.open_url(url)  # 打开网址
        goods.click_first()  # 点击首页
        categary_loc = ("css selector", "div.cat-box>div.cat1>a")  # 商品类的定位器
        goods_loc = ("css selector", "div.goods-title>a")  # 商品列表的定位器
        goods.click_texts(categary_loc, goods_loc)  # 点击商品类