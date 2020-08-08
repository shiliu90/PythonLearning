# content: come on !  
# author:    十六
# date:    2020/8/5

#   需求： 爬取搜狗首页的页面数据

import requests

if __name__ == "__main__":
    # step 1: 指定 url
    url = "https://www.sogou.com/"
    # step 2: 发起请求  get 方法会返回一个响应对象
    response = requests.get(url=url)
    # step 3：获取响应数据
    page_text = response.text  # text 是字符串数据
    # step 5: 持久储存
    with open('sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束")

