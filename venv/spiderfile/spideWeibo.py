import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {'Host': 'm.weibo.cn', 'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest', }


def get_page(page):
    params = {'type': 'uid', 'value': '2830678474', 'containerid': '1076032830678474'  # 'page': page
              }
    url = base_url + urlencode(params)
    try:
        print(url)
        response = requests.get(url, headers=headers)
        # print(response.status_code)
        if response.status_code == 200:
            # print(response.json())
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    if json:
        list = json.get('data').get('cards')
        for i in list:

            # print(i)
            if i.get('mblog'):

                # print('text='+i.get('mblog').get('text'))
                soup = BeautifulSoup(i.get('mblog').get('text'), 'lxml')

                # print(soup.prettify())#格式化html标签
                # print(soup.find_all(name='img')[0])
                tag = soup.find(name='img')
                if tag:  # 判断not null
                    print("开始")
                    print(soup.find(name='img'))
                    print(soup.find(name='img').get("src"))  # 获取属性
                    print("结束")


parse_page(get_page(0))