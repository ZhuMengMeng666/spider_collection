import time

import requests
from bs4 import BeautifulSoup as bs
import re
import os
#url='https://www.51shucheng.net/wuxia'
#<4>对每一章节的链接进入进行爬取内容
def novel_text(path,name,url):
    #爬取每一章小说具体内容
    #url="https://www.51shucheng.net/wuxia"
    print(path)
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
    }
    soup=requests.get(url=url,headers=headers)
    save=soup.content.decode('utf-8')
    shuju=bs(save,'html.parser')
    a=shuju.select('div.neirong>p')

    with open(path+"\{}.txt".format(name),'w') as f:
        for i in a:
            f.write(i.get_text())
            f.write('\r\n')
def novel_chapter_url(urls):
    #爬取每一小说章节链接
    #urls='https://www.51shucheng.net/wuxia/xueshanfeihu'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
    }
    soup = requests.get(url=urls, headers=headers)
    save = soup.content.decode('utf-8')
    shuju = bs(save, 'html.parser')

    a=shuju.select('div.mulu-list>ul>li>a')
    #print(a)

    if len(a) == 0:
        a = shuju.select('div.mulu-list-2>ul>li>a')
        #print(a)
    shuju = []
    for i in a:
        xiaoshuo_info = {
            'title': i['title'],
            'href': i['href']
        }
        shuju.append(xiaoshuo_info)
    #print(shuju)
    return shuju
def novel_name_url():
    #爬取小说链接
    url = 'https://www.51shucheng.net/wuxia'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
    }
    soup = requests.get(url=url, headers=headers)
    save = soup.content.decode('utf-8')
    shuju = bs(save, 'html.parser')
    a=shuju.select('div.mulu-list>ul>li>a')
    for i in a:
        novel_url.append(i['href'])
        novel_name.append(i.get_text())
if __name__ == '__main__':
    path = 'D:\Textspider'
    # <1>主页下的分类专区名称以及链接
    partition_name = []
    partition_url = []
    # <2>分类专区下的具体书名以及链接
    novel_name = []
    novel_url = []
    # <3>书籍信息下的章节名称以及链接

    #进行信息存储
    novel_info=[]
    novel_name_url()
    for i,j in zip(novel_name,novel_url):
        print(i+':'+j)
    for i,j in zip(novel_name,novel_url) :
        print('正在存储'+i+'信息')
        z=novel_chapter_url(j)
        print(z)
        info={
            'name':i,
            'href':j,
            'info':z
        }
        time.sleep(2)
        novel_info.append(info)
        print(i+'信息存储成功')
    #根据存储信息进行数据爬取
    for i in novel_info:
        z=path+'\\'+i['name']

        try:
            if not os.path.exists(z):
                os.mkdir(z)
                print(z + '已创建')
            else:
                print(z+'路径已存在')
        except Exception as e:
            print(z+'路径创建失败或者路径已存在')
            print('错误信息：'+e)
        print('存储路径：' + z)
        for j in i['info']:
            print(j)

            title=j['title']
            href=j['href']
                #print('ceshi')
            try:
                print('小说标题：'+title)
                print('下载路径：'+href)
                novel_text(z, title, href)
                print(j['title'] + '已下载完成!!!')
                time.sleep(5)
            except:
                print(j['title'] + '下载失败')