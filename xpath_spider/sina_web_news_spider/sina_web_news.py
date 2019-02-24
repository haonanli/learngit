#获取网易新闻爬虫文件,163行的get_more_link中的第二个参数用于获取更多的链接
import numpy as np
import preparation_spyder as ps
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from lxml import etree
import re
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import threading
from multiprocessing import Pool
import multiprocessing
from selenium.webdriver import ActionChains

ip_list=np.load("ip.npy")
# print(url_list)
# ip=np.random.choice(ip_list)
# print(url)
# us_ag=gf.get_user_agent()
#从gf

headers = {
    # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "User-Agent": ps.get_user_agent(),
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive"
}

def get_front_url(url):#获取以及页面的url
    text=requests.get(url,headers=headers)
    text.encoding=text.apparent_encoding
    text=text.text
    soup=etree.HTML(text)
    url_link_a=soup.xpath("//ul[@class='links clearfix']/li/a/@href")
    # print(url_link_a)
    # print(type(url_link_a))
    url_name_a=soup.xpath("//ul[@class='links clearfix']/li/a/text()")
    url_link_b=soup.xpath("//ul[@class='clearfix']/li/a/@href")
    # print(url_link_b)
    url_name_b=soup.xpath("//ul[@class='clearfix']/li/a/text()")
    url_link=url_link_a+url_link_b
    url_name=url_name_a+url_link_b
    print(url_link)
    print(url_name)
    url_link=[str("http://")+item for item in url_link]
    print(url_link)
    url_link=url_link[2:]
    url_name=url_name[2:]
    f=open(r"front_url.csv","w+",encoding="utf-8",errors="ignore",newline="")
    combine=list(zip(url_name,range(len(url_link)),url_link))#将文件存储为名称、编号、链接列
    writer=csv.writer(f)
    writer.writerows(combine)
    f.close()
    return url_link,url_name

def get_the_content(url,name):#得到一个URL列表，获取列表中每个链接对应的页面的文字信息
    with open(r"b.csv","w+",encoding="utf-8",errors="ignore",newline="") as csvfile:
        writer=csv.writer(csvfile)
        k=1
        for u in url:
            ip=np.random.choice(ip_list)
            proxies={
                "http":ip,
                "https":ip
            }
            try:
                text=requests.get(u,headers=headers,proxies=proxies)
                # text=requests.get(u,headers=headers)
                text.encoding=text.apparent_encoding
                text=text.text
            except:
                continue
            soup = etree.HTML(text)
            url_content= soup.xpath("//div[@class='article']/p/text()")
            if url_content==[]:
                url_content = soup.xpath("//div[@class='BSHARE_POP blkContainerSblkCon clearfix blkContainerSblkCon_14']/p/font/text()")
            url_content="".join(url_content)
            print(url_content)
            print(headers,'\n',ip)
            try:
                writer.writerow([name,url_content])
            except:
                print("error in the content_page_saving")
            k=k+1
            print(name,"正在爬取第",k,"个页面")
    x=np.random.uniform(0,0.8)
    time.sleep(x)

# 多线程方法
def multi_thread(url_list):#url_link是一个URL列表结合，即列表里面包列表
    threads = []
    for id, url in enumerate(url_list):
        thread = threading.Thread(target=get_the_content, args=(url, id,))
        threads.append(thread)
        thread.start()
        print("正在爬取第：", id, "个页面")
    for i in threads:
        i.join()

def multi_process(url_list):
    pool = Pool(multiprocessing.cpu_count())
    print("cpu个数为：{0}".format(multiprocessing.cpu_count()))
    for id,url in enumerate(url_list):
        pool.apply_async(get_the_content,args=(url,id,))
    # pool.map(get_the_content,url_list,list(range(len(url_list))))
    pool.close()
    pool.join()#调用join方法之前一定要先调用close方法，关闭进程池子

