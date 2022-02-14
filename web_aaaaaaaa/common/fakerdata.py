'''
@author:魏江霖
@time:2019/9/15

'''
from faker import Faker


# f=Faker(locale="zh_CN")
#
# print(f.name())  # 随机生成用户名
# print(f.address())
# print(f.email())
# print(f.phone_number())
# print(f.random_int(min=0,max=999999999))

class RegisterData:
    def __init__(self):
        self.fk = Faker(locale="zh_CN")

    # def username(self):
    #     """生成用户名"""
    #     return self.fk.name()
    #
    # def password(self):
    #     """生成密码"""
    #     return self.fk.password()
    #
    # def email(self):
    #     """生成邮箱"""
    #     return self.fk.email()
    #
    # def phone_number(self):
    #     """生成手机号码"""
    #     return self.fk.phone_number()

    def get_data_for_list(self):
        """将生成的数据集合成列表"""
        data = [self.fk.name(),self.fk.password(),self.fk.email(),self.fk.phone_number()]
        return data

if __name__ == '__main__':
    register = RegisterData()
    print(register.get_data_for_list())
