# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 22:25:58 2018

@author: zyx
"""

import re

# match , search   判断是否开始就存在，是否存在

ss = "a567a"

r = re.match("\d", ss)
# print 无可替代
print(r)
r1 = re.search("\d", ss)
print(r1)


# group

ss = "abc123abc456python"

r = re.match("abc(\d+)abc(\d+)python", ss)
print(r.groups())
print(r.group())
print(r.group(0,1,2))