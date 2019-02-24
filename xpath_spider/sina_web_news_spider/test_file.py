import pandas as pd
from lxml import etree
import requests

path=r'http://tech.sina.com.cn/'
data=requests.get(path)
data.encoding=data.apparent_encoding
soup=etree.HTML(data)

target=soup.xpath("//")