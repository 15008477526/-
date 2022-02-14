'''
'''

from common.base import Base

# 浏览
class Browse(Base):
    # 首页定位器
    first_loc = ('class name','cur')
    def click_first(self):
        self.click(self.first_loc)


# if __name__ == '__main__':
#     from common.base import open_browser
#
#     driver = open_browser('chrome')
#     login = LoginPage(driver)
#     browse_first = Browse(driver)
#     browse_first.open_url('http://ecshop.itsoso.cn/user.php')
#
#     login.input_username('zqs')
#     login.input_password('zqs950927')
#     login.click_submit()
#     browse_first.click_first()