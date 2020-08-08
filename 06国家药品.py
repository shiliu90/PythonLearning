# content: come on !  
# author:    十六
# date:    2020/8/6

import requests
import json

# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/69.0.3497.100 Safari/537.36', }
# 网页分析得到的 url
url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList"
# 为了添加所有 id 的空列表
id_lists = []
# 为了保存数据的 空列表
all_data_list = []

# 循环页数(前5页的数据，range(1,6) 来改变页数
for page in range(1,6):
    # 把页数转为标签
    page = str(page)
    # 参数设置 注意有变量
    data = {'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': ''}
    # 得到json 数据 -- 字典型数据类型
    res_json = requests.post(url=url, data=data, headers=headers).json()
    print(type(res_json))
    # 循环字典里 key(list) 提取里面的列表循环
    for dic in res_json["list"]:
        # 把字典里 Key["ID"] 的value 添加到空列表中
        id_lists.append(dic["ID"])
# 分析得到的url
url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById"
# 循环 每个ID
for id in id_lists:
    # 参数为 ID
    kw = {
        'id': id
    }
    # 请求数据
    res_json1 = requests.post(url=url, data=kw, headers=headers).json()
    # 把得到的数据 写入到 空列表中
    all_data_list.append(res_json1)

# 存储为.json 格式
fp = open('./all_data.json', 'w', encoding='utf-8')
# 把数据 转为json格式 （dump)
json.dump(all_data_list, fp=fp, ensure_ascii=False)

print('over')
