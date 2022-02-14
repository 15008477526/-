
'''
添加收货地址
'''
from common.base import Base

add_address_url = "http://ecshop.itsoso.cn/user.php?act=address_list"

class AddDress(Base):
    # 下拉框 省
    province_loc = ('xpath', '//form[last()]/table/tbody/tr/td[2]/select[2]')
    # 下拉框 市
    city_loc = ('xpath', '//form[last()]/table/tbody/tr/td[2]/select[3]')
    # 下拉框 区
    area_loc = ('xpath', '//form[last()]/table/tbody/tr/td[2]/select[4]')
    # 收件人
    name_loc = ('xpath', '//form[last()]/table/tbody/tr[2]/td[2]/input')
    # 详细地址
    address_loc = ('xpath', '//form[last()]/table/tbody/tr[3]/td[2]/input')
    # 电话
    tel_loc = ('xpath', '//form[last()]/table/tbody/tr[4]/td[2]/input')
    # 邮箱
    mailbox_loc = ('xpath', '//form[last()]/table/tbody/tr[2]/td[4]/input')
    # 邮政编码
    zip_code_loc = ('xpath', '//form[last()]/table/tbody/tr[3]/td[4]/input')
    # 手机
    handset_loc = ('xpath', '//form[last()]/table/tbody/tr[4]/td[4]/input')
    # 新增收货地址
    add_loc = ('css selector', 'input[value="新增收货地址"]')
    # 用户中心
    yonghu_loc = ('link text', '收货地址')
    user_loc =("link text", '用户中心')

    def recevied_good(self):
        self.click(self.yonghu_loc)

    # 下拉框省
    def add_province(self):
        '''随机生成省'''
        self.clickSelect(self.province_loc)

    # 下拉框市
    def add_city(self):
        '''随机生成市'''
        self.clickSelect(self.city_loc)

    # 下拉框区
    def add_area(self):
        '''随机生成区'''
        self.clickSelect(self.area_loc)

    # 收件人输入框
    def add_input_name(self, text):
        '''随机输入名字'''
        self.send_keys(self.name_loc, text)

    # 详细地址输入框
    def add_input_address(self, text):
        '''随机输入详细地址'''
        self.send_keys(self.address_loc, text)

    # 电话输入框
    def add_input_tel(self, text):
        '''随机输入电话'''
        self.send_keys(self.tel_loc, text)

    # 邮箱输入框
    def add_input_email(self, text):
        '''随机输入邮箱'''
        self.send_keys(self.mailbox_loc, text)

    # 邮编输入框
    def add_input_postcode(self, text):
        '''随机输入邮编'''
        self.send_keys(self.zip_code_loc, text)

    # 手机输入框
    def add_input_handest(self, text):
        '''随机输入手机'''
        self.send_keys(self.handset_loc, text)

    #  新增收货地址
    def click_add(self):
        '''点击'''
        self.click(self.add_loc)

    # 关闭浏览器
    def quit(self):
        self.quit()


if __name__ == '__main__':
    from common.base import open_browser
    import time
    from common.base import Base

    driver = open_browser('chrome')
    bs1 = Base(driver)
    base = AddDress(driver)
    base.open_url("http://ecshop.itsoso.cn/user.php?act=address_list")
    username1 = ('name', 'username')
    base.find_element(username1).send_keys('123456')
    password1 = ('name', 'password')
    base.find_element(password1).send_keys('123456')
    submit1 = ('name', 'submit')
    base.find_element(submit1).click()
    yonghu_loc = ('link text', '收货地址')
    base.find_element(yonghu_loc).click()

    # 下拉框
    base.add_province()
    time.sleep(1)
    base.add_city()
    time.sleep(1)
    base.add_area()
    time.sleep(1)


