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



# 封装类
class Bs4Yq():
    # 定义属性
    # 请求的url
    url = 'https://www.lmonkey.com/t'
    # 请求头
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }

    # 响应源代码的存放位置
    res_html = None

    # 存储解析后的数据
    varlist = []

    # 初始化方法
    def __init__(self):
        # 发起一个请求
        res = requests.get(self.url,headers = self.headers)
        if res.status_code == 200:
            self.res_html = res.text
            if self.ParseData():
                self.WriteJson()
                print('请求成功，数据写入文件')
        else:
            print('请求失败')

    # 解析html数据
    def ParseData(self):
        soup = BeautifulSoup(self.res_html, 'lxml')
        try:
            # 获取页面中所有的文章
            divs = soup.find_all('div', class_="list-group-item list-group-item-action p-06")
            for i in divs:
                r = i.find('div', class_="topic_title")
                if r:
                    vardict = {
                        'title': r.text.split('\n')[0],
                        'url': i.a['href'],
                        'author': i.strong.a.text,
                        'pubdate': i.span['title']
                    }
                    self.varlist.append(vardict)
            return True
        except:
            return False

    # 写入json数据
    def WriteJson(self):
        if self.varlist != []:
            try:
                with open('./yq.json', 'w') as fp:
                    json.dump(self.varlist, fp)
                return True
            except:
                return False
        else:
            print('无法获取当前解析的数据')
            return False



Bs4Yq()





