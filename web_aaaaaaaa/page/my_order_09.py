'''
'''

from common.base import Base

class MyOrder(Base):
    # 我的订单定位器
    myorder_loc = ('css selector',' a[href="user.php?act=order_list" ]')
    def My_Order(self):
        self.click(self.myorder_loc)    # 点击我的订单


