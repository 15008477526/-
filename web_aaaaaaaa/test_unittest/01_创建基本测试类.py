# 导入
import unittest

 # 创建测试类
 # 测试类继承unittest.TestCase

class Test_demo_1(unittest.TestCase):
     # test fixture 不是必须方法
    def test_case_a(self):
        '''测试用例1'''
        print('执行测试用例1')

    def test_case_c(self):
        '''测试用例3'''
        print('执行测试用例3')

    def test_case_b(self):
         '''测试用例2'''
         print('执行测试用例2')

if __name__ == '__main__':
    unittest.main(verbosity=2)