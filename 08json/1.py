# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 23:13:53 2018

@author: zyx
"""

import json


# 序列化
#json object  -->  dict

# json 字符串必须是标准格式，包括 双引号， 大小写
json_str = '{"name":"xxx", "age":22, "chinese":true}'

st1 = json.loads(json_str)

#json array   -->  list

json_str2 = '[{"name":"xxx", "age":22, "chinese":true},{"name":"yyy", "age":22, "chinese":false}]'

sts = json.loads(json_str2)

#反序列化

# py list --> json string
pylist = [
            {'name': 'xxx', 'age': 22, 'chinese': True},
            {'name': 'yyy', 'age': 22, 'chinese': False}
        ]
jstr = json.dumps(pylist)