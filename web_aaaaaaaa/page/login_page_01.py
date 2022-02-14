'''
'''

"""
login_page.py
封装页面的表现层
封装页面的操作层
需要继承base类
"""
from common.base import Base

login_url = "http://ecshop.itsoso.cn/user.php"  # 页面地址


class LoginPage(Base):
    """封装表现层: 制作定位器"""
    username_loc = ("name", "username")  # 用户名输入框
    password_loc = ("name", "password")  # 密码输入框
    remember_loc = ("id", "remember")  # 记住密码复选框
    submit_loc = ("class name", "us_Submit")  # 立即登录按钮
    result_loc = ('class name','f4_b')

    """
    封装操作层: 元素操作
    每一个元素的操作,都写成一个方法
    低耦合性:
        打电话:
            1.拿起手机
            2.拨号
            3.通话
        发短信:
            1.拿起手机
            2.编辑短信
            3.发送
        封装方法:
        1.拿起手机,2.拨号,3.通话,4编辑短信,5.发送
    """
    def input_username(self,text):
        """输入用户名"""
        self.send_keys(self.username_loc,text)

    def input_password(self,text):
        """输入密码"""
        self.send_keys(self.password_loc,text)

    def click_remember(self):
        """点击记住密码"""
        if self.is_selected(self.remember_loc):
            pass
        else:
            self.click(self.remember_loc)

    def click_submit(self):
        """点击立即登录"""
        self.click(self.submit_loc)



