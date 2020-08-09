#  re模块相关函数 match与search

'''
re.match() 函数
    + 从头开始匹配
    + 要么第一个就符合要求，要么不符合
    + 匹配成功则返回Match对象，否则返回None
    + 可以使用group()方法获取返回的数据
    + 可以使用span()方法获取匹配的数据的下标区间

re.search()
    + 从字符串开头到结尾进行搜索式匹配
    + 匹配成功则返回Match对象，否则返回None
    + 可以使用group()方法获取返回的数据
    + 可以使用span()方法获取匹配的数据的下标区间

search() 和 match() 方法的区别：
    match()方法是从字符串的开头进行匹配，如果开始就不符合正则的要求，则匹配失败，返回None
    search()方法是从字符串的开始位置一直搜索到字符串的最后，如果在整个字符串中都没有匹配到，则失败，返回None


'''

import re
# 定义字符串
vars = 'iloveyou521tosimida'
# 定义正则表达式
reg = 'love'

# search
res = re.search(reg,vars)
print(res)
print(res.group())
print(res.span())

# 调用正则 match 函数方法
# res = re.match(reg,vars)
# print(res.group())  # 获取返回的数据结果
# print(res.span())   # 获取匹配结果的下标区间
