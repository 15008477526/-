'''
后台商品管理
@author : 魏江霖

'''
from common.base import Base
from page.good_details3 import Buy_Good
login_back_url ='http://ecshop.itsoso.cn/admin/index.php'

class Back_Stage(Base):
    '''后台管理添加商品'''
    # 商品管理按钮
    shop_manager_loc=('class name','icon-goods')

    # 添加新商品
    add_good_loc =('css selector','a[href="goods.php?act=add"]')
    # 商品名称
    good_name_loc =('name','goods_name')
    # 颜色选择
    color_sele_loc=('css selector','img[style="margin-top:-1px]')
    # 字体样式
    script_style_loc=('name','goods_name_style')
    # 商品货号
    good_no_loc=('name','goods_sn')
    # 商品分类
    good_sort_loc=('name','cat_id')
    # 添加分类
    add_sort_loc=('css selector','button[onclick=rapidCatAdd()]')
    # 添加按钮
    add_loc=('css selector','input[value="添加"]')
    # 商品品牌下拉框
    shop_brand_loc=('name','brand_id')
    # 添加品牌
    add_brand_loc=('css selector','button[onclick="rapidBrandAdd()]')
    # 选择供货商下拉框
    supplier_loc=('name','suppliers_id')
    # 本店售价
    sell_price_loc=('name','shop_price')
    # 按市场价计算
    calc_price_loc =('css selector','input[onclick="marketPriceSetted()]')
    # 会员代销用户
    member_loc=('id','rank_3')
    # 会员价格123
    member_123_loc=('id','rank_6')
    # 会员VIP
    member_vip_loc=('id','rank_2')
    # 优惠数量
    youhui_num_loc=('name','volume_number[]')
    # 优惠价格
    youhui_price_loc=('name','volume_price[]')
    # 市场售价
    market_sell_loc=('name','market_price')
    # 市场售价取整数
    get_int_loc=('css selector','input[value="取整数"]')
    # 虚拟销量
    fictitious_loc=('name','virtual_sales')
    # 赠送消费积分
    give_integral_loc=('name','give_integral')
    # 赠送等级积分数
    rank_integral_loc=('name','rank_integral')
    # 积分购买金额
    integral_loc=('name','integral')
    # 促销价勾选框
    promotional_price_forword_loc=('id','is_promote')
    # 促销价输入框
    promo_price_loc=('id','promote_1')

    # 上传商品图片 选择文件
    put_on_loc=('name','goods_img')

    # 上传商品图片 输入框
    put_on_send_loc=('name','goods_img_url')

    # 确定按钮
    confirm_loc=('css selector','input[value=" 确定 "]')

    # 重置按钮
    reset_loc=('css selector','input[value=" 重置 "]')

    # 详细描述
    detail_descr_loc =('id','detail-tab')

    # 详细描述输入框
    send_msg_loc=('css selector','body[spellcheck="false"]')

    # 详细描述iframe
    frame_loc=('css selector','iframe[src="javascript:void(0)"]')

    # 其他信息
    other_msg_loc=('id','mix-tab')

    # 商品重量
    good_weight_loc=('name','goods_weight')

    # 复选框推荐
    checkbox_loc=('css selector','#mix-table>tbody>tr:nth-of-type(4)>td:nth-of-type(2)>input')

    # 上架框
    put_on_sale_loc=('name','is_on_sale')

    # 能作为普通商品销售
    sale_loc=('name','is_alone_sale')

    # 是否为免运费
    freight_loc=('name','is_shipping')

    # 商品属性
    good_attribute_loc=('id','properties-tab')

    # 商品类型下拉框
    good_type_loc=('name','goods_type')

    # 商品相册
    good_picture_loc=('id','gallery-tab')

    # 图片描述
    pic_des_loc=('name','img_desc[]')

    # 相册上传文件按钮
    shangchuan_button_loc=('name','img_url[]')

    # 输入链接地址
    url_loc=('name','img_file[]')

    # 后台新增商品货号
    back_good_no_loc=('css selector','div#listDiv>table>tbody>tr:nth-of-type(3)>td:nth-of-type(4)>span')

    # 新增商品查看
    look_good_loc=('css selector','div#listDiv>table>tbody>tr:nth-of-type(3)>td:nth-of-type(13)>a')


    # 点击商品名称输入
    def click_good_name(self,text):
        self.click(self.good_name_loc)
        self.send_keys(self.good_name_loc,text)

    # 字体样式选择
    def select_sort(self):

        self.clickSelect(self.script_style_loc)

    # 商品分类选择
    def select_good(self):
        self.clickSelect(self.good_sort_loc)

    # 商品品牌选择
    def select_brand(self):
        self.clickSelect(self.shop_brand_loc)

    # 本店售价输入
    def send_sell_price(self,price):
        element =self.find_element(self.sell_price_loc)
        element.clear()
        element.send_keys(price)

    # 促销价勾选框
    def select_promotional_price(self):
        element =self.find_element(self.promotional_price_forword_loc)
        try:
            if element.is_selected():
                element.click()
            else:
                pass
        except:
            print('有错啦')

    # 促销价输入框
    def send_promo_price(self,price):
        element=self.find_element(self.promo_price_loc)
        element.clear()
        element.send_keys(price)

    # 确定按钮点击
    def click_confirm(self):
        self.find_element(self.confirm_loc).click()

    # 上传商品文件
    def click_put_on_picture(self):
        self.find_element(self.put_on_loc).click()

    # 商品管理点击
    def click_shop_manager(self):

        element =self.find_element(self.shop_manager_loc)
        element.click()
    # 添加新商品点击
    def click_add_shop(self):
        self.find_element(self.add_good_loc).click()

    # 上传商品图片输入框
    def send_put_on_picture(self,url):
        element =self.find_element(self.put_on_send_loc)
        element.clear()
        element.send_keys(url)

    # 点击详细描述
    def click_detail_des(self):
        self.find_element(self.detail_descr_loc).click()


    # 详细输入框输
    def send_msg(self,msg):
        self.switch_to_frame('goods_desc___Frame')
        self.switch_to_frame(self.find_element(self.frame_loc))
        element=self.find_element(self.send_msg_loc)
        element.click()
        element.send_keys(msg)
        self.quit_frame()

    # 其他信息点击
    def click_other_msg(self):
        self.switch_to_frame('main-frame')
        self.find_element(self.other_msg_loc).click()

    # 商品重量点击输入
    def send_good_weight(self,num):
        element =self.find_element(self.good_weight_loc)
        element.click()
        element.send_keys(num)

    # 加入推荐 复选框操作
    def choice_box(self):
        boxes =self.find_elements(self.checkbox_loc)
        for box in boxes:
            if box.is_selected():
                pass
            else:
                box.click()

    # 点击上架
    def click_put_on(self):
        element=self.find_element(self.put_on_sale_loc)
        if element.is_selected():
            self.double_click(self.put_on_sale_loc)
        else:
            pass

    # 勾选销售商品
    def click_sale(self):
        element = self.find_element(self.sale_loc)
        if element.is_selected():
            self.double_click(self.sale_loc)
        else:
            pass

    # 勾选免运费商品
    def click_freight(self):
        element =self.find_element(self.freight_loc)
        if element.is_selected():
            pass
        else:
            element.click()

    # 点击商品属性
    def click_attribute(self):
        element=self.find_element(self.good_attribute_loc)
        element.click()

    # 商品类型勾选
    def select_type(self):
        self.clickSelect(self.good_type_loc)

    # 点击商品相册
    def click_picture(self):
        element =self.find_element(self.good_picture_loc)
        element.click()

    # 点击图片描述输入框
    def click_pic_des(self,text):
        element=self.find_element(self.pic_des_loc)
        element.click()
        element.send_keys(text)

    # 选择文件按钮
    def click_shangchuan(self):
        element =self.find_element(self.shangchuan_button_loc)
        # element.click()
        element.send_keys(r'E:\python\python_work\ecshop\script\test_login.py')

    #点击外部链接
    def click_url(self,url):
        element= self.find_element(self.url_loc)
        element.click()
        element.send_keys(url)

    # 获取后台新增商品货号
    def get_back_good_no(self):
        element=self.find_element(self.back_good_no_loc)
        text =element.text
        return text

    # 点击新增商品查看按钮
    def click_look_good(self):
        element= self.find_element(self.look_good_loc)
        element.click()




