'''
'''

from common.base import Base

class UserCenter(Base):
    user_loc = ('link text','用户中心')
    def usercenter(self):
        self.click(self.user_loc)   # 点击个人中心



