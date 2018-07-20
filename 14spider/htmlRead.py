from urllib import request
import urllib
url = 'http://www.0668bbs.com/sicijianshang/tangdai/libaishici/0673004195294541.htm'

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
txt =  response.read()
# txt =txt.decode()

# txt = txt.encode('utf-8')
print(type(txt))
print (123)
print(txt)

txt =txt.decode('gbk')

print(txt)
# with open('s.txt','wb') as fw:
# 	fw.write(txt)

# with open('s.txt','r') as fr:
# 	txt =fr.read()

# print(txt)