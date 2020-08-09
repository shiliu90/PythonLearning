# 。学习猿地-猿圈

'''
分析爬取的数据
数据源地址： https://www.lmonkey.com/t
数据内容： 文章标题，文章的链接，作者，发布时间
工具：
    python，requests,bs4，json
'''

import requests,json
from bs4 import BeautifulSoup

# 1。定义请求的URL和请求头
url = 'https://www.lmonkey.com/t'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

# 2。发送请求
res = requests.get(url,headers=headers)

# 3。判断请求是否成功，并获取请求的源代码
if res.status_code == 200:

    # 4。解析数据
    soup = BeautifulSoup(res.text,'lxml')
    # 获取页面中所有的文章
    divs = soup.find_all('div',class_="list-group-item list-group-item-action p-06")
    varlist = []
    for i in divs:
        r = i.find('div',class_="topic_title")
        if r:
            vardict = {
                'title':r.text.split('\n')[0],
                'url':i.a['href'],
                'author':i.strong.a.text,
                'pubdate':i.span['title']
            }
            varlist.append(vardict)
    # print(varlist)
    # 5。写入数据
    with open('./yq.json','w') as fp:
        json.dump(varlist,fp)