def set_browser():
    # 配置浏览器，通过DesiredCapacities来配置
    dcap = dict(DesiredCapabilities.PHANTOMJS)  # 在phantomjs上伪装浏览器
    dcap['phantomjs.page.settings.userAgent'] = (
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    dcap["phantomjs.page.settings.loadImages"] = False  # 此方法表示不载入图片，用于加快浏览器加载速度
    # service_args = ['--ignore-ssl-errors=true']  # 浏览器代理，也可以是['--proxy=127.0.0.1:9999', '--proxy-type=socks5']
    service_args = [
        # '--proxy=%s' % np.random.choice(ip_list),  # 代理 IP：prot    （eg：192.168.0.28:808）
        # '--proxy = 192.168.0.28:808',  # 代理 IP：prot    （eg：192.168.0.28:808）
        '--proxy-type=http',  # 代理类型：http/https
        '--load-images=no',  # 关闭图片加载（可选）
        '--disk-cache=yes',  # 开启缓存（可选）
        '--ignore-ssl-errors=true']
    driver = webdriver.PhantomJS(executable_path=r"G:\codefile\pythonfile\统计计算\phantomjs-1.9.8-windows\phantomjs",
                                 desired_capabilities=dcap, service_args=service_args)  # 打开带配置的浏览器
    # driver.implicitly_wait(5)  # 隐式等待时间是5s
    time.sleep(5)  # 隐式等待时间
    # driver.set_page_load_timeout(15)  # 设置10s页面超时返回时间
    # driver.set_script_timeout(20)  # 设置10s脚本超时时间
    return driver

#点击加载更多二级页面链接,用于在具体的二级页面点击“加载更多”的按钮
def get_more_links(driver,num):#num为点击次数
    for i in range(num):
        try:
            ac = driver.find_element_by_xpath("//div[@class='tianyi__list-a']/div[last()]")
            ActionChains(driver).move_to_element(ac).perform()  # 定位鼠标到指定元素
            time.sleep(2)  # 给加载内容预留2秒
        except:
            print("出错")
            continue
        print("第{0}轮".format(i))

def get_total_url_list(driver,url_link):#返回二级页面中所有的标签列表
    url_list=[]

    for id, item in enumerate(url_link):
        # driver = webdriver.PhantomJS(executable_path=r"G:\程序文件\python程序文件\统计计算\phantomjs-1.9.8-windows\phantomjs",desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true'])
        driver.get(item)

        get_more_links(driver,10)
        # time.sleep(3)
        page_source = driver.page_source#获取整个页面的标签信息
        page_source = page_source.encode("utf-8", "ignore").decode("utf-8")
        # print(page_source)
        # soup=BeautifulSoup(page_source,"html.parser")
        # print(text)
        soup = etree.HTML(page_source)
        # url = soup.xpath("//div[@class='cardlist-a__list']/div[@class='ty-card ty-card-type1 clearfix']/div[@class='ty-card-r']/h3/a/@href")#返回一个url列表
        url = soup.xpath("//div[@class='ty-card ty-card-type1 clearfix']/div[@class='ty-card-r']/h3/a/@href")#返回一个url列表
        if url==[]:
            url = soup.xpath("//div[@class='feed-card-item-hd']/h2/a/@href")  # 返回一个url列表
        if url==[]:
            url = soup.xpath("//div[@data-ctr='list']/div/div[@class='item udv-clearfix']/div[@class='c-title']/div[@class='content']/a/@href")
        # url = soup.xpath("//div[@class='ndi_main']//a")
        print(url)
        print("第{0}轮，有{1}个链接".format(id, len(url)))
        url_list.append(url)
    return url_list

def main():
    url = "http://sports.sina.com.cn/"
    url_link, url_name = get_front_url(url)
    print(url_link)
    num_link = len(url_link)

    #用于获取伪装的浏览器
    driver=set_browser()
    #用于获取所有的链接，形成列表的列表
    url_list=get_total_url_list(driver,url_link)
    #部署多线程
    # multi_thread(url_list)

    #部署多进程
    multi_process(url_list)
    #关闭浏览器
    driver.close()

def show_time(item):
    a=time.localtime(item)
    b=time.asctime(a)
    return b

if __name__=='__main__':
    begin=time.time()
    main()
    end=time.time()
    total=end-begin
    try:
        print("开始时间是：{}".format(show_time(begin)))
        print("结束时间是：{}".format(show_time(end)))
        print("总共消耗的时间是：{}".format((end-begin).minutes))
    except:
        print("time is errow")