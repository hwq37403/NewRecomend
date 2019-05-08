import requests
from bs4 import BeautifulSoup
import json
import pandas
import time
import xlwt
import xlrd
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
    res = requests.get(url)
    print(res.text)
    jdata=res.text.lstrip('try{feedCardJsonpCallback(').rstrip('catch(e){};')
    print(jdata)
    str = '{'+jdata+'}}'
    print(str)
    jd = json.loads(str)
    # print(jd)
    for ent in jd['result']['data']:
        newsdetails.append(getNewsDetail(ent['url']))
    return newsdetails


url1='https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&versionNumber=1.2.4&page={}&encode=utf-8&callback=feedCardJsonpCallback&_={}'

news_total = []
for i in range(1,1000):
    newsurl = url1.format(i,int(time.time() * 1000))
    newsary = parseListLinks(newsurl)
    news_total.extend(newsary)


# columns=['Id','Title','Content']
df = pandas.DataFrame(news_total)
workbook = xlrd.open_workbook('news.xls', formatting_info=True)  # 打开
sheets = workbook.sheet_names()  # 获取表中所有表格数据
worksheet = workbook.sheet_by_name(sheets[1])
rows_old = worksheet.nrows
df.to_excel('newss.xls',startrow=rows_old)

