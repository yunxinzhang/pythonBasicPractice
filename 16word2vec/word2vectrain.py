from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import time

# sentences = Word2Vec.Text8Corpus('train.txt')
# model = Word2Vec(sentences,size=128, window=5,min_count=5,workers=4)

# model.save('word_embedding_128');

# with open('wiki.zh.word.text',encoding='utf8') as fr:
# #with open('s.txt',encoding='utf8') as fr:
# 	s = fr.read()
# 	print(s)

'''
sentences = []
with open('train.txt','r') as fr:
	 while 1:
	 	line = fr.readline()
	 	if not line:
	 		break
	 	a = line.strip().split(' ')
	 	sentences.append(a)

model = Word2Vec(sentences,size=128, window=5,min_count=5,workers=4)
model.save('word_embedding_128');	 	
'''
a = time.time()
wlist = []
# for i in range(1,100000):
wlist.append('滚动轴承')
wlist.append('轮齿')
wlist.append('啮合点')
wlist.append('关节轴承')
wlist.append('润滑剂')
wlist.append('啮合刚度')
wlist.append('变速器')
wlist.append('螺旋角')
wlist.append('机械传动')
wlist.append('接触点')
b  = time.time()
print(b-a)
print(len(wlist))

a = time.time()
res= []
model = Word2Vec.load('word_embedding_128')
for i in range(len(wlist)):
	for j in range(len(wlist)):
		sim = model.similarity(wlist[i],wlist[j])
		res.append(sim)
b  = time.time()
print('>>>',b-a)		
a = model.similarity("轴承","齿轮")
print(a)
a = model.similarity("轴承","力矩")
print(a)
a = model.most_similar(positive=['轴承', '齿轮'], negative=['支撑'], topn=10)
print(a)