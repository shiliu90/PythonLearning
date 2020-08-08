# content: come on !  
# author:    十六
# date:    2020/8/5

#   - 需求：爬取搜狗指定词条对应的搜索结果页面（简易网页采集器） UA检测
#   这里  需要加上 UA伪装 US:User-Agent(请求网页载体的身份标识）
#   一定要使用 UA伪装
import requests

if __name__ == "__main__":
    # 将UA伪装： 将对应的user-agent 封装到一个字典中
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.105 Safari/537.36"}

    # url 后的参数 单独提取出。
    url = "https://www.sogou.com/web"
    # 处理 url携带的参数：封装好字典中。与get请求相对应
    kw = input("请输入要搜索的名字")
    param = {
        "query": kw}

    # params= 就是对应 url的参数。 headers = UA伪装
    response = requests.get(url=url, params=param, headers=headers)

    # 得到响应数据
    page_text = response.text

    file_name = kw + '.html'
    path = "./text/" + file_name

    with open(path, 'w', encoding="utf-8") as fp:
        fp.write(page_text)
    print(file_name, "数据完成！")





