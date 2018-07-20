# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 03:46:38 2018

@author: zyx
"""
import time
# 开闭原则
# 对于修改是封闭的，对于扩展是开放的

# 装饰器
def timeit(func):
    def wrapper(*args, **kw):
         start = time.time()
         func(*args, **kw)   # 参数列表 ： 可变参数 *， 关键词参数 **
         end = time.time()
         print("用时", end-start, "秒")
    return wrapper   #必须返回
         
if __name__ == "main":
    
    @timeit         
    def square(ls):
        nls = []
        for i in ls:
            nls.append(i*i)
        return nls
    
    
    @timeit         
    def say(ls, sth=""):
        nls = []
        print(sth)
        for i in ls:
            nls.append(i*i)
        return nls
            
    ls = range(10000)
    len(ls)
    
    t = square(ls)
    say(ls,"hello")

