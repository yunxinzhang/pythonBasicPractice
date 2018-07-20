# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 01:39:51 2018

@author: zyx
"""
#全局变量的缺点是对对象的处理 不封闭， 其它地方修改了全局变量的值，难以查找
init = 0

def add(x):
    global init
    init += x
    return init

add(3)
add(4)
add(5)