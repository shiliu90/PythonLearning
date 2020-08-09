from lxml import etree

text = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>学习猿地 - 成就自己的只需一套精品</title>
</head>
<body>
    <ul>
        <li><a href="/a/b/c/java/">java工程师</a></li>
        <li><a href="/a/b/c/python/">python工程师</a></li>
        <li><a href="/a/b/c/ai/">AI工程师</a></li>
    </ul>
</body>
</html>
'''


#第一种方式，读取⼀个html⽂件并解析

# 使用etree解析html字符串
html = etree.HTML(text)

# 提取数据
r = html.xpath('/html/body/ul/li/a/text()')
# ['java工程师', 'python工程师', 'AI工程师']
# print(r)

r = html.xpath('/html/body/ul/li[1]/a/text()')
# print(r)  #['java工程师']


#第二种方式，读取⼀个html⽂件并解析
html = etree.parse('./test.html', etree.HTMLParser())
# print(html)

# 提取数据
r = html.xpath('/html/body/ul/li/a/text()')
print(r)