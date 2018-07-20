# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 21:56:22 2018

@author: zyx
"""

import re
# eg 1
ss = "1234567"

def change(val):
    s = val.group()
    if s=="1":
        return "_one_"
    elif s=="2":
        return "_two_"
    elif s=="3":
        return "_three_"
    elif s=="4":
        return "_four_"
    else:
        return s
    
ns = re.sub("\d",change,ss)

# eg 2
ss = "12*34*64+122"

def change2(val):
    s = val.group()
    if int(s)>34:
        return "_one_"
    elif int(s) == 34:
        return "_zeor_"
    elif int(s)<34:
        return "_%_"

ns = re.sub("[\d]+", change2, ss)

