import requests
from lxml import etree


# 封装类。进行学习猿地的登录和订单的获取
class LMonKey():
    # 登录请求地址
    loginurl = 'https://www.lmonkey.com/login'
    # 账户中心地址
    orderurl = 'https://www.lmonkey.com/my/order'
    # 请求头header
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    # 请求对象
    req = None
    # token口令
    token = ''
    # 订单号
    ordercode = 0


    # 初始化方法
    def __init__(self):
        # 请求对象的初始化
        self.req = requests.session()
        if self.getlogin():
            if self.postlogin():
                self.getorder()

    # get 登录页面 获取_token
    def getlogin(self):
        # 1。get请求 login页面，设置cookie，获取_token
        res = self.req.get(url=self.loginurl,headers=self.headers)
        if res.status_code == 200:
            print('get登录页面请求成功')
            html = etree.HTML(res.text)
            self.token = html.xpath('//input[@name="_token"]/@value')[0]
            print('token获取成功')
            return True
        else:
            print('请求错误')

    # post 请求登录 设置cookie
    def postlogin(self):
        uname = input('手机号：')
        passw = input('密码：')
        data = {
            '_token':self.token,
            'username':uname,
            'password':passw
        }
        # 发起post请求
        res = self.req.post(url=self.loginurl,headers=self.headers,data=data)
        if res.status_code == 200 or res.status_code == 302:
            print('登录成功')
            # 请求订单数据
            return True

    # get 请求账户中心 获取默认订单号
    def getorder(self):
        # 3。get请求 账户中心，获取默认订单号
        res = self.req.get(url=self.orderurl,headers=self.headers)
        if res.status_code == 200:
            print('账户中心请求成功,正在解析数据')
            html = etree.HTML(res.text)
            r = html.xpath('//div[@class="avatar-content"]//small/text()')
            print(r)
            self.ordercode = r



obj = LMonKey()







