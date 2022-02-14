# import random
# a = "".join(random.sample('ABCDEFGHIJKLMNOPQRSTXYZ',5))
# print(a)
# b = "".join(random.choice("0123456789") for i in range(10))
# print(b)

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化
# driver.set_window_size(480,800)
url = "http://oms-uat.jiangxi-isuzu.cn/#/login"
driver.get(url)
sleep(2)

user = driver.find_element_by_css_selector("input[placeholder='账户名']")
password = driver.find_element_by_css_selector("input[placeholder='密码']")

# 定位关键字
# VIN = driver.find_element_by_css_selector("input[placeholder='请输入VIN']")
# # 定位动力类型
# energy_type = driver.find_element_by_xpath("//div[@style='width: 150px;'/div/span]")
#
# # 定位搜索按钮
# button = driver.find_element_by_xpath("//button[@type='button']/span")
button_1 = driver.find_element_by_xpath("//button[@type='button']")

user.send_keys("admin")
password.send_keys("Admin$123")
button_1.click()
# sleep(5)
# VIN.send_keys("8324")
# VIN_8324 = driver.find_element_by_xpath("//div[@class='el-select-dropdown__wrap el-scrollbar__wrap']/ul/li/span")
# VIN_8324.click()
# sleep(3)
# button.click()

sleep(10)
driver.quit()