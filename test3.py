import requests
from bs4 import BeautifulSoup
import json
import pandas
import time
import xlwt
def getNewsDetail(newsurl): #得到某个新闻的全部信息
    result = {}
    try:
        res = requests.get(newsurl,timeout=0.5)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        result['title'] = soup.select('.main-title')[0].text
        if len(soup.select('.date-source a')):
            result['newssource'] = soup.select('.date-source a')[0].text
        else:
            result['newssource'] = soup.select('.date-source .source')[0].text
        result['time'] = soup.select('.date')[0].text
        result['article'] = ' '.join([p.text.strip() for p in soup.select('#article p')[:-2]])
        result['editor'] = soup.select('.show_author')[0].text.strip("责任编辑：")
        result['comments'] = getCommentCount(newsurl)
        return result
    except Exception as e:
        return result

def parseListLinks(url): #得到某页新闻的信息
    newsdetails = []
    res = requests.get(url,headers=headers)
    print(res)
    print(res.text)
    jdata=res.text.lstrip('try{feedCardJsonpCallback(').rstrip('catch(e){};')
    # print(jdata)
    str = '{'+jdata+'}}'
    # print(str)
    jd = json.loads(str)
    # print(jd)
    for ent in jd['result']['data']:
        newsdetails.append(getNewsDetail(ent['url']))
    return newsdetails


url1='https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4363153913276127&root_comment_max_id=139796972637328&root_comment_max_id_type=0&root_comment_ext_param=&page=8&filter=hot&sum_comment_number=2346&filter_tips_before=0&from=singleWeiBo&__rnd=1555752117907'
news_total = []
headers = {'Cookies':'Your cookie',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5558.400 QQBrowser/10.1.1695.400'}
# 在requests中加入headers


    # newsurl = url1.format(i,int(time.time() * 100000))
newsurl=url1

res = requests.get(newsurl,headers=headers)

print(res.text)

# columns=['Id','Title','Content']
df = pandas.DataFrame(news_total)
df.to_excel('news.xls')

