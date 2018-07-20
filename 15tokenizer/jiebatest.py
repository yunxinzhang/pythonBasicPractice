import jieba
import jieba.analyse as ja
import jieba.posseg as pseg

''' #分词
st = '陈小鲁系开国元帅陈毅次子。公开报道显示，其于2018年2月28日在海南三亚，因急性大面积心肌梗死去世，享年72岁。'

res = jieba.cut('陈小鲁系开国元帅陈毅次子。公开报道显示，其于2018年2月28日在海南三亚，因急性大面积心肌梗死去世，享年72岁。')

res = ' '.join(res)

print(res)
'''

''' # 提取关键词
with open('1.txt','r') as fr:
	txt = fr.read()
	print(txt)
	tfidf = ja.extract_tags
	keywords = tfidf(txt, 10)
	print(' '.join(keywords))

	textrank = ja.textrank
	keywords = textrank(txt, 10)
	print(' '.join(keywords))
'''
print(unicode('中文字符').encode('utf-8'))
# words = pseg.cut('你是猴子派来的救兵吗？')
words = pseg.cut('沟通是维持人际关系的方法。')
# print(type(words))

# print(type(next(words)))
for w in words:
	print(w.word, w.flag)
