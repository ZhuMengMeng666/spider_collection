import re
import time
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from selenium import webdriver
from pyecharts.charts import Bar, Page, Pie, WordCloud
from pyecharts import options as opts
from selenium.webdriver import ActionChains


def csdn_spider(url):
    option = webdriver.ChromeOptions()
    #option.add_argument("headless"), chrome_options=option
    browser = webdriver.Chrome('E:\python\Scripts\chromedriver.exe')
    browser.get(url)
    browser.implicitly_wait(20)
    z=[]
    while len(z)<50:
        browser.execute_script('window.scrollBy(0,10000)')
        time.sleep(2)
        z = browser.find_elements_by_xpath("//div[@class='floor-rank-item']")
        print(len(z))
    a=browser.find_elements_by_xpath("//div[@class='floor-rank-item']//div[@class='hostitem floor']//div["
                                     "@class='box']//div[@class='hostitem-item-left']//span")
    Rank=[]#排名
    for i in a:
        Rank.append(int(i.text))
    #print(Rank)
    b=browser.find_elements_by_xpath("//div[@class='floor-rank-item']//div[@class='hostitem floor']//div["
                                     "@class='box']//div[@class='hostitem-item-middle']//div["
                                     "@class='hostitem-item-content']//div[@class='hosetitem-title']//a")
    href=[]#文章链接
    title=[]#标题
    for i in b:
        href.append(i.get_attribute('href'))
        title.append(i.text)
    #print(href)
    #print(title)
    c=browser.find_elements_by_xpath("//div[@class='floor-rank-item']//div[@class='hostitem floor']//div["
                                     "@class='box']//div[@class='hostitem-item-middle']//div["
                                     "@class='hostitem-item-content']//div[@class='hosetitem-dec']//span")
    info=[]
    for i in c:
        if len(i.text.split())!=0:
            info.append(int(i.text.split()[0]))
    #print(info)
    #print(info)
    liulan=info[0::3]#浏览量
    pinglun=info[1::3]#评论数
    shoucang=info[2::3]#收藏数
    d=browser.find_elements_by_xpath("//div[@class='floor-rank-item']//div[@class='hostitem floor']//div["
                                     "@class='box']//div[@class='hostitem-item-right']//div[@class='left']//span["
                                     "@class='num']")
    hot=[]#热度
    for i in d:
        hot.append(int(i.text))
    #print(hot)
    e=browser.find_elements_by_xpath("//div[@class='floor-rank-item']//div[@class='hostitem floor']//div["
                                     "@class='box']//div[@class='hostitem-item-right']//div[@class='right']//a["
                                     "@class='name']")
    author_href=[]#作者个人中心链接
    name=[]#作者名字
    for i in e:
        author_href.append(i.get_attribute('href'))
        name.append(i.text)
    #print(author_href)
    #print(name)
    Info=[]
    for i,j,k,l,m,n,o,p,q in zip(title,liulan,pinglun,shoucang,name,author_href,href,Rank,hot):
        zong={
            'rand':p,
            'title':i,
            'liulan':j,
            'pinglun':k,
            'shoucang':l,
            'hot':q,
            'name':m,
            'a_href':n,
            'href':o
        }
        Info.append(zong)
    # for i in Info:
    #     print(i)

if __name__ == '__main__':
    url='https://blog.csdn.net/rank/list/content?type=java'
    csdn_spider(url)