if __name__ == '__main__':
    from common.base import open_browser
    import time
    driver=open_browser('chrome')
    bs = Back_Stage(driver)
    libuy=Buy_Good(driver)
    bs.open_url('http://ecshop.itsoso.cn/admin/index.php')
    username_loc=('name','username')
    username =bs.find_element(username_loc)
    username.send_keys('admin')
    password_loc=('name','password')
    password=bs.find_element(password_loc)
    password.send_keys('admin123')
    submit_loc=('css selector','input[value="登 录"]')
    submit =bs.find_element(submit_loc)
    submit.click()
    # 进入iframe
    time.sleep(3)
    bs.switch_to_frame('menu-frame')
    # driver.switch_to.frame('menu-frame')
    # 商品管理按钮

    bs.click_shop_manager()
    # good =driver.find_element_by_css_selector('li[class="icon-goods"]')

    # 添加新商品
    # add_good_loc = ('css selector', 'a[href="goods.php?act=add"]')
    bs.click_add_shop()
    # add_good =driver.find_element_by_css_selector('a[href="goods.php?act=add"]')
    # add_good.click()
    # 退出iframe
    # bs.quit_1_frame()
    # driver.switch_to.parent_frame()
    bs.quit_patent_frame()
    # 在进入iframe
    bs.switch_to_frame("main-frame")

    # 添加商品名称
    bs.click_good_name('可口可乐')
    # 字体样式选择
    bs.select_sort()
    # 商品分类
    bs.select_good()
    # 商品品牌选择
    bs.select_brand()
    # 本店售价
    bs.send_sell_price(45)
    # 点击商品上传 输入框
    bs.send_put_on_picture('http://image.namedq.com/uploads/20181219/23/1545233909-MDtFANczwO.jpg')

    # 点详细描述
    bs.click_detail_des()

    bs.send_msg('这是娑娜')

    bs.click_other_msg()

    bs.send_good_weight(2)

    # 复选框 加入推荐
    bs.choice_box()

    # 上架勾选
    bs.click_put_on()

    # 普通商品销售
    bs.click_sale()

    # 免运费商品
    bs.click_freight()
    # 点击商品属性
    bs.click_attribute()

    # 商品类型勾选
    bs.select_type()

    # 点击商品相册
    bs.click_picture()

    # 点击图片描述
    # bs.click_pic_des('云顶之弈')
    # 选择文件按钮
    # bs.click_shangchuan()

    # 点击外部链接
    bs.click_url('www.baidu.com')
    # # 确定按钮
    bs.click_confirm()

    time.sleep(3)
    # 获取后台新增商品货号
    num =bs.get_back_good_no()
    print(num)

    # 点击查看
    bs.click_look_good()

    # 切换到前台窗口
    handles=driver.window_handles
    driver.switch_to.window(handles[1])

    # 获取前台货号
    num1 = libuy.get_front_good_no()
    print(num1)
