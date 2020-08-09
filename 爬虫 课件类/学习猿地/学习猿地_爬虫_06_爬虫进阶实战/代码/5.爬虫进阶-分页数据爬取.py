# 。分页数据爬出

import requests
import time
import json
from lxml import etree


# 页面请求函数
def getPage(url):
    # 定义请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
    }
    # 发起请求
    res = requests.get(url, headers=headers)
    # 判断请求状态
    if res.status_code == 200:
        # 获取响应数据
        response = res.content.decode('utf-8')
        return response
    else:
        return False



# 解析页面html的数据
def parseHTML(html):
    try:
        # 使用XPATH解析html数据
        res_html = etree.HTML(html)
        ips = res_html.xpath('//table[@id="ip_list"]//tr//td[2]/text()')
        ports = res_html.xpath('//table[@id="ip_list"]//tr//td[3]/text()')

        data = list(zip(ips, ports))
        # [(1,2),(1,2)] == [{1:2},{1:2}]
        data = [{i[0]:i[1]} for i in data]
        return data
    except:
        return False


# 测试ip是否好用
def testIp(ip):
    # 定义请求的url
    url = 'http://httpbin.org/get'
    # 定义请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
    }
    # 定义代理ip
    proxies = {
        'http': f'{ip[0]}:{ip[1]}',
        'https': f'{ip[0]}:{ip[1]}',
    }
    try:
        # 发起get请求
        res = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        # 检测请求状态
        if res.status_code == 200:
            # 获取响应内容
            # data = res.json()
            # print(data['origin'].split(',')[0])
            return True
        else:
            return False
    except:
        return False


# 主程序
def main(num):
    # 拼接url
    url = f'https://www.xicidaili.com/nn/{num}'
    # 调用请求页面的程序
    html = getPage(url)
    if html:
        # 调用解析html的方法
        alist = parseHTML(html)
        # data = []
        # for ip in alist:
        #     # 把返回的解析的数据，去发请求测试是否好用
        #     okip = testIp(ip)
        #     if okip:
        #         data.append(ip)

        # 把返回的好用的ip数据写入文件
        with open('./ipdata.json','a+') as fp:
            for i in alist:
                fp.write(json.dumps(i))
                fp.write('\n')



# 如果当前这个脚本是作为主程序使用，那么__name__的结果 就是 __main__
if __name__ == '__main__':
    for i in range(1,10):
        print(f'当前正在爬取第{i}页')
        main(i)
        # 每爬取一个页面后，停顿2秒
        time.sleep(2)

'''
分析：
url :
    https://www.xicidaili.com/nn/1  第一页
    https://www.xicidaili.com/nn/2  第二页
    https://www.xicidaili.com/nn/3  第三页
'''