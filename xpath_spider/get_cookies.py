import requests
import re
from lxml import etree

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive"
}
cookies={"cookie":"SINAGLOBAL=175122764878.4104.1511873851388; wvr=6; UOR=www.chinacloud.cn,widget.weibo.com,login.sina.com.cn; login_sid_t=ceae9024dc1bd9a9b63e995f196f83e6; _s_tentry=passport.weibo.com; Apache=3290476942035.0522.1514773588742; ULV=1514773588750:6:1:2:3290476942035.0522.1514773588742:1514687942010; cross_origin_proto=SSL; SSOLoginState=1514773649; SCF=AowL1aEpXP0Lw2CwqlbYflG_wO_zifyKOe9_K9gakgYA0KET_lJwwNqKzXFlAYR4nd0NlcvjmCoEnro75dOqcPM.; SUB=_2A253TezCDeRhGeNP7loU9C_NzzuIHXVUO1kKrDV8PUNbmtANLVPukW9NTm0bSo1ZYtTufn6ewbJAKLUXwmQRXS96; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh.knk6R7Kujvl-G4FKjaaC5JpX5K2hUgL.Fo-pSKnfSh2pShM2dJLoIpjLxK-LB.-LB--LxKMLB-eL1K2peoeXSK.RS0qt; SUHB=09P9IGC8en__wG; ALF=1546309649; un=15671592312"}
url="https://weibo.com/u/5158541147/home?wvr=5"
content=requests.get(url,headers=headers,cookies=cookies)
print(content.content)
coo=content.cookies
print(coo)
for item in coo:
    print(item.name)
    print(item.value)
    print(item.expires)