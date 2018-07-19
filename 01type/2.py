# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:56:14 2018

@author: zyx
"""

#list
type([1,2,'d'])
ls = [1,2,3,4]
type(ls[0:2])
type(ls[-1:]) #仅仅一个元素的list

ls2=[3,4,5]
# add
ls+ls2
ls[0] = 33
ls3 = [[1,2],[3,4]]


#tuple
type((1,2,3))
tp1 = (1,2)
tp2 = (3,4)
tp1+tp2
tp1[0]
#tp1[0] = 55
type((1,))
tp3 = ()
type(tp3)
print((1,))

# 序列
#序列号
#切片
tp4 = (1,2,3)
3 in tp4
3 not in tp4
len(tp4)
max(tp4)
min(tp4)

ord('a') # 返回ascii编码

