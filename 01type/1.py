# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:19:13 2018

@author: zyx
"""

# only  int , float
type(1)
type(1.1)

# //  , /
type(3//2)  #int
type(3/2)

# 2,8,16
0b11
0o11
0x11

bin(22)
int(0b11)
hex(11)
oct(11)

#bool
type(True)
type(False)

# str
type('hello')
s = 'let\'s go'
# ''' 可以书写多行
ss = '''
hello world
hello world
hello world
'''
print(ss)
sss  = r'c:\user\zyx' # 原始字符串
sss
print(sss)

# str operation
stra = 'hello '
stra * 3  
stra[4]
stra[-1] # 反向数
stra[0:4]
stra[0:-1] # 去掉最后一个字符
stra[1:]
