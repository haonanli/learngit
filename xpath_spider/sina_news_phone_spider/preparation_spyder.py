import requests
import re
from lxml import etree
import numpy as np
# import process_wangyi as sw
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive"
}
def process(text):
    clean_text=re.sub("\n","",str(text)).strip()
    return clean_text

#获取ip代理网站的ip地址和端口号
def get_content(url):
    url=requests.get(url,headers=headers)
    url.encoding=url.apparent_encoding
    # print(url.text)
    ip_text=etree.HTML(url.text)
    print(ip_text)
    ip=ip_text.xpath("//table[@id='ip_list']//tr[@class='odd']/td[2]/text()")
    port=ip_text.xpath("//table[@id='ip_list']//tr[@class='odd']/td[3]/text()")

    ip_list=[]
    for i in range(len(ip)):
        item=process(ip[i])+":"+process(port[i])
        ip_list.append(item)
    return ip_list

def test_ip(ip_list):
    available_ip_list=[]
    available_proxies_list=[]
    for item in ip_list:
        address="http://"+item
        proxies={
            "http":address,
            "https":address
        }
        try:
            url="http://news.163.com/"
            a=requests.get(url,proxies=proxies,timeout=15)#,headers=headers,
        except:
            print(item,"is not available")
            continue
        available_ip_list.append(item)
        available_proxies_list.append(proxies)
    return available_ip_list,available_proxies_list

def get_user_agent():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    user_agent = np.random.choice(user_agent_list)
    return user_agent

#尝试用多进程来筛选
def main():
    url="http://www.xicidaili.com/nn/"
    ip_list=get_content(url)
    print("未测试前ip_list",ip_list)
    clean_ip_list,clean_proxies_list=test_ip(ip_list)
    print("测试后的ip_list",clean_ip_list)
    print("测试后的proxies_list",clean_proxies_list)
    return clean_ip_list

if __name__=="__main__":
    clean_ip_list=main()
    print("get the whole ip_list")
    np.save("ip.npy",clean_ip_list)