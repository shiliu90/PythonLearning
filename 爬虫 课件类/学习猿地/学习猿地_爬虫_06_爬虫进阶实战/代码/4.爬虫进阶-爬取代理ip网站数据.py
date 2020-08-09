# 。爬取代理ip数据


import requests
from lxml import etree


# 定义请求头
url = 'https://www.xicidaili.com/nn/'
# 定义请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
}
#发起请求
res = requests.get(url,headers=headers)
# 判断请求状态
if res.status_code == 200:
    # 获取响应数据
    response = res.content.decode('utf-8')
    # 使用XPATH解析html数据
    res_html = etree.HTML(response)
    ips = res_html.xpath('//table[@id="ip_list"]//tr//td[2]/text()')
    ports = res_html.xpath('//table[@id="ip_list"]//tr//td[3]/text()')
    data = list(zip(ips,ports))
    print(len(data))

    # 剩下的就是需要 验证当前这些个ip是否正常好用

