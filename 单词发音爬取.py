# author: "十六"
import requests


# 百度翻译 -- 英音
def bd_uk(word):
    global res_con_uk
    url_uk = "https://fanyi.baidu.com/gettts?lan=uk&text=" + word + "&spd=3&source=web"

    parameter_uk = {
        'lan': 'uk',
        'text': word,
        'spd': '3',
        'source': 'web'}

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52 "}

    try:
        res = requests.get(url=url_uk, params=parameter_uk, headers=headers)
        res.raise_for_status()
        res_con_uk = res.content
    except Exception:
        print("异常")

    path_name_uk = "./mp3/" + word + " bd_uk.mp3"
    with open(path_name_uk, "wb") as opw:
        opw.write(res_con_uk)
    print("{} bd_uk已经保存完毕!!".format(word))


# 百度翻译 -- 美音
def bd_en(word):
    global res_con_en
    url_en = "https://fanyi.baidu.com/gettts?lan=en&text=" + word + "&spd=3&source=web"

    parameter_en = {
        'lan': 'en',
        'text': word,
        'spd': '3',
        'source': 'web'}

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52 "}

    try:
        res = requests.get(url=url_en, params=parameter_en, headers=headers)
        res.raise_for_status()
        res_con_en = res.content
    except Exception:
        print("异常")

    path_name_en = "./mp3/" + word + " bd_en.mp3"
    with open(path_name_en, "wb") as opw:
        opw.write(res_con_en)
    print("{} bd_en已经保存完毕!!".format(word))


# 有道翻译 -- 英音
def yd_uk(word):
    global res

    parameter_uk = {
        'audio': word,
        "type": "1"}
    url_uk = "http://dict.youdao.com/dictvoice"

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52 "}

    try:
        res_ul = requests.get(url=url_uk, params=parameter_uk, headers=headers, stream=True)
        res_ul.raise_for_status()
        url = res_ul.url
        res = requests.get(url=url).content
    except Exception:
        print("异常")

    path_name_uk = "./mp3/" + word + " yd_uk.mp3"
    with open(path_name_uk, "wb") as opw:
        opw.write(res)
    print("{} yd_uk已经保存完毕!!".format(word))


# 有道翻译 -- 美音
def yd_en(word):
    global res

    parameter_en = {
        'audio': word,
        "type": "2"}

    url_en = "http://dict.youdao.com/dictvoice"

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52 "
    }

    try:
        res_ul = requests.get(url=url_en, params=parameter_en, headers=headers, stream=True)
        res_ul.raise_for_status()
        url = res_ul.url
        res = requests.get(url=url).content
    except Exception:
        print("异常")

    path_name_en = "./mp3/" + word + " yd_en.mp3"
    with open(path_name_en, "wb") as opw:
        opw.write(res)
    print("{} yd_en已经保存完毕!!".format(word))


# 欧路词典 -- 英音
def ol_uk(word):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52 "}
    input_url = "https://dict.eudic.net/dicts/en/" + word

    web_text = requests.get(input_url, headers=headers).text
    f_mun = web_text.find("voice-js voice-button voice-button-en")
    web_tet = web_text[f_mun:f_mun + 280]
    fist_num = web_tet.find("=") + 1
    last_num = web_tet.find(">")
    # 参数并转换
    params = web_tet[fist_num:last_num].replace("amp;", "")
    # 构建下载链接
    url = "https://api.frdic.com/api/v2/speech/speakweb?" + eval(params)
    # 得到mp3数据
    res_ol_uk = requests.get(url=url).content
    path_name_uk = "./mp3/" + word + " ol_uk.mp3"
    with open(path_name_uk, "wb") as opw:
        opw.write(res_ol_uk)
    print("{} ol_uk已经保存完毕!!".format(word))


# 欧路词点 - 美音
def ol_en(word):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52 "}
    input_url = "https://dict.eudic.net/dicts/en/" + word

    web_text = requests.get(input_url, headers=headers).text
    f_mun = web_text.rfind("voice-js voice-button voice-button-en")
    web_txt = web_text[f_mun:f_mun + 180]
    fist_num = web_txt.find("=") + 1
    last_num = web_txt.find(">")
    # 得到参数
    params = web_txt[fist_num:last_num].replace("amp;", "")
    # 构建下载链接
    url = "https://api.frdic.com/api/v2/speech/speakweb?" + eval(params)
    res_ol_en = requests.get(url=url).content
    path_name = "./mp3/" + word + " ol_en.mp3"
    with open(path_name, "wb") as opw:
        opw.write(res_ol_en)
    print("{} ol_en单词下载成功".format(word))


while True:
    input_word = input("输入单词:____(输入'q'退出循环)")
    if input_word == "q":
        break
    else:
        bd_uk(input_word)
        bd_en(input_word)
        yd_uk(input_word)
        yd_en(input_word)
        ol_uk(input_word)
        ol_en(input_word)
