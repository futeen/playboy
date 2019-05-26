import requests
import sys
import io
from urllib import request


def login():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

    # 登录后才能访问的网页
    url = 'fakeurl'

    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    cookie_str = r''

    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value

    req = request.Request(url)
    req.add_header("cookie", cookie_str)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    resp = request.urlopen(req)
    print(resp.read().decode("utf-8"))


if __name__ == "__main__":
    login()

