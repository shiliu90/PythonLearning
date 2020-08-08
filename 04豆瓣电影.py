# content: come on !  
# author:    十六
# date:    2020/8/5

import requests
import json

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list"
    dic = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.100 Safari/537.36', }

    response = requests.get(url=url, params=dic, headers=headers)
    list_data = response.json()

    fp = open("./text/doupan.json", 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print("over")


