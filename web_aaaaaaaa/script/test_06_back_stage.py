'''
@author : 魏江霖
测试后台商品添加   货号比较

'''
from common.random_faker import randomData
from page.back_stage import Back_Stage
from common.base import open_browser
from page.good_details3 import Buy_Good
import unittest

class Test_Back_Stage(unittest.TestCase):
    '''测试后台商品添加'''
    def setUp(self):
        # 打开浏览器
        self.driver=open_browser('chrome')
        self.bs = Back_Stage(self.driver)
        self.libuy = Buy_Good(self.driver)
        self.bs.open_url('http://ecshop.itsoso.cn/admin/index.php')
        username_loc = ('name', 'username')
        username = self.bs.find_element(username_loc)
        username.send_keys('admin')
        password_loc = ('name', 'password')
        password = self.bs.find_element(password_loc)
        password.send_keys('admin123')
        submit_loc = ('css selector', 'input[value="登 录"]')
        submit = self.bs.find_element(submit_loc)
        submit.click()


    def test_case_1(self):

        import time
        import random

        lists = randomData()
        num = random.randint(1,20)
        name =lists[0]

        self.bs.switch_to_frame('menu-frame')
        # 点击商品管理
        self.bs.click_shop_manager()
        # 点击添加新商品
        self.bs.click_add_shop()
        self.bs.quit_patent_frame()
        # 在进入iframe
        self.bs.switch_to_frame("main-frame")

        # 添加商品名称
        self.bs.click_good_name(name)
        # 字体样式选择
        self.bs.select_sort()
        # 商品分类
        self.bs.select_good()
        # 商品品牌选择
        self.bs.select_brand()
        # 本店售价
        self.bs.send_sell_price(num)
        # 点击商品上传 输入框
        self.bs.send_put_on_picture('http://image.namedq.com/uploads/20181219/23/1545233909-MDtFANczwO.jpg')
        #
        #         # 点详细描述
        self.bs.click_detail_des()

        self.bs.send_msg('这是娑娜')
        self.bs.click_other_msg()
        self.bs.send_good_weight(2)
        # 复选框 加入推荐
        self.bs.choice_box()

        # 上架勾选
        self.bs.click_put_on()

        # 普通商品销售
        self.bs.click_sale()
        # 免运费商品
        self.bs.click_freight()
        # 点击商品属性
        self.bs.click_attribute()

        # 商品类型勾选
        self.bs.select_type()

        #点击商品相册
        self.bs.click_picture()
        #
        # # 点击图片描述
        # self.bs.click_pic_des('云顶之弈')
        # 选择文件按钮
        # self.bs.click_shangchuan()

        # 点击外部链接
        self.bs.click_url('www.baidu.com')

        # 确定按钮
        self.bs.click_confirm()
        time.sleep(5)

        # 获取后台新增商品货号
        num =self.bs.get_back_good_no()
        print(num)

        # 点击查看
        self.bs.click_look_good()

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

        # 获取前台货号
        num1 = self.libuy.get_front_good_no()
        print(num1)

        self.assertEqual(num,num1,msg='不相等哦')
