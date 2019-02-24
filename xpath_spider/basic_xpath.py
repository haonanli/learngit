import requests
from lxml import etree
import re
import jieba
from zhon.hanzi import punctuation
# url="http://sports.163.com/17/1226/16/D6JIAM7F0005877V.html"
# html=requests.get(url)
# html.encoding=html.apparent_encoding
# # soup=BeautifulSoup(html.text,"html.parser")
# # # print(soup.prettify())
# soup=etree.HTML(html.text)
# pose_text=soup.xpath("//div[@id='endText']/p/text()")
# pose_text="".join(pose_text)
# pose_text=re.sub("\s|\d","",pose_text)
# print(pose_text)
# #去除所有的中文字符
# a=jieba.lcut(pose_text,cut_all=False)
# print(a)
# pose_text=re.sub(r"[%s]+" %punctuation,"",pose_text)#去除所有的标点标点符号
# print(pose_text)
# seperate_word=jieba.lcut(pose_text,cut_all=False)
# print(seperate_word)

url="https://movie.douban.com/subject/26799731/comments?start=20&limit=20&sort=new_score&status=P&percent_type="
html=requests.get(url)
html.encoding=html.apparent_encoding
# soup=BeautifulSoup(html.text,"html.parser")
# # print(soup.prettify())
soup=etree.HTML(html.text)
# pose_text=soup.xpath("//a[text()='后页 >']/@href")
pose_text=soup.xpath("//a[@class='next']/text()")
print(pose_text)
# pose_text="".join(pose_text)
# pose_text=re.sub("\s|\d","",pose_text)
# print(pose_text)
# #去除所有的中文字符
# a=jieba.lcut(pose_text,cut_all=False)
# print(a)
# pose_text=re.sub(r"[%s]+" %punctuation,"",pose_text)#去除所有的标点标点符号
# print(pose_text)
# seperate_word=jieba.lcut(pose_text,cut_all=False)
# print(seperate_word)

