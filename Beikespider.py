import time
import  requests
from bs4 import BeautifulSoup as bs
import  pandas
def text(page):
    url='https://sjz.ke.com/ershoufang/yuhua1/pg{}/'.format(page)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
    }
    soup=requests.get(url=url,headers=headers)
    save = soup.content.decode('utf-8')
    shuju = bs(save, 'html.parser')
    a=shuju.select('ul.sellListContent>li.clear>div>div>a') #房子标题
    b=shuju.select('ul.sellListContent>li.clear>div>div>div>div>a') #房子小区名
    c=shuju.select('ul.sellListContent>li.clear>div>div.address>div.houseInfo')
    d=shuju.select('ul.sellListContent>li.clear>div>div.address>div.followInfo')
    e=shuju.select('ul.sellListContent>li.clear>div>div.address>div.priceInfo>div.totalPrice.totalPrice2>span')#房价
    f=shuju.select('ul.sellListContent>li.clear>div>div.address>div.priceInfo>div.unitPrice>span')#房价单价
    g=shuju.select('ul.sellListContent>li.clear>a.img.CLICKDATA.maidian-detail')
    for i in a:
        title.append(i['title'])
    for i in b:
        xiaoqu.append(i.get_text())
    for i in c:
        z=i.get_text().split()
        str=''
        for j in z:
            str += j
        tedian.append(str)
    for i in d:
        z=i.get_text().split()
        str = ''
        for j in z:
            str += j
        xinxi.append(str)#发布信息时间以及关注人数
    for i in e:
        price.append(i.get_text()+'万')
    for i in f:
        uprice.append(i.get_text())
    for i in g:
        #print('*'*20)
        href.append(i['href'])
    for a,b,c,d,e,f in zip(title,xiaoqu,tedian,xinxi,price,uprice):
        z={
            'title':a,
            'xiaoqu':b,
            'tedian':c,
            'xinxi':d,
            'price':e,
            'uprice':f,
            'href':g
        }
        info.append(z)
def save():
    z = {'标题': title, '小区': xiaoqu, '特点': tedian, '信息': xinxi, '价格': price, '单价': uprice,'链接':href}
    dm_file = pandas.DataFrame(z)
    # dm_file.to_excel('Dongman.xlsx', sheet_name="动漫数据分析")
    dm_file.to_csv("房价1.1.csv", encoding='utf-8-sig', index=True, index_label='序号')
if __name__ == '__main__':
    info=[]
    title = []
    xiaoqu = []
    tedian = []
    xinxi = []
    price = []
    uprice = []
    xuhao=[]
    href=[]
    z=input('请输入开始爬取页数：')
    k=input('请输入结束爬取页数：')
    for i in range(int(z),int(k)+1):
        print('开始爬取{}页数据,请勿关机或停止该程序'.format(i))
        try:
            text(i)
            print('第{}页已爬取完毕'.format(i))
            time.sleep(5)
        except  Exception as e:
            print('错误为：'+e)
        time.sleep(2)
    save()
    print('信息已保存完毕,文件存储位置为当前程序所在文件夹,祝君开心')