from lxml import etree
import requests
import re
from selenium import webdriver

# driver = webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# url ='https://www.qimai.cn/rank/release'
# driver.get(url=url)
# html=driver.page_source
# print(html)
# with open("text.html",'w',encoding='utf-8')as f:
#     f.write(driver.page_source)

headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"

}
response =requests.get(url='https://api.qimai.cn/rank/release?analysis=cBMfQlFeWxcWUlQBVUUEcBMDCAQGBgtTDg1XAHZCAQ%3D%3D',headers=headers)

html=response.content.decode('unicode=escape')
print(html)
# with open("text.py",'w',encoding='utf-8')as f:
#     f.write(html)
name_list = re.findall('"appName":"(.*?)"',html)
price_list = re.findall('"price":"(.*?)"',html)
genre_list = re.findall('"genre":"(.*?)"',html)
releaseTime = re.findall('"releaseTime":"(.*?)"',html)
publisher_list = re.findall('"publisher":"(.*?)"',html)
with open("信息.txt",'a',encoding='utf-8')as fp:
    for name,price,genre,time,publisher in zip(name_list,price_list,genre_list,releaseTime,publisher_list):
        fp.write("应用："+ name +'\n')
        fp.write("公司：" + publisher + '\n')
        fp.write("价格：" + price + '\n')
        fp.write("分类：" + genre + '\n')
        fp.write("时间：" + time + '\n'+'\n')





