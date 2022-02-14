from selenium import webdriver

# driver = webdriver.Chrome()

# 火狐浏览器 先记住密码
# 火狐浏览器 帮助---故障排除信息--配置文件夹
# profile_director = "配置文件夹的路径"
# # 实例化火狐浏览器配置项
# profile = webdriver.FirefoxProfile(profile_director)
# driver = webdriver.Firefox(profile)

# 谷歌浏览器

user_data_dir = r"--user-data-dir=C:\Users\windows-pc\AppData\Local\Google\Chrome\User Data"
# # # 配置谷歌浏览器加载项
options = webdriver.ChromeOptions()
options.add_argument(user_data_dir)

driver = webdriver.Chrome(options=options)

driver.get("http://oms-uat.jiangxi-isuzu.cn/#/login")