# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 18:59:08 2018

@author: zyx
"""
#同一工作目录下无需 __init__.py
from Student import Student

st = Student(20,'zyx')
st1 = Student(21,'xxx')
# __dict__ 返回字典 属性->值
st.__dict__
Student.__dict__
# id 返回 变量地址
id(st)
id(st1)
# __class__ 获取类对象
st.__class__.lastStudentName
st.say()
print (Student.getLastStudentName())
print (Student.add(3,4))

#st.__topSecret() 找不到函数，因为__开头的函数被重新命名了
st._Student__topSecret()

print(st.getScore())
st.setScore(20)
print(st.getScore())
st.__score = -1 #给对象增加了一个属性，__开头的属性是隐藏的，无法直接获取的
st.__dict__
print(st.getScore())
print(st.__score)
