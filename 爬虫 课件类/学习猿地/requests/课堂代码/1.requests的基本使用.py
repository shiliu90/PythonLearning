import requests

# 定义请求的url
url = 'https://www.baidu.com/'

# 发起get请求
res = requests.get(url=url)

# 获取响应结果
print(res)  # <Response [200]>
print(res.status_code) # 请求状态码 200
print(res.content) # b'....' 二进制的文本流
# print(res.content.decode('utf-8')) # 把二进制的文本流按照utf8的字符集转化为普通字符串
print(res.text) # 获取响应的内容
print(res.url)  # 请求的url地址
print(res.request.headers) # 请求的头信息 {'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
print(res.headers) # 响应头信息 {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'Keep-Alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Sat, 09 Nov 2019 07:03:19 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:23:55 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}




