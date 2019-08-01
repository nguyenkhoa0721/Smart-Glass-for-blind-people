import bs4
from bs4 import BeautifulSoup as soup
import requests
from urllib.request import urlopen
def NEWS(title):
  if (title==""):
  	title=""
  result=[]
  rj = requests.get("https://cenaserver.kt-browser.com/news-v1?text="+str(title))
  tmps=rj.json()
  d=0
  for tmp in tmps:
    d=d+1
    result.append((d,tmp["title"],tmp["link"]))
  return result

  Client=urlopen(news_url)
  xml_page=Client.read()
  Client.close()
  soup_page=soup(xml_page,"xml")
  news_list=soup_page.findAll("item")
  result=[]
  d=0
  for news in news_list:
    d=d+1
    result.append((d,news.title.text,news.link.text))
  return result
#print(NEWS("Học sinh lớp 11 chế tạo hệ thống trợ giúp lái xe an toàn"))
