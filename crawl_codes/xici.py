import requests
from scrapy.selector import Selector
import pymysql
import time

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="article_spider", charset="utf8")
cursor = conn.cursor()


def crawl_ips(page):
    # 爬取西刺的免费ip代理
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
    try:
        for i in range(1, page):
            list = []
            print(i)
            re = requests.get("http://www.xicidaili.com/nn/{0}".format(i), headers=headers)
            selector = Selector(text=re.text)
            ip_select = selector.xpath("//*/tr/td[2]").extract()
            port_select = selector.xpath("//*/td[3]").extract()
            for x in range(len(ip_select)):
                ip = ip_select[x][5: -5]
                port = port_select[x][5:-5]
                list.append((ip, port))
            # print(list)
            for x in list:
                cursor.execute(
                    "insert ip(ip, port) VALUES('{0}', {1})".format(x[0], x[1])
                )
                conn.commit()
            del list[:]

            time.sleep(1)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    crawl_ips(1500)

