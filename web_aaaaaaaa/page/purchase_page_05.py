'''
'''

from common.base import Base


class Purchase(Base):
    purchase_loc = ('class name','td1')     # 创建定位器
    def purchase(self):
        self.click(self.purchase_loc)   # 点击立即购买,加入购物车

