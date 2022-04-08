#爬取我校主页所有新闻链接，并将链接放到一个列表里，将链接补充完整，根据新闻页面的网址爬取新闻内容存为文件
#主要练习requests  BeautifulSoup库的使用
# 以下代码仅供参考，字符编码异常页面需要特别处理
from bs4 import BeautifulSoup
import re
import requests

#第一步获取新闻标题和链接
url="http://www.hgu.edu.cn"
headers={
    "Host": "www.hgu.edu.cn",
    "Referer": "https://www.hgu.edu.cn",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 QIHU 360SE"}
response=requests.get(url,headers=headers)
if not response:
    print("请求失败，状态码为：",response.status)
html=response.content.decode()# 获取响应的文本
soup = BeautifulSoup(html,'html.parser')# 用html解析器


titlelist=[]#临时存储title
hreflist=[]  #临时存储href
datalist=[] # 以字典形式存储各个新闻标题和链接

divlist=['div[class="tab_box_hotnew"] a','div[class="tab_box_trends"] a']
for div in divlist:

    divtext=soup.select(div)#使用组合选择器找到新闻列表div下面所有的a 链接

    for a in divtext:
        titlelist.append(a['title'])
        hreflist.append("http://www.hgu.edu.cn/{}".format(a['href']))
    for t,h in zip(titlelist,hreflist):
        data={
            'title':t,
            'href':h
        }
        datalist.append(data)

        for d in datalist:
            title = d["title"]
            url = d["href"]
            with open("D:/PyTest/{}.txt".format(title), 'w') as f:
                response = requests.get(url, headers=headers)
                if not response:
                    print("请求失败，状态码为：", response.status)
                response.encoding = "utf-8"
                html = response.content.decode("utf-8")  # 获取响应的文本
                soup = BeautifulSoup(html, 'html.parser')  # 用html解析器
                try:
                    newstext = soup.select('div[class="v_news_content"]')[0].get_text()  # 使用组合选择器找到新闻列表div下面所有的a 链接
                    f.write(newstext)
                except IndexError as e:
                    print("爬取异常的新闻标题为：", title, "url:", url)
                except UnicodeEncodeError as e1:
                    print("爬取字符编码异常的新闻标题为：", title, "url:", url)