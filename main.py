import re
import requests
from bs4 import BeautifulSoup
def bspider(url):
    #全站，国创相关，动画，音乐，舞蹈，游戏，知识，科技，运动，汽车，生活，美食，动物圈，鬼畜，时尚，娱乐，影视，原创，新人
    tscore = []  # 综合评分
    name = []  # 视频名称
    bfl = []  # 播放量
    pls = []  # 评论数
    author = []  # 作者
    href=[]#视频链接
    video_list_info = []  # 综合存储
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    for tag in soup.find_all('div', class_='info'):
        bf = tag.a.string
        name.append(str(bf))
    for tag in soup.find_all('div', class_='detail'):
        bf = tag.find('span', class_='data-box').get_text()
        if '亿' in bf:
            num = float(re.search(r'\d(.\d)?', bf).group()) * 10000
            bf = num
        else:
            bf = re.search(r'\d*(\.)?\d', bf).group()
        bfl.append(float(bf))
    for tag in soup.find_all('div', class_='detail'):
        pl = tag.find('span', class_='data-box').next_sibling.next_sibling.get_text()
        if '万' not in pl:
            pl = '%.1f' % (float(pl) / 10000)
        else:
            pl = re.search(r'\d*(\.)?\d', pl).group()
        pls.append(float(pl))
    for tag in soup.find_all('div', class_='pts'):
        zh = tag.find('div').get_text()
        tscore.append(int(zh))
    n = soup.select('div.detail>a>span')
    for i in n:
        a = i.text.strip().split('\n')
        author.append(a[0])
    for i in soup.select('ul.rank-list>li>div.content>div.info>a'):
        href.append('https:' + i['href'])
    for i in href:
        print(i)
    for i, j, k, l, p in zip(name, author, bfl,pls,tscore):
        video_info = {
            'name': i,
            'author': j,
            'bfl': k,
            'pls': l,
            'tscore': p
        }
        video_list_info.append(video_info)
    return video_list_info
if __name__ == '__main__':
    url = 'https://www.bilibili.com/v/popular/rank/bangumi'
    bspider(url)
