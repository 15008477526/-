
from page.login_page import LoginPage

url = "http://ecshop.itsoso.cn/user.php?act=address_list"

'''
修改地址
'''
class ModifyAddress(LoginPage):
    province_log = ('id', 'selProvinces_0')  # 下拉框 省
    city_log = ('id', 'selCities_0')  # 下拉框 市
    area_log = ('id', 'selDistricts_0')  # 下拉框 区
    name_log = ('id', 'consignee_0')  # 收件人
    address_log = ('id', 'address_0')  # 详细地址
    tel_log = ('id', 'tel_0')  # 电话
    mailbox_log = ('id', 'email_0')  # 邮箱
    zip_code_log = ('id', 'zipcode_0')  # 邮政编码
    handset_log = ('id', 'mobile_0')  # 手机
    sure_log = ('css selector', 'input[value="确认修改"]')  # 确认修改按钮
    delete_log = ('css selector', 'input[value="删除"]')  # 删除
    yonghu = ('link text', '用户中心')

    def recevied_good(self):
        self.click(self.yonghu)

    # 下拉框省
    def province(self):
        self.clickSelect(self.province_log)

    # 下拉框市
    def city(self):
        self.clickSelect(self.city_log)

    # 下拉框区
    def area(self):
        self.clickSelect(self.area_log)

    # 收件人输入框
    def input_name(self, text):
        '''随机输入'''
        self.send_keys(self.name_log, text)

    # 详细地址输入框
    def input_address(self, text):
        '''随机输入'''
        self.send_keys(self.address_log, text)

    # 电话输入框
    def input_tel(self, text):
        '''随机输入'''
        self.send_keys(self.tel_log, text)

    # 邮箱输入框
    def input_email(self, text):
        '''随机输入'''
        self.send_keys(self.mailbox_log, text)

    # 邮编输入框
    def input_postcode(self, text):
        '''随机输入'''
        self.send_keys(self.zip_code_log, text)

    # 手机输入框
    def input_handest(self, text):
        '''随机输入'''
        self.send_keys(self.handset_log, text)

    # 确认修改按钮
    def click_sure(self):
        '''点击'''
        self.click(self.sure_log)

    # 删除按钮
    def click_delete(self):
        '''点击'''
        self.click(self.delete_log)

    #  弹框
    def tankuang(self):
        # 进入弹框
        alert = self.driver.switch_to.alert
        alert.accept()

    # 关闭浏览器
    def quit(self):
        self.quit()


if __name__ == '__main__':
    from common.base import open_browser
    import time
    from common.base import Base
    from page.add_address import Receiving1

    driver = open_browser('chrome')
    bs1 = Base(driver)
    base = Receiving(driver)
    base.open_url("http://ecshop.itsoso.cn/user.php?act=address_list")
    username1 = ('name', 'username')
    base.find_element(username1).send_keys('leiyu')
    password1 = ('name', 'password')
    base.find_element(password1).send_keys('leiyu980920')
    submit1 = ('name', 'submit')
    base.find_element(submit1).click()
    yonghu = ('link text', '收货地址')
    base.find_element(yonghu).click()

    # # 下拉框
    # base.province()
    # time.sleep(1)
    # base.city()
    # time.sleep(1)
    # base.area()
    # time.sleep(1)
    #
    #
    # result = base.randomData()
    # # # 输入项
    # base.input_name(result[0])
    # base.input_address(result[1])
    # base.input_tel(result[3])
    # base.input_email(result[2])
    # base.input_postcode(result[4])
    # base.input_handest(result[3])
    base.click_delete()
    base.tankuang()
