'''
'''

from common.base import Base

class BuyNowPage(Base):
    buy_now_loc = ('class name','price-btn')
    # 点击立即购买
    def buy_now(self):
        self.click(self.buy_now_loc)






