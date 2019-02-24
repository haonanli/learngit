#使用多个user_agent切换，使用代理ip来爬虫
import numpy as np
import requests
import re
from lxml import etree
import datetime
import get_ip_from_ip_agent as gf

def get_time(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

#获取ip
# proxies_list=gf.main()
# proxies=np.random.choice(proxies_list)

#获取浏览器
user_agent=gf.get_user_agent()
headers={
    "User-Agent":user_agent,
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive"
}
data={
    "form_email":"15671592312@163.com",
    "form_password":"weichen3737",
    "login":u"登陆",
    "redir":"https://www.douban.com"
}
sess=requests.session()
url="https://www.douban.com/login"
contact_url="https://www.douban.com/"

#获取cookies
content=sess.post(url,headers=headers,data=data)
text=sess.get("https://www.douban.com/",headers=headers,)
print(text.cookies)
for item in text.cookies:
    print("name",item.name)
    print("value",item.value)
    print("expires",item.expires)
    print("expire_time",get_time(item.expires))