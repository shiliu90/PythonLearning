import requests

# 定义请求的url
url = 'https://www.lmonkey.com/my/order'

# 定义请求头信息
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'cookie':'Hm_lvt_676e52e2eddd764819cab505b21e9ee8=1573357630; UM_distinctid=16e536c37bc234-0bd9595023c634-1c3c6a5a-13c680-16e536c37bd82b; CNZZDATA1277679765=592294367-1573357631-%7C1573357631; wechat_flag=eyJpdiI6IkszSEtaV3dOdmJYTXdsQkJYVmg2YkE9PSIsInZhbHVlIjoiOUdSWnpZVDVIbWRYTlR2WWo4WDJjRVQ5ZmNNUTJ6WklIaitndXA2YXNZR1o2Yk80ZEFoZGhPV3Zzbm9mbVNXZiIsIm1hYyI6Ijc3YTIwN2E4MWM1NDRkZDc4Y2E3NmYxMjJmODIwNDExNTEwNjM0YmZiZTJjOTA2MzQ1MGFhYTZjYjA1MzQzOWEifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IjE5UE5oeXNWTml4bFVDNFE3TmFVUmc9PSIsInZhbHVlIjoiN2tWSGk2b3NXbklDMGZFZUNlMVE2T2kzYUxHMkpjaFJSZkhcL2pFRVR3cDlDNTB5dVhrRVpHZkN6UDVpRUxlb3MiLCJtYWMiOiJjMmI4NjRjZWZhMmVhODAzNDQwOTA3YThiZTAyNzNlMThjNDAyYzc0MjgxYzQ2ZTllZjAwODJiZDQwMmUyYjJkIn0%3D; _session=eyJpdiI6IkM2WklsTytwbGxzTjR2bkNLdjhmNlE9PSIsInZhbHVlIjoieEdaRDFlOGJXU1FSRlpFeENXUzc5NGZrd3VndUlpOVZoM3RYTGlrNnh4K0NLNlVnWUUwVU9WYmdMWUhvNjBtciIsIm1hYyI6IjU2OTc1ZjBkODExMzA1OWU0Y2Y5OGQzZWVlYTUxZTZkZDVkNmY3OWU4ZmY0MTM3ZDBlZDM5Zjg1MDhhM2UzZDYifQ%3D%3D; Hm_lpvt_676e52e2eddd764819cab505b21e9ee8=1573358797'
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