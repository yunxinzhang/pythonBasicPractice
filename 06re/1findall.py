# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 18:05:20 2018

@author: zyx
"""
# ctrl + shift + i ---> help(fun) (spider)
lan = "  _1c|2c++|3java|4python|5js|6ruby|7swift|8go|9c#|10sql|11perl|12cypher"

# 用 index， in
print("python" in lan)
print(lan.index("python"))


import re

#寻找常量
r = re.findall("j",lan)
print(r)

#寻找规则
#元字符  “\d"
number = re.findall("\d",lan)
print(number)
chars = re.findall("\D",lan)
print(chars)

# 特殊字符在正则表达式中要小心
# ^ 取反
# [] 或
# - 范围
# \d 数字
# \D 非数字
# \w 数字和字符 _
# \s 空白字符
chos = re.findall("[jv]a",lan)
spch = re.findall("c[^a-zA-Z]",lan)
cn   = re.findall("\w", lan)
cnw   = re.findall("\W", lan)
la = re.findall("[a-z]{2,}", lan)

# 非贪婪 ?
gr = re.findall("[a-z]{3,4}?",lan)


#边界匹配
# ^ $ 在[]中和在[]外不一样
qq = "1231234456"
r = re.findall("^[\d]{4,10}$",qq)

#组
r = re.findall("(123){2}", qq)  # [123]

#re.I, re.S(\n)
ss = "HELLO\n world"
r = re.findall("hello.{1}",ss, re.I | re.S)


#re.sub
r = re.sub("o", "e", ss, flags = re.I)