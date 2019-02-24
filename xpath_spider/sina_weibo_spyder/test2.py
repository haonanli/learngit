import numpy as np

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
headers = {
    # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive"
}

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

def get_more_links(driver,num):#num为点击次数
    for i in range(num):
        try:
            driver.find_element_by_xpath("//div[@class='post_addmore']/span").click()
            time.sleep(5)
        except:
            print("出错")
            continue
        print("第{0}轮".format(i))

def get_weibo_content(driver,path):
    print("###")
    text=driver.get(path)
    page_source = driver.page_source
    page_source = page_source.encode("utf-8", "ignore").decode("utf-8")
    soup=BeautifulSoup(page_source,"html.parser")
    print(soup.prettify())
    url_text = soup.find("a", {"class": "S_txt1"})
    print(url_text)
    # soup=etree.HTML(page_source)
    # print(soup)
    # urt_text=soup.xpath("//div[@class='WB_text W_f14']/text()")
    for item in url_text:
        print(item)


def main():
    # path = r"https://weibo.com/u/6522715262/home?wvr=5&uut=fin&from=reg#1523092906913"
    path = r"https://m.weibo.cn/"
    cookies = {'cookie': { '_T_WM':'95538d91158b8c915b41776a840a7b5f','SUB':'_2A2534s7MDeRhGeBL6VAW8SvOzT6IHXVVLNKErDV6PUJbkdANLXTdkW1NRyPuilMf5EIxDQE9vHD6M-5HKMBCShxA','SUHB':'0u5RwtwFfeYpq5','SCF':'AviXLfRG5MUUf0C_-y0pu7k-ENCQGukyNkH_hfJQixDUZ8S6ss9KB4nKkERuJqjdnmfcrNoCZVMyDsqFf9YkAP8.','SSOLoginState':'1525071516', 'H5_INDEX':'0_all', 'H5_INDEX_TITLE':'%E6%95%B0%E6%8D%AE%E8%99%AB7087','WEIBOCN_FROM':'1110006030','M_WEIBOCN_PARAMS':'featurecode%3D20000320%26oid%3D4234519227838488%26luicode%3D20000061%26lfid%3D4234519227838488%26uicode%3D20000174%26fid%3Dhotword'}}

    # cookies = { '_T_WM':'95538d91158b8c915b41776a840a7b5f','SUB':'_2A2534s7MDeRhGeBL6VAW8SvOzT6IHXVVLNKErDV6PUJbkdANLXTdkW1NRyPuilMf5EIxDQE9vHD6M-5HKMBCShxA','SUHB':'0u5RwtwFfeYpq5','SCF':'AviXLfRG5MUUf0C_-y0pu7k-ENCQGukyNkH_hfJQixDUZ8S6ss9KB4nKkERuJqjdnmfcrNoCZVMyDsqFf9YkAP8.','SSOLoginState':'1525071516', 'H5_INDEX':'0_all', 'H5_INDEX_TITLE':'%E6%95%B0%E6%8D%AE%E8%99%AB7087','WEIBOCN_FROM':'1110006030','M_WEIBOCN_PARAMS':'featurecode%3D20000320%26oid%3D4234519227838488%26luicode%3D20000061%26lfid%3D4234519227838488%26uicode%3D20000174%26fid%3Dhotword'}

    driver=set_browser()
    # driver.add_cookie(cookies)
    get_weibo_content(driver,path)
    driver.close()

main()