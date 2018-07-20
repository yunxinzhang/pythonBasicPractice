# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 03:02:51 2018

@author: zyx
"""

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(self.name, ":", self.age)
        

class Student(Person):  #继承
    def __init__(self, name, age, score):
        super(Student,self).__init__(name,age) #调用 子类的父类
        self.score = score
    def say(self):
        super(Student,self).say()
        print(self.name, self.age, self.score)
        
st = Student("x", 12, 100)
st.say()