# coding:utf-8
import os
from urllib import parse
import chardet
import requests
from faker import Faker
from bs4 import BeautifulSoup

# url = 'https://www.cnblogs.com/lei0213/p/6099008.html'
# base_url = 'https://www.cnblogs.com'

# url = 'http://sklearn.apachecn.org/cn/0.19.0/'
# base_url = 'http://sklearn.apachecn.org/'

url = 'http://www.w3school.com.cn/cssref/css_selectors.asp'
base_url = 'http://www.w3school.com.cn/'


# url = 'https://www.jianshu.com/c/V2CqjW?utm_medium=index-collections&utm_source=desktop'
# base_url = 'https://www.jianshu.com/'

headers = {
    'User-Agent': Faker().firefox()
}


def clean():
    for filename in os.listdir('style/'):
        os.remove(os.path.join('style/', filename))

    for filename in os.listdir('html/'):
        os.remove(os.path.join('html/', filename))


def get_html(url):
    response = requests.get(url=url, headers=headers)
    text = response.content   # response.text 返回的是unicode  response.content返回的是bytes
    coding = chardet.detect(text)['encoding']
    return BeautifulSoup(text.decode(coding), 'lxml')


def download(url, save_folder):
    filename = parse.urlparse(url).path.split('/')[-1]

    try:
        with open(os.path.join(save_folder, filename), 'wb') as fp:
            fp.write(requests.get(url=url, headers=headers).content)
    except Exception as e:
        print(e)

    print('download {} success'.format(filename))


def main():
    obj = get_html(url)
    for row in obj.select('script[src],img[src],link[href]'):
        key = 'src' if 'src' in row.attrs else 'href'
        path = row[key]
        src_url = parse.urljoin(base_url, path)
        filename = parse.urlparse(src_url).path.split('/')[-1]
        row[key] = '../style/' + filename
        download(src_url, 'style')

    with open('html/home.html', 'wb') as fp:
        fp.write(obj.prettify().encode('utf-8'))


if __name__ == '__main__':
    # TODO 爬虫被禁 数据无法抓取  （暂时解决）
    # TODO 下载重试
    # TODO ajax加载页面如何拖动滚动条

    clean()
    main()
