import requests
from lxml import etree

def get_data():
    page = requests.get("http://support.i-search.com.cn/")
    html = page.text
    selector = etree.HTML(html)
    topic_list = selector.xpath("//div[@class='module']//h2/a/text()")
    for x in topic_list:
        print(x.split())


if __name__ == "__main__":
    get_data()
