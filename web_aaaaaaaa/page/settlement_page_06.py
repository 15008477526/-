'''
'''

from common.base import Base

class Settlement(Base):
    settlement_loc = ('css selector','img[alt="checkout"]')
    def settlement_o1(self):
        self.click(self.settlement_loc)   # 点击去结算

# if __name__ == '__main__':
#     from common.base import open_browser
#     from common.base import Base
#     from page.下单 import purchase_page
#
#     driver = open_browser('chrome')
#     driver01 = purchase_page.Purchase(driver)
#
#     Settlement_01 = Settlement(driver)
#     Settlement_01.open_url('http://ecshop.itsoso.cn/goods.php?id=304')
#     driver01.purchase()
#     Settlement_01.settlement_o1()
