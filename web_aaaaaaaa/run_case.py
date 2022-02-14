
import unittest
import time
import HTMLTestRunnerPlugins
""" 
测试套件：方式三：unittest.defaultTestLoader() 
"""
test_dir='./script'
discover=unittest.defaultTestLoader.discover(test_dir)


# 指定测试报告存放位置
report_dir ='./report'

# 命名测试报告名称
now =time.strftime('%Y-%m-%d %H_%M_%S')

report_filename =report_dir+'/'+now+'report.html' # 测试报告路径+名称

with open(report_filename,'wb') as fp:
    # 使用第三方插件执行并生成测试报告
    runner = HTMLTestRunnerPlugins.HTMLTestRunner(
        title='ECShop自动化测试报告',
        description='登录注册页面自动化',
        stream=fp
    )


# 执行测试套件中的测试用例
    runner.run(discover)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)