# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 04:38:32 2018

@author: zyx
"""

from urllib import request

url = "https://www.gushiwen.org/gushi/songci.aspx"

fr = request.urlopen(url)
txt = str(fr.read(),encoding="utf-8")
#<span><a href="https://so.gushiwen.org/shiwenv_3ffd5d0653a9.aspx" target="_blank">如梦令·昨夜雨疏风骤</a>(李清照)</span>


import re
#. 除\n之外的字符
# [\s\S]* 更为可靠，避免换行引起的错误
# 使用非贪婪模式，避免不必要的问题
lt = re.findall('<span>.+?target="_blank">(.+?)</a>\((.+?)\)</span>', txt)
