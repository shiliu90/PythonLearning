import requests,json
from lxml import etree

class Yq():
    # 请求的地址 猿著
    url = 'https://www.lmonkey.com/essence'

    # 请求头header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    # 爬取的数据
    data = ''
    # 存储数据
    filepath = './yq.json'

    # 初始化
    def __init__(self):
        # 发送请求
        res = requests.get(url = self.url,headers = self.headers)
        if res.status_code == 200:
            print('数据请求成功，正在写入')
            # 请求的内容写入文件
            with open('./yq.html','w') as fp:
                fp.write(res.text)
            if self.pasedata():
                self.writedata()

    # 解析数据
    def pasedata(self):
        print('解析数据')
        # 解析数据
        html = etree.parse('./yq.html', etree.HTMLParser())

        # 提取数据 作者 文章标题 文章地址url
        authors = html.xpath('//div[contains(@class,"old_content")]//div[contains(@class,"list-group-item-action")]//strong/a/text()')
        titles = html.xpath('//div[contains(@class,"old_content")]//div[contains(@class,"list-group-item-action")]//div[contains(@class,"flex-fill")]//div/text()')
        titleurl = html.xpath('//div[contains(@class,"old_content")]//div[contains(@class,"list-group-item-action")]//div[contains(@class,"flex-fill")]/a/@href')

        # 整理数据
        data = []
        for i in range(0,len(authors)):
            res = {'author':authors[i],'title':titles[i],'url':titleurl[i]}
            data.append(res)
        self.data = data
        return True

    #写入数据
    def writedata(self):
        print('写入数据')
        with open(self.filepath,'w') as fp:
            json.dump(self.data,fp)


# 实例化对象
Yq()