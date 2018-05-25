import requests
import re
import time


def get_one_page(url):
    headers = {'Host': 'maoyan.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def main(offset):
    global aaa
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    # print(html)
    list = re.findall('(?<=title=\").+?(?=\" class)', html)
    list1 = re.findall('(?<=<p class=\"star\">).+?(?=</p>)', html, re.S)
    a = 0
    for i in list:
        print("no" + str(aaa + 1) + ":" + i + "  " + str.strip(list1[a]))
        a = a + 1

        aaa = aaa + 1


print('开始。。。。')
aaa = 0;
for i in range(10):
    main(offset=i * 10)
    time.sleep(1)
print('结束')   