import requests

# 定义请求的url
# url = 'https://www.lmonkey.com/'
url = 'https://www.xicidaili.com/nn'

# 定义请求头信息
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

# 发起get请求
res = requests.get(url=url,headers=headers)

# 获取响应状态码
code = res.status_code
print(code)

# 响应成功后把响应的内容写入文件中
if code == 200:
    with open('./test.html','w') as fp:
        fp.write(res.text)