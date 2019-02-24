#此代码有问题
import requests
from PIL import Image
import pytesser3

url="http://ip.zdaye.com/"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive"
}
# def get_url(url):
#     content=requests.get(url,headers=headers)

def pre_process():
    threshold=0.5
    table=[]
    for i in range(256):
        if(i<threshold):
            table.append(0)
        else:
            table.append(1)
    return table

link=r"C:\Users\john\Downloads\1.bmp"
im=Image.open(link)#打开图片
imagry=im.convert("L")
# imagry.show()

# table=pre_process()
# out=imagry.point(table,"1")
# out.show()
print(pytesser3.image_to_string(imagry))