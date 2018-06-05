#手机代理到mitmproxy上并且处于同一网络下，执行命令：mitmdump -s xxx.py
#拦截app请求打印headers，方法名字必须写成这个。
def request(flow):
    flow.request.headers['cache-control']='max-age=0'
    print('request信息开始...')
    print('request信息开始...')
    print('headers='+str(flow.request.headers))
    print('cookies='+str(flow.request.cookies))
    print('host='+str(flow.request.host))
    print('port='+str(flow.request.port))
    print('method='+str(flow.request.method))
    print('url='+str(flow.request.url))
    print('scheme='+str(flow.request.scheme))
    print('request信息结束')
    #flow.request.url='https://www.baidu.com/'  #重置请求URL,但是需要注意整个请求都要改动
#拦截app响应打印headers，方法名字必须写成这个。
def response(flow):
    print('response信息开始...')
    print('status_code='+str(flow.response.status_code))
    print('headers='+str(flow.response.headers))
    print('cookies='+str(flow.response.cookies))
    print('text='+str(flow.response.text))
    print('response信息结束')