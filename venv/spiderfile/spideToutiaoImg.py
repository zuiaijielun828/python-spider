import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import json
import re
import time
import random

base_url = 'https://www.toutiao.com/search_content/?'
headers = {
    'Referer': 'https://www.toutiao.com/search',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
count=1
iplist=[]
listurl=set()
def get_page(page):
    params = {
        'offset': page,
        'format': 'json',
        'keyword': '风景图片',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab'
    }
    url = base_url + urlencode(params)
    try:
        #print(url)
        response = sendget(url)
        #print(response.status_code)
        if response.status_code == 200:
            json_dicts=json.dumps(response.json(),indent=4)
            #print(json_dicts)
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)
def parse_page(jsons):
    response=''
    for i in jsons.get("data"):
        if i.get("item_source_url") :
            imgurl="https://www.toutiao.com"+i.get("item_source_url")
            #print(imgurl)
            response = sendget(imgurl)
            aaa=re.findall(r'http:.*?pgc-image\\\\.*?(?=\\\")',response.text)
            for j in aaa:
                j=re.sub(r'\\','',j)
                listurl.add(j)

def download():
    for url in listurl:
        response =sendget(url,qtype='img')
        if response:
            with open(url[-23:]+'.jpg', 'wb') as f:
                f.write(response.content)
                print(url[-23:]+'.jpg下载成功')

def sendget(url,qtype=''):
    response=''
    try:
        global count
        proxies={}
        if count==len(iplist):
            count=0
        htype='http'
        if iplist[count][4]=='s':
            htype='https'
        count=random.randint(0,len(iplist))
        if count==len(iplist):
            count=random.randint(0,len(iplist))
        proxies[htype]=iplist[count]
        print(url)
        host=re.findall(r'(?<=http://).*?(?=/)',url)
        if not host:
             host=re.findall(r'(?<=https://).*?(?=/)',url)
        host1=str(host)
        host1=host1[2:-2]
        headers['Host']=host1
        if(qtype=='img'):
            response=requests.get(url,headers=headers,timeout=5)
        else:
            response=requests.get(url,headers=headers,proxies=proxies,timeout=5)
        print(response)
        #time.sleep(random.randint(5,6))
    except :
        print('发生错误！！！')
    return response

def execute():
    for i in range(0,100):
        print('第'+str(i)+'页开始')
        parse_page(get_page(20*i))
        download()
        #time.sleep(1)
        print('第'+str(i)+'页结束')
def readip():
    file=open('ip.txt')
    for line in file:
        if line.strip():
            iplist.append(line.split('&')[1].lower()[:-1])
    file.close()
def main():
    readip()
    execute()
main()
