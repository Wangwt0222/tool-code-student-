import requests
import sys
import io
from selenium import webdriver  # 载入库文件
from selenium.webdriver import FirefoxOptions

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

# 建立Chrome浏览器对象
opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=opts)
# browser = webdriver.FireFox()
# browser = webdriver.Chrome()
# 登录页面
url = r'http://202.204.48.82/0.htm'

# 访问登录页面
browser.get(url)

# 等待一定时间，让js脚本加载完毕
browser.implicitly_wait(3)

# 输入账号，密码
browser.find_element_by_id("uname").clear()
browser.find_element_by_id("uname").send_keys("")
browser.find_element_by_id("upass").clear()
browser.find_element_by_id("upass").send_keys("")
browser.find_element_by_xpath("//input[@type='submit']").click()

# 网页截图
# browser.save_screenshot('picture1.png')
# 打印网页源代码
print(browser.page_source.encode('utf-8').decode())

browser.quit()
