# content: come on !  
# author:    十六
# date:    2020/8/6


import requests
import json

if __name__ == "__main__":
    address = input('请输入地址：')
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    data = {
        'cname': '',
        'pid': '',
        'keyword': address,
        'pageIndex': '1',
        'pageSize': '10'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.100 Safari/537.36', }

    response = requests.post(url=url, data=data, headers=headers)
    print(response.text)
    list_data = response.json()
    print(list_data)

    fp = open("text/YC.json", 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print("over")


