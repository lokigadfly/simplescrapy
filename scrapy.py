from bs4 import BeautifulSoup
import requests
import random
def request(url):
	text = ''
	possible = 'abcdefghijklmnopqrstuvwxyz0123456789'
	for i in range(32):
		text = text + possible[random.randint(0,len(possible)-1)]
	cookies = dict(__cfduid=text)
	headers = {'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,und;q=0.4,ja;q=0.2,ko;q=0.2'}
	while True:
		try:
			r  = requests.get(url, cookies = cookies, headers = headers)
			html = r.text
			break
		except requests.exceptions.RequestException as e:
			print(e)
	return html

html_doc = request("https://movie.douban.com/subject/1296141/");
soup = BeautifulSoup(html_doc,"lxml")

something=soup.find_all(id="info")
print(soup.prettify())
for tr in something:
	#  标题
	movie_title=soup.find(property="v:itemreviewed")
	print(movie_title.contents[0])
	# 导演部分
	director=tr.contents[1]
	director_name=director.find_all(rel="v:directedBy")
	directorlist=[]
	for item in director_name:
		directorlist.append(item.contents[0])
	print(directorlist)
	# 编剧部分
	writers=tr.contents[4]
	writers_name=writers.find_all("a")
	writerslist=[]
	for item in writers_name:
		writerslist.append(item.contents[0])
	print(writerslist)
	#  主演部分
	starrings=tr.contents[7]
	starrring_name=starrings.find_all(rel="v:starring")
	starrings_list=[]
	for item in starrring_name:
		starrings_list.append(item.contents[0])
	print(starrings_list)

	#  类型
	genre=soup.find_all(property="v:genre")
	genre_list=[]
	for item in genre:
		genre_list.append(item.contents[0])
	print(genre_list)
	# print(tr.contents[12])
