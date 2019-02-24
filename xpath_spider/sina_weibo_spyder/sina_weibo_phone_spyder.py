from lxml import etree
import requests
from bs4 import BeautifulSoup
import re
import data_processor as dp
headers = {
    # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive"
}
'''传入链接，获取该链接网页的全部内容'''
def get_weibo_content(path,cookies):
    print("###")
    text=requests.get(path,headers=headers,cookies=cookies)
    # text.encoding=text.apparent_encoding
    print(text.text)
    soup=BeautifulSoup(text.text,"html.parser")
    print(soup.prettify())
    # soup = etree.HTML(text.text)
    # print("!!!")
    # '''使用正则表达式提取信息'''
    # # regex=re.compile(r'<div class=\\"WB_text W_f14\\".*>')
    # result=re.findall(r'<div class=\\"WB_text W_f14\\".*?>(.*?)<\\/div>',soup.prettify())
    # print(len(result))

    url_text=soup.xpath("//p[@class='default-content txt-xl']/text()")
    print(url_text)
    for item in url_text:
        print(item)


def main():
    path = r"https://m.weibo.cn/"
    cookies = {'cookie': '_T_WM=95538d91158b8c915b41776a840a7b5f; SUB=_2A2534s7MDeRhGeBL6VAW8SvOzT6IHXVVLNKErDV6PUJbkdANLXTdkW1NRyPuilMf5EIxDQE9vHD6M-5HKMBCShxA; SUHB=0u5RwtwFfeYpq5; SCF=AviXLfRG5MUUf0C_-y0pu7k-ENCQGukyNkH_hfJQixDUZ8S6ss9KB4nKkERuJqjdnmfcrNoCZVMyDsqFf9YkAP8.; SSOLoginState=1525071516; H5_INDEX=0_all; H5_INDEX_TITLE=%E6%95%B0%E6%8D%AE%E8%99%AB7087; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=featurecode%3D20000320%26oid%3D4234519227838488%26luicode%3D20000061%26lfid%3D4234519227838488%26uicode%3D20000174%26fid%3Dhotword'}
    get_weibo_content(path,cookies)

main()