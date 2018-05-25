#!/usr/bin/env python3
#-*- coding=utf-8 -*-
import requests
import re
import traceback
from requests import exceptions
f=open('ip.txt','a', encoding='UTF-8', errors='ignore')
def checkAvailable(ip,port,type):
    try:
        proxies = {}
        proxies[type]=type+'://'+ip+':'+port
        url='https://blog.csdn.net/'
        #url='http://www.jrj.com.cn/'
        print(proxies)
        r =requests.get(url, proxies=proxies, timeout=3)
        print(r)
        if r.status_code==200:
            f.write(ip+'&'+proxies.get(type)+'\n')
            print("ok")
    except :
         traceback.print_exc()
    finally:
        pass
def closeFile():
    f.close()
def getIP(endpage):
    for i in range(1,endpage):
        try:
            url = "https://www.kuaidaili.com/free/inha/"+str(i)+"/"
            r=requests.get(url,timeout=10)
            list1=re.findall(r'(?<=IP\">).*?(?=<)',r.text,re.S)
            list2=re.findall(r'(?<=PORT\">).*?(?=<)',r.text,re.S)
            list3=re.findall(r'(?<=类型\">).*?(?=<)',r.text,re.S)
            for j in range(len(list1)):
                checkAvailable(list1[j],list2[j],list3[j].lower())
            print('第'+str(i)+'页结束，状态码='+str(r))
        except :
            traceback.print_exc()
        finally:
             pass
def main():
    print("开始...")
    getIP()
    closeFile()
    print("结束")
main()