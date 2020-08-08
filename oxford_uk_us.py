# content: come on !  
# author:    十六
# date:    2020/8/7

import requests
import re


# oxford 英音 and 美音
def oxford_uk_us(word):
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.105 Safari/537.36"}

    inp_url = "https://www.oxfordlearnersdictionaries.com/definition/english/" + word

    response = requests.get(url=inp_url, headers=headers).text
    ex = '<div class=".*?mp3="(.*?)" data-src-ogg.*?</div> '
    m = re.findall(ex, response, re.S)
    print(m)
    for url in m:
        if "uk" in url:
            oxford_uk = requests.get(url=url).content
            path_uk = word + " ox_uk.mp3"
            with open(path_uk, "wb") as opw_uk:
                opw_uk.write(oxford_uk)
        else:
            oxford_us = requests.get(url=url).content
            path_us = word + " ox_us.mp3"
            with open(path_us, "wb") as opw_us:
                opw_us.write(oxford_us)

    print("{} ox_uk.mp3和{} ox_us.mp3 下载完成".format(word,word))


while True:
    word = input("输入单词：")
    if word == "q":
        break
    else:
        oxford_uk_us(word)


