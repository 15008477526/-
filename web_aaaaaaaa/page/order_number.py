'''
'''

# 验证点击 订单号
from common.base import Base

class OrderNumber(Base):
    rdernumber_loc = ('class name','f6')
    def ordernumber(self):
        self.click(self.rdernumber_loc)     # 点击 订单号




