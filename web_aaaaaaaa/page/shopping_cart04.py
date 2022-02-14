from common.base import Base
from page.good_details3 import Buy_Good,good_url

class ShoppingCart(Base):
    # 商品名称
    good_name_loc =('class name','f6')
    # 继续购物
    keep_shopping_loc=('css selector','img[alt="continue"]')
    # 购买数量
    buy_num_loc=('class name','inputBg')

    # 清空购物车
    clear_car_loc=('css selector','input[type="button"]')
    # 更新购物车
    refresh_car_loc=('name','submit')
    # 删除按钮
    delete_loc =('link text','删除')
    # 去结算
    pay_loc=('css selector','img[alt="checkout"]')

    # 购物金额小计
    buy_price_loc=('css selector','td[bgcolor="#ffffff"]')


    def click_keep_shopping(self):
        self.click(self.keep_shopping_loc)

    def click_send_num(self):
        self.click(self.buy_num_loc)
    # 输入数量
    def send_buy_num(self,num):
        self.click(self.buy_num_loc)
        self.send_keys(self.buy_num_loc,num)

    # 点击清空购物车
    def click_clear_car(self):
        self.click(self.clear_car_loc)

    # 点击更新购物车
    def update_car(self):
        self.click(self.refresh_car_loc)

    # 点击删除按钮
    def delete_button(self):
        self.click(self.delete_loc)

    # 点击去结算
    def pay(self):
        self.click(self.pay_loc)

    # 获取弹窗 确定删除
    def get_alert_confirm(self):
        alert =self.driver.switch_to.alert
        alert.accept()

    # 获取弹窗 取消
    def get_alert(self):
        alert =self.driver.switch_to.alert
        alert.dismiss()

    # 获取商品名称
    def get_name(self,locator):
        element = self.find_element(locator)
        text = element.text
        return text

    # 获取商品数量
    def get_num(self,locator):
        element=self.find_element(locator)
        num =element.get_attribute('value')
        return num

    # 获取金额小计具体内容
    def get_price_content(self,locator):
        element=self.find_element(locator)
        content =element.text
        return content





if __name__ == '__main__':
    from common.base import open_browser
    from time import sleep
    driver = open_browser('chrome')

    buy = Buy_Good(driver)  # 实例化Buy_Good
    buy.open_url(good_url)
    buy.click_libuy()
    shopping =ShoppingCart(driver) # 实例化ShoppingCart

    good_loc=('class name','f6')
    print(shopping.get_name(good_loc))
    buy_num_loc = ('class name', 'inputBg')
    shopping.send_buy_num(3)
    shopping.update_car()
    num =shopping.get_num(buy_num_loc)
    print(num)
    buy_price_loc = ('css selector', 'form[name="formCart"]>table:nth-of-type(2)>tbody>tr>td')
    content =shopping.get_price_content(buy_price_loc)
    print(content)
    # shopping.click_keep_shopping()  # 点击继续购物
    # shopping.click_clear_car() # 清空购物车
    # shopping.click_send_num()
    # shopping.send_buy_num(3)
    # 点击更新购物车
    # shopping.update_car()
    # 点击删除
    # shopping.delete_button()
    # sleep(2)

    # shopping.get_alert_confirm()