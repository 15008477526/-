'''
ddt
'''

import unittest
import ddt

# 准备测试数据
test_data=[
    {'username':'jianji','password':'1234'},
    {'username':'azir','password':'1234'},
    {'username':'ashe','password':'1234'},
    {'username':'vn','password':'1234'},
    {'username':'mouse','password':'1234'}
]

# 测试类
@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(*test_data)
    def test_case_1(self,data):
        print(data['username'],data['password'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
