#
'''
re.findall()
    + 按照正则表达式的规则在字符中匹配所有符合规则的元素，结果返回一个列表，如果没有找到则返回空列表

re.finditer()
    + 按照正则表达式的规则在字符中匹配所有符合规则的元素，返回一个迭代器

re.sub() 搜索替换
    + 按照正则表达式的规则，在字符串中找到需要 被替换的字符串，完成一个替换
参数：
    pattern： 正则表达式的规则，匹配需要被替换的字符串
    repl：    替换后的字符串
    string：  被替换的原始字符串

compile()
    可以直接将正则表达式定义为 正则对象，使用正则对象直接操作

'''

import re

# 定义字符串
varstr = 'iloveyou521tosimida511'

# 正则表达式
reg = '\d{3}'
# 函数调用
# res = re.findall(reg,varstr)
# res = re.finditer(reg,varstr)
# print(list(res))

# 找到数字，替换成其它
# res = re.sub(reg,'AAA',varstr)
# print(res)

# 直接定义正则表达式对象
reg = re.compile('\d{3}')
# 直接使用创建的正则对象，去调用对应的方法或函数
res = reg.findall(string=varstr)
# print(res)

lines = [
    'i love 512 you',
    'i love 521 you',
    'i love 345 you',
    'i love 543 you',
]

reg = re.compile('\d{3}')
for i in lines:
    # reg = '\d{3}'
    # res = re.search(reg,i)
    # print(res.group())

    res = reg.search(i).group()
    print(res)




