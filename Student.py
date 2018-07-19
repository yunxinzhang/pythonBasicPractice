# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 18:56:13 2018

@author: zyx
"""
# Life is short. I use python

class Student():
    totalNumber = 0
    lastStudentName = ''
    def say(self):
        print("My name is %s" % self.name)
        print("I am %s years old" % self.age)
        self.__topSecret()
    

# =============================================================================
# 1 构造函数为 __init__
# 2 不能直接访问类变量
# 3 成员变量通过 self. 来添加
# 4 构造函数返回 None
# =============================================================================
    def __init__(self,age=0,name='',score=0):
        self.age = age
        self.name = name
        self.__score = score
        Student.totalNumber = Student.totalNumber+1
        #另外一种方式调用类变量
        self.__class__.lastStudentName = name
    
    
    
    @classmethod
    def getTotalNumber(cls):
        return cls.totalNumber
    @classmethod
    def getLastStudentName(cls):
        return cls.lastStudentName
    
    @staticmethod
    def add(x, y):
        return x+y
    
    def __topSecret(self):
        print("top secret")
    def setScore(self, score=0):
        self.__score = score
    def getScore(self):
        return self.__score

