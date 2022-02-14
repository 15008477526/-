'''
'''

from common.base import Base

# 测试点击再次购买按钮
class Repurchase(Base):
    repurchase_loc = ('link text','再次购买')
    def repurchase(self):
        self.click(self.repurchase_loc)

