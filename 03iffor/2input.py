# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 15:33:21 2018

@author: zyx
"""

accname = 'root'
accpwd = 'tiger'
name = input("输入姓名>>")
pwd = input("输入密码>>")  # 返回的数据类型为str

if (name == accname and accpwd == pwd):
    print("go")
else:
    print("error")