#!/usr/bin/env python
# coding: utf-8
#https://www.xiaomiyoupin.com/detail?gid=123534&pid=315064&spmref=YouPinPC.$Home$.list.0.46309913
import re
import time
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from selenium import webdriver
from pyecharts.charts import Bar, Page, Pie, WordCloud
from pyecharts import options as opts
def get_href(key):
    Info=[]
    info_title=[]
    info_jieshao=[]
    info_href=[]
    info_price=[]
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    browser = webdriver.Chrome('E:\python\Scripts\chromedriver.exe', chrome_options=option)
    url='https://www.xiaomiyoupin.com/search?keyword={}'.format(key)

    browser.get(url)
    browser.implicitly_wait(20)
    info1=browser.find_elements_by_xpath("//div[@class='m-product-list  clearfix']/div//p[@class='pro-info']")
    for i in info1:
        info_title.append(i.get_attribute("title"))
    #print(info_title)
    info2 = browser.find_elements_by_xpath("//div[@class='m-product-list  clearfix']/div//p[@class='pro-desc']")
    for i in info2:
        info_jieshao.append(i.get_attribute("title"))
        #print(i.get_attribute("title"))
    info3 = browser.find_elements_by_xpath("//div[@class='m-product-list  clearfix']/div")
    for i in info3:
        info_href.append(i.get_attribute("data-src"))
    #print(info_href)
    info4 = browser.find_elements_by_xpath("//div[@class='m-product-list  clearfix']/div//p["
                                           "@class='pro-price']//span[@class='m-num']")
    for i in info4:
         info_price.append(i.text)
    for i,j,k,l in zip(info_title,info_jieshao,info_price,info_href):
        a={
            'title':i,
            'introduce':j,
            'price':k,
            'url':l
        }
        Info.append(a)
    # for i in Info:
    #     print(i['introduce'])
    return Info
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#爬取特点信息
def get_tedian_info(url):
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    browser = webdriver.Chrome('E:\python\Scripts\chromedriver.exe', chrome_options=option)
    browser.get(url)
    name=[]
    number=[]
    Info=[]
    browser.implicitly_wait(20)
    browser.find_element_by_xpath("//div[@class='detail-content']//div[@class='info fl']//div["
                                        "@class='nav-title']/ul/*[2]").click()
    info = browser.find_element_by_xpath("//div[@class='tabbar-container']")
    time.sleep(2)
    z1=info.text.split()
    for i in z1:
        z = r'[(|)]'
        c=re.split(z,i)
        name.append(c[0])
        number.append(c[1])
    for i,j in zip(name,number):
        dio={
            'name':i,
            'number':j
        }
        Info.append(dio)
    browser.quit()
    return Info
def go(n,key):
    Info = []  # ————————>总信息字典
    info_title_href_intr = []  # 产品标题，介绍，链接——————————>存储字典
    info_Features = []  # 产品特点————————>存储字典
    info_zong = []
    a = []
    b = []
    c = []
    d = []
    try:
        info_title_href_intr = get_href(key)
    except Exception as e:
        print('错误为:' + e)
    jishu = 0
    print('搜索到{}条商品:'.format(len(info_title_href_intr)))
    for i in info_title_href_intr:
        print(i['title'])
    print('即将开始爬取，请勿关机或暂停')

    for i in info_title_href_intr[0:n]:
        print('开始爬取:' + i['title'])
        try:
            info_Features = get_tedian_info(i['url'])
            info_zong.append(info_Features)
            print(i['title'] + '爬取完毕')
        except Exception as e:
            print('出现错误为:' + e)
        time.sleep(2)
    print('目标爬取完毕')
    for i in info_title_href_intr[0:n]:
        a.append(i['title'])
        b.append(i['introduce'])
        c.append(i['price'])
        d.append(i['url'])
    for i, j, k, l, m in zip(a, b, c, d, info_zong):
        g = {
            'title': i,
            'introduce': j,
            'price': k,
            'url': l,
            'F': m
        }
        Info.append(g)
    # for i in Info:
    #     print(i)
    return Info,info_title_href_intr

def echarts_bar(Info):
    title=[]
    intr=[]
    price=[]
    for i in Info[1]:
        title.append(i['title'])
        intr.append(i['introduce'])
        price.append(i['price'])

    page = Page(layout=Page.DraggablePageLayout)
    bar = (
        Bar(init_opts=opts.InitOpts(width='1000px', height='700px', theme=ThemeType.MACARONS))
            .add_xaxis(title)
            .add_yaxis("价格", price, color="#19CAAD")
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: '#81FFEF'
                    }, {
                        offset: 1,
                        color: '#F067B4'
                    }], false)"""),
                    "barBorderRadius": [6, 6, 6, 6],
                    "shadowColor": 'rgb(0, 160, 221)',
                }},
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ), markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="min", name="最小值"),
                    opts.MarkLineItem(type_="max", name="最大值")
                ]
            ))
            .set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                             xaxis_opts=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_show=True),
                                                      axislabel_opts=opts.LabelOpts(rotate=-90)
                                                      ),
                             title_opts=opts.TitleOpts(title="商品价格柱形图", subtitle="从左往右随机排列")

                             )

    )

    bar.set_series_opts(label_opts=opts.LabelOpts(font_size=10, font_style='italic'))
    page.add(bar)
    page.render('E://搜索商品信息价格表.html')

def echarts_wordcloud_pie(Info,n):
    #print(n)
    title=[]
    intr=[]
    price=[]
    for i in Info[1]:
        title.append(i['title'])
        intr.append(i['introduce'])
        price.append(i['price'])

    page = Page(layout=Page.DraggablePageLayout)

    tedian_zong = Info[0]
    tedian_first = tedian_zong[n]
    tedian = []
    number = []
    for i in tedian_first['F']:
        if(i['name']!='全部'):
            tedian.append(i['name'])
            number.append((int(i['number'])))
    bar2 = (
        Pie(init_opts=opts.InitOpts(width='1300px', height='600px', theme=ThemeType.LIGHT))
            .add(
            title[0],
            [list(z) for z in zip(tedian, number)],
            radius=["40%", "75%"],
            center=["59%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=True,
                                      # position 标签的位置
                                      position="outside",
                                      ),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="{}特点信息饼状图".format(title[n]), subtitle="信息仅供参考"),
            legend_opts=opts.LegendOpts(
                orient="vertical",  # 图例垂直放置
                pos_top="10%",  # 图例位置调整
                pos_left="2%"),
        )
    )
    #print(list(zip(tedian, number)))
    bar3=(
        WordCloud(init_opts=opts.InitOpts(width='1300px', height='600px', theme=ThemeType.LIGHT))
        .add(
        "",
        list(zip(tedian, number)),
            #词云图字体大小范围
        word_size_range=[50, 200],
             # 字体风格
        textstyle_opts=opts.TextStyleOpts(font_family="Arial"),
         # 阴影
        emphasis_shadow_color = "white",
        shape='circle'
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="{}特点信息词云".format(title[n]), subtitle="信息仅供参考"),
            legend_opts=opts.LegendOpts(
                orient="vertical",  # 图例垂直放置
                pos_top="10%",  # 图例位置调整
                pos_left="2%"),
        )
    )

    page.add(bar2,bar3)
    page.render('E://{}.html'.format(title[n]))


if __name__ == '__main__':
    Info=[]
    key = input('请输入想要查询的关键字:')
    n=int(input('请输入查看个数:'))
    Info=go(n,key)
    print('正在生成信息柱状图')
    echarts_bar(Info)
    for i in range(n):
        echarts_wordcloud_pie(Info,i)







