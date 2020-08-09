from lxml import etree


# 解析html文件
html = etree.parse('./test.html', etree.HTMLParser())

# 提取数据

# r = html.xpath('/html/body/ul/li/a/text()')
# print(r)

# 获取页面中所有的li里面的数据
# r = html.xpath('//li/a/text()')
# print(r)

# 获取指定标签里面的li数据
t = html.xpath('//div[@class="teacher"]//li/a/text()')
# print(t)
h = html.xpath('//div[@class="teacher"]//li/a/@href')
# print(h)

res = list(zip(t,h))
print(res)

#
'''
/ 当前元素的直接子节点
// 当前元素的子节点或孙子节点

text() 获取文本
@attr 获取属性对应的值
'''


