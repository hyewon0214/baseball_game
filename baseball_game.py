from bs4 import BeautifulSoup
import urllib.request
response=urllib.request.urlopen('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo&year=2020')
soup=BeautifulSoup(response,'html.parser')
data=[]
for tr_tag in soup.find(id='regularTeamRecordList_table').find_all('tr'):
    th_tag=tr_tag.find('th')
    strong_tag=th_tag.find('strong')
    span_tag = tr_tag.findAll('span')