# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 18:51:40 2018

@author: zyx
"""

lt = [0,1,2,3,4,5,6,7]

# 序列用切片
for i in lt:
    print(i)
for i in lt[0::2]:
    print(i)
for i in lt[-1::-1]:
    print(i)
    
for i in range(0,len(lt),2):
    print(i)
    
    
for i in range(len(lt)-1,-1,-1):
    print (lt[i])

# 位置，结束点，步长 
for i in range(len(lt)-1,-1,-2):
    print (lt[i])
    
for i in range(len(lt)-1,-1,-2):
    print (lt[i], end=" | ")
    
    
# 高性能
# 封装性好，可以复用