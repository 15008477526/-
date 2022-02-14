'''
登录页面
    封装页面表现层 操作层
    继承Base
'''
from common.base import Base

login_url ='http://ecshop.itsoso.cn/user.php'

class LoginPage(Base):
    username_loc=('name','username')  # 用户名输入框
    password_loc=('name','password')  # 密码输入框
    remember_loc=('id','remember')  # 记住密码 复选框
    submit_loc=('class name','us_Submit') # 立即登录按钮
    user_loc=('class name','f4_b')  # 登录成功后显示用户名
    quit_loc=('link text','退出') # 登录成功后退出按钮


    '''封装操作层'''
    # 用户名输入
    def input_username(self,text):
        self.send_keys(self.username_loc,text)

    # 密码输入
    def input_password(self,text):
        self.send_keys(self.password_loc,text)

    # 复选框 记住密码
    def click_remember(self):
        if self.is_selected(self.remember_loc):
            pass
        else:
            self.is_selected(self.remember_loc)

    # 点击立即登录
    def click_submit(self):
        self.click(self.submit_loc)



if __name__ == '__main__':
    from common.base import open_browser
    driver =open_browser('chrome')  # 打开浏览器
    login = LoginPage(driver)
    login.open_url(login_url)
    login.input_username('123456')
    login.input_password('123456')
    login.click_submit()
    quit_loc = ('link text', '退出')  # 登录成功后退出按钮
    result =login.displayed(quit_loc)
    print(result)

