# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 03:31:12 2018

@author: zyx
"""

x = [1,2,3,4]
y = [3,6,9,7,11]
y = map(lambda x:x**3, x) # map object
y = list(y)


# =============================================================================
# # map 的参数为 可变参数； 以最短的为准
# =============================================================================
z = list(map(lambda a, b : a * b , x, y))


# =============================================================================
# # ruduce 
# =============================================================================
from functools import reduce
fac = reduce(lambda a,b:a*b, x)

# =============================================================================
# #filter 清洗数据
# =============================================================================

nx = list(filter(lambda x:x>2, x)) #filter object  --> iterater


# =============================================================================
# #sorted 排序  #help(sorted)
# =============================================================================

class student():
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
        
st1 = student('x',99)
st2 = student('y',100)
st3 = student('z',98)
st = [st1, st2, st3]

sst = sorted(st, key=lambda st:st.score)
type(sst)
for it in sst:
    print(it.name)


















