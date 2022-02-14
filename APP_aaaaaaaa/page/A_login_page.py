"""@author:郁华夏"""

from common.base_app import BaseApp


class LoginPage(BaseApp):
    """登录/注册页面"""

    account_num_loc = ('id', 'com.tpshop.malls:id/mobile_et')  # 账号输入框
    password_loc = ('id', 'com.tpshop.malls:id/pwd_et')  # 密码输入框
    confirm_login_loc = ('id', 'com.tpshop.malls:id/login_tv')  # 确认登录

    def input_account_num(self, mobile):
        """输入账号"""
        self.send_keys(self.account_num_loc, mobile)

    def input_password(self, pwd):
        """输入密码"""
        self.send_keys(self.password_loc, pwd)

    def click_confirm_login(self):
        """点击<登录>"""
        self.click(self.confirm_login_loc)


if __name__ == '__main__':
    from common.base_app import open_app
    from time import sleep

    driver = open_app()  # 打开TPShop,进入登录页面
    login = LoginPage(driver)
    login.input_account_num('13730626896')  # 输入账号
    sleep(1)
    login.input_password('123456')  # 输入密码
    sleep(1)
    login.click_confirm_login()  # 点击登录
    sleep(2)
    login.quit()
