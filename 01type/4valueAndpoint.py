# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:46:13 2018

@author: zyx
"""
# 值类型 引用类型

# =============================================================================
# int , str,  tuple 值类型
# [] , set, {} 引用类型
# =============================================================================


a = 1
b = a
a = 2
print(a, b)

l1 = [1,2,3]
id(l1)      # id(var) ----> id[var]
l2 = l1
l1[0] = 99
id(l1)
print(l1, l2)

str1 = "hello"
id(str1)
str1 = str1+" world"
id(str1)
print(str1 )

#eg
tp = (1,2,[12,33])
id(tp[2])
tp[2][0] = 0
id(tp[2])
print(tp)