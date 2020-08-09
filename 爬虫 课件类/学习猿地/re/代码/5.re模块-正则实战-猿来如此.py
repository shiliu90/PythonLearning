
'''

数据地址：https://www.lmonkey.com/ask
数据字段： 问题，时间，url,作者
'''


import requests,re,json

# 1.定义请的url和请求头
url = 'https://www.lmonkey.com/ask'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

# 2.发起请求
res = requests.get(url,headers=headers)

# 3.检测请求是否成功
if res.status_code == 200:
    # 4.获取返回的数据，
    res_html = res.text

    # 5。 进行数据解析

    # 定义解析问题标题的正则
    reg = '<div class="topic_title mb-0 lh-180 ml-n2">(.*?)<small'
    titlelist = re.findall(reg,res_html)
    # 定义解析作者的正则
    reg = '<strong>(.*?)</strong>'
    authorlist = re.findall(reg,res_html)
    # 定义解析时间的正则
    reg = '<span data-toggle="tooltip" data-placement="top" title="(.*?)">'
    datelist = re.findall(reg,res_html)
    # 定义解析url的正则
    reg = '<a href="(https://www.lmonkey.com/ask/\d+)" target="_blank">'
    urllist = re.findall(reg,res_html)
    # 压缩数据
    data = list(zip(titlelist,authorlist,datelist,urllist))

    # 常规方式 处理 数据，[{},{},{}]
    # datalist = []
    # for i in data:
    #     res = {'title':i[0],'url':i[1],'author':i[2],'datetime':i[3]}
    #     datalist.append(res)

    # 列表推导式
    datalist = [{'title':i[0],'url':i[1],'author':i[2],'datetime':i[3]} for i in data]

    # 数据入库
    with open('./data.json','w',encoding='utf-8') as fp:
        json.dump(datalist,fp)





