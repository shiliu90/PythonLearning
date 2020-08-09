'''

当频繁请求一个网站时，对方会认为攻击或者盗取数据，禁用ip是反制的有效手段。
如何破解这个问题？

1。推荐方案 就是降低爬虫请求的频率，不要对别人的服务器造成压力。
2。使用代理IP

'''

import requests


# 定义请求的url
url = 'http://httpbin.org/get'
# 定义请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
}
# 定义代理ip
proxies = {
    'http':'110.243.8.252:9999',
    'https':'110.243.8.252:9999',
}
try:
    # 发起get请求
    res = requests.get(url,headers=headers,proxies=proxies,timeout=5)
    # 检测请求状态
    if res.status_code == 200:
        # 获取响应内容
        data = res.json()
        print(data['origin'].split(',')[0])
except:
    print('请求失败')
