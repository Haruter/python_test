import requests
import re
from bs4 import BeautifulSoup
num=0#定义条数的初始值
#定义一个变量url，为需要爬取数据我网页网址
url = 'http://www.guangzhoubbs.net/forum-42-1.html'
#获取这个网页的源代码，存放在req中，{}中为不同浏览器的不同User-Agent属性，针对不同浏览器可以自行百度
req = requests.get(url,{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
#生成一个Beautifulsoup对象，用以后边的查找工作
soup = BeautifulSoup(req.text,'html.parser')
#筛选获取的数据，或用正则进行数据匹配
# for item in soup.table.find_all('a'):
#     item1 = item.get("href")
#     item2 = item.get_text()
#     print(item1)
#     print(item2)

print(soup)
