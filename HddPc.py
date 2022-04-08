import requests
import  re
from bs4 import BeautifulSoup
def save():
    url="http://www.hgu.edu.cn"
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
    }
    soup=requests.get(url=url,headers=headers)
    save=soup.content.decode('utf-8')
    shuju=BeautifulSoup(save,'html.parser')
    for i in shuju.find_all('a',target="_blank"):
        #print(i)
        if i.find('span')!=None:
            #获取url
            res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
            #获取url中的文字信息
            res = r'<a.*?>(.*?)<span>'
            link = re.findall(res_url, str(i), re.I | re.S | re.M)
            mm = re.findall(res, str(i), re.S | re.M)
            print(url+"/"+link[0]+":"+mm[0])



def xinxi():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
    }
    url="http://www.hgu.edu.cn/info/1089/10407.htm"
    soup = requests.get(url=url, headers=headers)
    save = soup.content.decode('utf-8')
    neirong = BeautifulSoup(save, 'html.parser')
    for i in neirong.find_all('p'):
        #if i.find(style="text-align: center;")==None:
            #print(i)
            print(i)


        #print(i.text)




def main():

    save()
    #print(html)
    #xinxi()

if __name__ == '__main__':
    main()