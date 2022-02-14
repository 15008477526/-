'''
@author:魏江霖


注册
'''
from common.base import Base

register_url='http://ecshop.itsoso.cn/user.php?act=register'

class Register(Base):
    '''注册'''
    # 用户名输入框
    username_loc=('id','username')

    # email输入框
    email_loc=('id','email')

    # 密码输入框
    password_loc=('id','password1')

    # 确认密码输入框
    confirm_password_loc=('id','conform_password')

    # 手机输入框
    phone_loc=('name','extend_field5')

    # 密码提示问题下拉框
    select_password_loc=('name','sel_question')

    # 密码问题答案
    answer_question_loc=('name','passwd_answer')

    # 单选框
    radio_loc=('name','agreement')

    # 立即注册按钮
    register_loc=('name','Submit')

    # 已有账号,要登录链接
    login_loc=('link text','我已有账号，我要登录')

    # 忘记密码链接
    forget_password_loc=('link text','您忘记密码了吗？')

    # 输入用户名
    def input_username(self,text):
        self.send_keys(self.username_loc,text)

    # email输入框
    def input_email(self,text):
        self.send_keys(self.email_loc,text)

    # 密码输入框
    def input_password(self,password):
        self.send_keys(self.password_loc,password)

    # 确认密码输入框
    def input_confirm_password(self,password):
        self.send_keys(self.confirm_password_loc,password)

    # 手机输入框
    def input_phone(self,phone):
        self.send_keys(self.phone_loc,phone)

    # 密码提示问题选择
    def click_password_question(self):
        self.clickSelect(self.select_password_loc)

    # 密码问题答案输入
    def input_question(self,answer):
        self.send_keys(self.answer_question_loc,answer)

    # 看过并接受协议
    def remember_receive(self):
        if self.is_selected(self.radio_loc):
            pass
        else:
            self.is_selected(self.radio_loc)

    # 立即注册点击
    def click_register(self):
        self.click(self.register_loc)

    # 点击我要登录
    def click_login(self):
        self.click(self.login_loc)

    # 点击忘记密码
    def click_forget(self):
        self.click(self.forget_password_loc)

if __name__ == '__main__':
    from common.base import open_browser
    driver=open_browser('chrome')
    zc =Register(driver)  # 实例化
    zc.open_url(register_url)
    from common.register_data import RegisterData
    register = RegisterData()
    lists = register.get_data_for_list()  # 随机数据
    zc.input_username(lists[0])
    zc.input_email(lists[2])
    password =lists[1]
    zc.input_password(password)
    zc.input_confirm_password(password)
    zc.input_phone(lists[3])
    zc.click_password_question() # 密码提示问题
    zc.input_question('安妮')
    # zc.click_register()  # 立即注册
    # zc.click_login() # 我要登录