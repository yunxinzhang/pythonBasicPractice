# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 01:28:20 2018

@author: zyx
"""

# 避免使用全局变量
# 函数式编程
init = 0

def factory(nnow):
    def add(num):
        nonlocal nnow  # 类似类变量； 利用factory的参数名和函数体中的变量名一致来声明
        nnow += num
        return nnow
    
    return add

cnt = factory(init)

cnt(3)
cnt(4)
cnt(5)