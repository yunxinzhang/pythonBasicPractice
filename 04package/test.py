# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 19:04:47 2018

@author: zyx
"""
import sys
print(sys.path)
#文件夹名   文件名  变量&函数
# 如此这样导入，名字短

# method 1
from zmath import fun
print (fun.add(4,4))
print(fun.pi)

# method 2
# =============================================================================
# * 代表函数与变量等
# from zmath.fun import *
# print(add(3,4))
# print(pi)
# =============================================================================

# method 3
# =============================================================================
# 如此导入名字长
# import zmath.fun
# print(zmath.fun.add(2,3))
# print(zmath.fun.pi)
# =============================================================================
