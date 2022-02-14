# 导入
import unittest

# 创建测试类
class Test_Demo_2(unittest.TestCase):

# 添加特殊方法
    def setUp(self):
        print('setUp在每条测试用例前执行一次')

    def tearDown(self):
        print('tearDown在每条测试用例执行后执行一次')

    @classmethod
    def setUpClass(cls):
        print('setUpClass在所有测试用例前执行前执行一次')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass在所有测试用例前执行后执行一次')

# 添加测试用例
    def test_case_a(self):
        '''测试用例1'''
        print('执行测试用例1')
        self.assertEqual([],[],msg='出错啦')

    def test_case_c(self):
        '''测试用例3'''
        print('执行测试用例3')
        self.assertTrue('',msg='c出错啦')

    def test_case_b(self):
         '''测试用例2'''
         print('执行测试用例2')
         self.assertEqual('2','2',msg='b出错了')

if __name__ == '__main__':
    unittest.main(verbosity=2)