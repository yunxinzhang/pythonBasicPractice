# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 23:55:22 2018

@author: zyx
"""

from enum import IntEnum

#增加代码的可读性，易于维护

# 继承
class Color(IntEnum):
    YELLOW = 0
    BLACK = 1
    RED = 2
    BLUE = 3
    
print (Color.YELLOW)

# 数字转类
a = Color(0)
print(a)
#a = Color.YELLOW
if a == Color.YELLOW:
    print("yes")
else:
    print("no")