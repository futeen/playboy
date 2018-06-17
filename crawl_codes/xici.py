import requests
from scrapy.selector import Selector
import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="article_spider", charset="utf8")
cursor = conn.cursor()


def crawl_ips():
    # 爬取西刺的免费ip代理
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
    for i in range(1, 2):
        print(i)
        re = requests.get("http://www.xicidaili.com/nn/{0}".format(i), headers=headers)
        selector = Selector(text=re.text)
        ip_select = selector.xpath("//*/tr/td[2]").extract()
        ip_list = []
        for ip in ip_select:
            ip_list.append(ip[5:-5])
        # print(ip_list)
        for x in ip_list:
            cursor.execute(
                "insert proxy_ip(ip) VALUES('{0}')".format(x)
            )
            conn.commit()


crawl_ips()


