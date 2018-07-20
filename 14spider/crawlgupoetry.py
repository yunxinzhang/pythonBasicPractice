import requests
from bs4 import BeautifulSoup as bsp
url = 'http://so.gushiwen.org/gushi/tangshi.aspx'
web = 'http://so.gushiwen.org'
response = requests.get(url)
# ctrl+[, ctrl+]可以左右平移
# print(response.text)

html = bsp(response.text,'lxml')

# print (html.prettify())

span = html.select('span')
i=0
with open('poets.txt','w') as fw:
	while(i < len(span)):
		poet = span[i].a['href']
		url = web+poet
		response = requests.get(url)
		html = bsp(response.text,'lxml')
		title = html.find(name='h1')
		# print(title.text)
		author = html.find(name='p', attrs={'class':'source'})
		# print (author.select('a')[0].text)
		author = author.select('a')
		authortime = author[0].text
		authorname = author[1].text
		# print(authortime,authorname)
		content = html.find(name='div', attrs={'class':'contson'})
		# print(content.text)
		fw.write(title.text+'\n')
		fw.write(authortime+' '+authorname+'\n')
		fw.write(content.text+'\n\n\n')
		i+=1
		# break