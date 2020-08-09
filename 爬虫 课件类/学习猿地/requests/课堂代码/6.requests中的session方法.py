import requests

# 需要请求的目标地址
url = 'http://www.zmz2019.com/user/user'

# 登录请求的地址
loginurl = 'http://www.zmz2019.com/User/Login/ajaxLogin'

# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

# 如果需要爬虫程序主动记录cookie并且携带cookie，那么在使用requests之前先调用session方法
# 并且使用session方法返回的对象发送请求即可
req = requests.session()

# 登录请求时的数据
data = {
'account': 'yichuan@itxdl.cn',
'password': 'pyTHON123',
'remember': '1',
'url_back': 'http://www.zmz2019.com/user/user'

}
# 发起登录请求
res = req.post(url=loginurl,headers=headers,data=data)

# 判断状态
code = res.status_code
print(code)

if code == 200:
    # 发起新的请求，去获取目标数据
    res = req.get(url=url,headers=headers)
    with open('rr.html','w') as fp:
        fp.write(res.text)


# 思考作业：
'''
1。session()起到的作用
2。去思考如何用这样的思路去完成 学习猿地 的登录 （能写出思路即可）
'''