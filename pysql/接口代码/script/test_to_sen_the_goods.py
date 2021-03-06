'''
@author:杨钟
@time:2019/09/23
'''
#待发货
import unittest
from interface.login_3interface import Login
from interface.to_sen_the_3goods import Tstsg
from common.get_keyword import GetKeyword
from common.py_lizi import Database

class TestToSen(unittest.TestCase):
    def setUp(self):
        self.session = Login.get_session()
        self.db = Database()#实例化Database

    def test_to_sen(self):
        sen_data ={"session":self.session,"type":"await_ship","pagination":{"count":10,"page":1}}
        response = Tstsg.tstsg(sen_data)
        # 获取返回值中的订单号
        order = GetKeyword.get_value_by_keyword(response, "order_sn")
        print(order)
        # 获取用户的uid
        uid = GetKeyword.get_value_by_keyword(self.session, 'uid')
        # print(type(uid))
        # 查找订单表中对应用户的所有的待付款订单号
        all_order_sn = self.db.read_all(f"select order_sn from ecs_order_info where user_id = {uid}")
        # print(all_order_sn)
        # 返回的order_sn是列表格式,获取所有的值
        all_order = GetKeyword.get_values_by_keyword(all_order_sn, "order_sn")
        print(all_order)
        # 判断待付款的订单是否在订单列表里面 子集
        self.assertIsNotNone(set(order).issubset(all_order))

    if __name__ == '__main__':
        unittest.main()