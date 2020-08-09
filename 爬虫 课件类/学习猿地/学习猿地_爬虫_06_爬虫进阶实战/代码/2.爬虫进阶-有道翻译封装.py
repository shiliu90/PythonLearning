
import requests

# 封装翻译的函数
def fanyi(kw):
    # 定义请求的url
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 定义请求的参数
    data = {
        'i': kw,
        'doctype': 'json'
    }
    # 发起请求 post
    res = requests.post(url, data=data)
    # 查看请求结果，
    code = res.status_code
    if code == 200:
        # 解析数据
        # print(res.content)
        # print(res.json())  # 如果返回的是json数据，可以直接解析
        resdata = res.json()
        if resdata['errorCode'] == 0:
            # 请求成功
            print(resdata['translateResult'][0][0]['tgt'])
    else:
        print('翻译请求失败，请联系管理员')



vars = """
 *********************
 ** 欢迎使用py翻译工具 **
 ** 输入需要翻译的内容 **
 ** 输入字母 q 则退出  **
 *********************    
 """
print(vars)

while True:
    # 获取用户的输入内容
    keyword = input('输入需要翻译的内容：')
    # 判断是否需要退出
    if keyword == 'q':
        break
    # 调用函数，进行翻译
    fanyi(keyword)
