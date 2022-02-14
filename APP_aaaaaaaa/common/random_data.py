from faker import Faker

f = Faker(locale="zh_CN")


# print(f.name())  # 随机生成用户名
# print(f.address())
# print(f.email())
# print(f.phone_number())
# print(f.random_int(min=0,max=999999999))

class RandomData:
    def __init__(self):
        self.f = Faker(locale="zh_CN")

    def get_data_for_list(self):
        """将生成的数据集合成列表"""
        data = [self.f.name(), self.f.password(), self.f.phone_number(), self.f.email()]
        return data

    def random_name(self):
        """生成随机姓名"""
        return self.f.name()

    def random_goods_sn(self):
        """生成随机商品货号"""
        return 'ECS' + str(self.f.random_number(digits=6))

    def random_word(self):
        """生成一个随机词语"""
        return self.f.word()

    def random_int_4(self):
        """随机输入一个4位数字"""
        return self.f.random_int()

    def random_text(self):
        """随机输入一篇文章"""
        return self.f.text()

    def random_paragraph(self):
        """随机输入一段话"""
        return self.f.paragraph()

    def random_sentence(self):
        """随机输入一句话"""
        return self.f.sentence()

    def random_company_prefix(self):
        """随机生成一个公司简称"""
        return self.f.company_prefix()

    def random_username(self):
        """随机生成一个用户名"""
        return self.f.user_name()

    def random_email(self):
        """随机生成一个邮箱"""
        return self.f.email()

    def random_password(self):
        """随机生成一个密码"""
        return self.f.password()

    def random_tel(self):
        """随机生成一个手机号"""
        return self.f.phone_number()

    def random_postcod(self):
        """随机生成一个邮编"""
        return self.f.postcode()

    def random_street_address(self):
        """随机生成一个街道地址"""
        return self.f.street_address()

    def random_num_8(self):
        """随机生成8位数字"""
        return self.f.random_number(digits=8)

    def random_num_2(self):
        """随机生成2位数字"""
        return self.f.random_number(digits=2)

    def get_data_for_cnee_list(self):
        """生成收货人地址必填项列表"""
        data = [self.f.name(), self.f.email(), self.f.street_address()]
        return data


if __name__ == '__main__':
    rd = RandomData()
    print(rd.random_int_4())
