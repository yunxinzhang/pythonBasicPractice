# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:12:55 2018

@author: zyx
"""
import time
# set 

s = {1,2,3,4}
2 in s

t1 = time.time()
s2 = {1,2,2,2}
for i in range(100000):
    x = i*i/123*2323
s2
t2 = time.time()
print(t2-t1)

len(s2)

s - s2
s & s2
s | s2

type(set()) # 空集
type({})

#dict

skill = {"B":"Block", "M":"Move", "R":"RUN"}
skill["B"]
len(skill)

# key unhashable type
#dic = {[1,2]:"A"}
dic = {(1,2):"A"}