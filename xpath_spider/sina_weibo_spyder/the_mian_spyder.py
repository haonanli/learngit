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
    text=requests.get(path,cookies=cookies)
    # text.encoding=text.apparent_encoding
    soup=BeautifulSoup(text.text,"html.parser")
    # b = "WB_text W_f14"
    # b = "WB_detail"
    # stra = "\\" + '"' + b + "\\" + '"'
    # print(stra)
    # # print(soup.prettify())
    # # url_text=soup.find('div',{'class':stra})
    # url_text=soup.find('title')
    # print(url_text)
    # soup=etree.HTML(text.text)
    print("!!!")
    '''使用正则表达式提取信息'''
    # regex=re.compile(r'<div class=\\"WB_text W_f14\\".*>')
    result=re.findall(r'<div class=\\"WB_text W_f14\\".*?>(.*?)<\\/div>',soup.prettify())
    print(len(result))
    print(result)
    for item in result:
        # item=dp.pre_processing_to_get_chinese(item)
        print(item)
        item=re.sub(item,"[^\u4e00-\u9fa5]","")
        print(item)


    # url_text=soup.xpath("//*[@id=\\'v6_pl_content_homefeed\\']/div/div[4]/div[4]/div[1]/div[4]/div[3]/text()[1]")
    # print(url_text)
    # for item in url_text:
    #     print(item)


def main():
    path = r"https://weibo.com/u/6522715262/home?wvr=5&uut=fin&from=reg#1523092906913"
    cookies={'cookie':'SCF=AowL1aEpXP0Lw2CwqlbYflG_wO_zifyKOe9_K9gakgYAyu7Y1vR6T6pkga_cjn3q7BkjjFwWGackkhvnMaWMbTU.; SUB=_2A253zfsfDeRhGeBL6VAW8SvOzT6IHXVUu2vXrDV8PUNbmtANLXWskW9NRyPuiiUwtwg9U-S_qquEmiHYFADJW3JK; wvr=6; YF-V5-G0=46bd339a785d24c3e8d7cfb275d14258; YF-Page-G0=b98b45d9bba85e843a07e69c0880151a; _s_tentry=-; UOR=,weibo.com,spr_sinamkt_buy_hyww_weibo_t137; Apache=282227831004.57336.1523157817378; SINAGLOBAL=282227831004.57336.1523157817378; ULV=1523157817426:1:1:1:282227831004.57336.1523157817378:; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; WBtopGlobal_register_version=2018040811'}
    get_weibo_content(path,cookies)

main()