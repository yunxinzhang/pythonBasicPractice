
#统计字符串中各个字符的个数
import json
def cal(txt):
	dic = {}
	cnt = len(txt)
	for i in range(cnt):
		if txt[i] in dic:
			dic[txt[i]] += 1
		else:
			dic[txt[i]] = 1
	return dic

#测试data.txt文件，计算各个字符出现的次数
with open('data.txt','r') as fr:
	# print(fr.read())
	txt = fr.read()
	dic = cal(txt)
	with open('json.txt','w') as fw:
		fw.write(json.dumps(dic))
	print(dic)
	
	ls = sorted(dic.items(), key=lambda x: x[1], reverse=True)
	print(ls)
	# ls=sorted(dic.items(), lambda x,y:x[1]-y[1]>0)
	#t = [ v for v in sorted(dic.values())]

	print(30*'#')
	print(ls)

