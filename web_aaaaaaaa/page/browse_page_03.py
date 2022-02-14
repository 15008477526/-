'''

'''

# 导包
from common.base import Base
from page.login_page_01 import LoginPage

class Browse_page(Base):
    # 点击手机
    phone_loc = ('link text','手机')
    def click_phone(self):
        self.click(self.phone_loc)



