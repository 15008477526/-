'''
商品详情页面
'''
from common.base import Base


good_url ='http://ecshop.itsoso.cn/goods.php?id=304'

class Buy_Good(Base):
    '''页面点击立即购买'''
    # 商品名字
    good_name_loc=('class name','goods_style_name')
    # 商品牌子
    good_brand_loc=('css selector','a[href="brand.php?id=20"]')
    # 购买数量框
    number_loc=('id','number')
    # 立即购买框
    libuy_loc=('css selector','img[src="themes/default/images/buybtn1.png"]')
    # 收藏按钮
    collect_loc=('css selector','img[src="themes/default/images/bnt_colles.gif"]')
    # 分享按钮
    share_loc =('css selector','img[src="themes/default/images/bnt_recommend.gif"]')
    # 价格
    price_loc=('id','ECS_RANKPRICE_6')

    # 前台商品货号
    front_good_no_loc=('css selector','li.clearfix:nth-child(1)>dd:nth-child(1)')


    # 点击商品牌子
    def click_brand(self):
        self.click(self.good_brand_loc)

    # 购买数量输入
    def send_number(self,num):

        self.double_click(self.number_loc)
        self.send_keys(self.number_loc,num)
        self.click(self.price_loc)
    # 点击立即购买
    def click_libuy(self):
        self.click(self.libuy_loc)


    # 点击收藏按钮
    def click_collect(self):
        self.click(self.collect_loc)

    # 点击分享按钮
    def click_share(self):
        self.click(self.share_loc)

    # 获取商品名称
    def get_good_name(self,locator):
        element =self.find_element(locator)
        text = element.text
        return text

    # 前台商品详情页面获取商品货号
    def get_front_good_no(self):
        element=self.find_element(self.front_good_no_loc)
        content =element.text.split('：')
        text =content[1]   # ECS000304
        # print(content)  商品货号：ECS000304
        return text



if __name__ == '__main__':
    from common.base import open_browser
    from time import sleep
    driver = open_browser('chrome')
    libuy = Buy_Good(driver)  # 实例化Buy_Good
    libuy.open_url(good_url)
    good_name_loc = ('class name', 'goods_style_name')
    print(libuy.get_good_name(good_name_loc))

    # 前台商品货号
    front_good_no_loc = ('css selector', 'li.clearfix:nth-child(1)>dd:nth-child(1)')
    num =libuy.get_front_good_no()
    print(num)
    # sleep(2)
    # libuy.send_number(3)
    # sleep(3)
    #
    #
    # libuy.click_libuy()
