import urllib.request
from lxml import etree
import ssl
from PIL import Image
import urllib
import io
import time


def get_url_list(pages):
    context = ssl._create_unverified_context()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    y = 2483
    for x in range(11, pages):
        web_url = 'https://www.732ee.com/htm/piclist8/' + str(x) + '.htm'
        print(web_url)
        first_request = urllib.request.Request(web_url, headers=headers)
        # first_request = str(first_request)
        response = urllib.request.urlopen(first_request, context=context)
        html = response.read()
        selector = etree.HTML(html)
        # pprint.pprint(response.read())
        urls_list = selector.xpath('//*[@class="textList"]/li/a/@href')
        # print(urls_list)
        urls = []
        for url in urls_list:
            url = 'https://www.732ee.com' + url
            urls.append(url)

        for url in urls:
            print(url)
            time.sleep(2)
            second_request = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(second_request, context=context)
            html = response.read()
            selector = etree.HTML(html)
            pic_list = selector.xpath('//*[@class="picContent"]/img/@src')
            # print(pic_list)
            # number = 1
            for pic_url in pic_list:
                dir_name = '/Users/futeen/stockings_pic/' + str(y) + '.jpg'
                print(dir_name)
                request = urllib.request.Request(pic_url, headers=headers)
                response = urllib.request.urlopen(request, context=context)
                pic = response.read()
                img = Image.open(io.BytesIO(pic))
                img.save(dir_name)
                y += 1
                time.sleep(2)


if __name__ == '__main__':
    get_url_list(30)

