import requests
import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8') #改变标准输出的默认编码

#建立Phantomjs浏览器对象，括号里是phantomjs.exe在你的电脑上的路径
browser = webdriver.PhantomJS('d:/tool/07-net/phantomjs-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')

#登录页面
url = r'http://ssfw.xmu.edu.cn/cmstar/index.portal'

# 访问登录页面
browser.get(url)

# 等待一定时间，让js脚本加载完毕
browser.implicitly_wait(3)

#输入用户名
username = browser.find_element_by_name('user')
username.send_keys('学号')

#输入密码
password = browser.find_element_by_name('pwd')
password.send_keys('密码')

#选择“学生”单选按钮
student = browser.find_element_by_xpath('//input[@value="student"]')
student.click()

#点击“登录”按钮
login_button = browser.find_element_by_name('btn')
login_button.submit()

#网页截图
browser.save_screenshot('picture1.png')
#打印网页源代码
print(browser.page_source.encode('utf-8').decode())

browser.quit()
