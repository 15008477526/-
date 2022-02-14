
from page.shopping_cart04 import ShoppingCart
from common.base import open_browser
from page.good_details3 import Buy_Good,good_url
import unittest


class Test_Shopping_Cart(unittest.TestCase):

    def setUp(self):
        # 打开浏览器
        driver=open_browser('chrome')
        # 实例化Buy_Good
        self.good=Buy_Good(driver)
        # 打开网址
        self.good.open_url(good_url)
        self.shopping =ShoppingCart(driver)

    # 用例每次执行后执行
    def tearDown(self):
        self.good.close()

    def is_equal(self,locator1,locator2):
        '''测试商品名称是否 一样'''
        result1 =self.good.get_good_name(locator1)
        self.good.click_libuy() # 点击立即购买
        result2 =self.shopping.get_name(locator2)
        # 断言
        self.assertEqual(result1,result2,msg='不相等哦')


    def add_num(self,number):
        '''增加数量  购物车'''
        self.shopping.send_buy_num(number)
        num1 = str(number)
        print(num1)
        # 点击更新购物车
        self.shopping.update_car()
        # 断言
        num2 =self.shopping.get_num(self.shopping.buy_num_loc)
        print(num2)
        self.assertEqual(num1,num2,msg='不相等 啊啊啊')


    def is_delete(self):
        content =self.shopping.get_price_content(self.shopping.buy_price_loc)
        self.assertEqual('购物金额小计 ￥0.00元，比市场价 ￥0.00元 节省了 ￥0.00元 (0)',content,msg='不相等啊')


    def test_case_02(self):
        self.good.click_libuy()
        self.is_equal(self.good.good_name_loc, self.shopping.good_name_loc)



    # 购物车 增,改
    def test_case_03(self):
        import time
        import random
        #  点击立即购买
        self.good.click_libuy()
        number = random.randint(1,100)
        # 数量输入
        self.add_num(number)
        time.sleep(2)

    # 购物车 确认删除
    def test_case_04(self):
        # 点击立即购买
        self.good.click_libuy()
        # 点击删除按钮
        self.shopping.delete_button()
        # 确认删除
        self.shopping.get_alert_confirm()
        self.is_delete()



if __name__ == '__main__':
    unittest.main(verbosity=2)
    # test = Test_Shopping_Cart()
    # print(test.look_equal(('class name', 'goods_style_name'), ('class name', 'f6')))