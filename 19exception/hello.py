print ('hello world!')

dic = {'name':'xxx', 'age':33}

for k,v in dic.items():
	print (k,'\t',v)


try:
 	print (1/0)
except Exception as e:
	print ('divide zero error')


dic = {}
dic['xx'] = 1
print (dic)