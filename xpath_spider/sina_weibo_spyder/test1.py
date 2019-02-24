from lxml import etree
import requests
from bs4 import BeautifulSoup
'''传入链接，获取该链接网页的全部内容'''
path = r"https://m.weibo.cn/"
cookies={'cookie':'_T_WM=95538d91158b8c915b41776a840a7b5f; SUB=_2A2534s7MDeRhGeBL6VAW8SvOzT6IHXVVLNKErDV6PUJbkdANLXTdkW1NRyPuilMf5EIxDQE9vHD6M-5HKMBCShxA; SUHB=0u5RwtwFfeYpq5; SCF=AviXLfRG5MUUf0C_-y0pu7k-ENCQGukyNkH_hfJQixDUZ8S6ss9KB4nKkERuJqjdnmfcrNoCZVMyDsqFf9YkAP8.; SSOLoginState=1525071516; H5_INDEX=0_all; H5_INDEX_TITLE=%E6%95%B0%E6%8D%AE%E8%99%AB7087; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=featurecode%3D20000320%26oid%3D4234519227838488%26luicode%3D20000061%26lfid%3D4234519227838488%26uicode%3D20000174%26fid%3Dhotword'}

print("###")
text=requests.get(path,cookies=cookies)
text.encoding=text.apparent_encoding
# soup=etree.HTML(text.text)
soup=BeautifulSoup(text.text,"html.parser")
print(soup.prettify())
url_text=soup.find("div",{"class":"WB_text W_f14"})

# print(soup)
# print()
# url_text=soup.xpath("//div[@class='WB_detail']/div[@class='WB_text W_f14']/text()")
print(url_text)
for item in url_text:
    print(item)


