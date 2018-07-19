# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:11:49 2018

@author: zyx
"""

# 算术
# 赋值   += **=
# 比较   == +++
# 逻辑   and or not+
# 位运算符    & | ~ ^ >> <<
# 成员运算符  in  not in
# 身份运算符 id1==id2

a = 3
a = a**3

# 短路
[1] or []
#  [1]

# is not is
a = 1
b = 1.0
a == b
a is b

tp1 = (12,1)
tp2 = (12,1)
tp1 == tp2
tp1 is tp2
tp2 = tp1
tp1 is tp2

# 对象的三个特征 id， type， value
a = 123
type(str)
isinstance(a,int)
# 声明的变量名为str是不好的习惯
isinstance(a,(float,list,str))

a = 1
b = 2
a & b
a | b
~a # 补码 n --> -n-1
~b
a^b
a<<1
c = -1
~c   # c~c = -1



a = 1
b = 2
c = 3


# and > or
a and b or c

#(a and b) or c

a or b and c

# a or (b and c)

#单目运算符优先级高 error , 没有这种规矩， 写代码的时候避免这种难以阅读的代码
not a and b or c

# ((not a) and b) or c

a and not b or c

# 算术 > 比较  > 逻辑