'''
'''

from common.base import Base


class SubmitOrder(Base):
    # 申通
    sto_loc = ('css selector','input[value="5"]')
    # 邮局平邮
    post_loc = ('css selector','input[value="6"]')
    # 到付
    to_pay_loc = ('css selector','input[value="7"]')
    # 天工收银
    tien_gong_loc = ('css selector','input[value="4"]')
    # 支付宝
    alipay_loc = ('css selector','input[value="alipay"]')
    # 微信
    weixin_loc = ('css selector','input[value="vxpay"]')
    # 余额
    balance_loc = ('css selector','input[value="1"][onclick="selectPayment(this)"]')
    # 银行转账
    bank_loc = ('css selector','input[value="2"]')
    # 货到付款
    reach_loc = ('css selector','input[value="3"]')
    # 支付宝
    payment_loc = ('name','payment')
    # 提交订单
    place_order_loc = ('css selector','input[type="image"]')



    def sto(self):
        # 点击选择申通
        self.click(self.sto_loc)

    def post(self):
        # 点击选择平邮
        self.click(self.post_loc)

    def to_pay(self):
        # 点击选择到付
        self.click(self.to_pay_loc)

    def tien_gong(self):
        # 选择天工收银
        self.click(self.tien_gong_loc)

    def alipay(self):
        # 选择支付宝
        self.click(self.alipay_loc)

    def weixin(self):
        # 选择微信
        self.click(self.weixin_loc)

    def balance(self):
        # 选择余额
        self.click(self.balance_loc)

    def bank(self):
        # 选择银行转账
        self.click(self.bank_loc)

    def reach(self):
        # 选择货到付款
        self.click(self.reach_loc)

    def payment(self):
        # 选择支付宝支付
        self.click(self.payment_loc)

    def place_order(self):
        # 提交订单
        self.click(self.place_order_loc)












