# -*- coding: utf-8 -*-

import TFIDF
import xlrd
import xlwt
import rw_new
import random
import w2v_use
import cut
import re
import pandas as pd
import os
from xlutils.copy import copy
import math

# 根据编号读新闻
filepath = 'news.xls'
user_fpath='user.xls'

#1.建立用户兴趣词表
#读取用户浏览的最后一次新闻
num=random.randint(1,100)
text,time,title=rw_new.rd(filepath,num,'国内')
# print(title)
# print(text)
# print(time)
#获得时间
strout=str(time)
user_times=strout[6:17]
user_times=user_times[0:4]+'-'+user_times[5:7]+'-'+user_times[8:10]
# print(user_times[-2::])#日
# print(user_times[5:7])#月

#限制词汇
new_file = xlrd.open_workbook(user_fpath)

sheet = new_file.sheet_by_name(sheet[0])

row=sheet.nrows

if row<10000:
    try:
        keyword = TFIDF.tfidf(text)

        # 得到兴趣程度和衰减程度，兴趣程度为相似度，衰减的初值=相似度.时间为正则表达式
        for word in keyword:
            try:
                l = w2v_use.w2v_topk(word)
                rw_new.wt(l, user_fpath, user_times)
            except KeyError:
                continue
    except BaseException:
        print('基础词表建立失败')
# #兴趣词表初步建立完成

#通过时间判断衰减程度





#2.读取3天里的所有新闻
# num=random.randint(1,100)


text,time,title=rw_new.rd_all(filepath)
num=len(time)
# print(num)
strout={}

out_text={}#文章
out_title={}#标题
out_time={}#时间
num_list=0

for i in range(1,num):
    strout[i] = str(time[i])
    # print(strout[i])
    times = strout[i][6:17]
    times = times[0:4] + '-' + times[5:7] + '-' + times[8:10]
    # print (times)
    strout[i]=times
    sim={}
    count=0#关键词计数
    try:
        if int(times[8:10]) - int(user_times[-2::]) > -2 and int(times[8:10]) - int(
                user_times[-2::]) < 2:  # 用户最后一次浏览时间与新闻的时间判断 2
            # 符合时间的标准
            keyword = TFIDF.tfidf(text[i])
            for line in keyword:

                new_file = xlrd.open_workbook(user_fpath)

                sheet = new_file.sheet_by_name('user')
                row = sheet.nrows
                for j in range(1, row):
                    words = sheet.cell(j, 0)
                    word = str(words).lstrip('text:')
                    word2 = eval(word)
                    word1 = line
                    # print(word1)
                    try:
                        if word1 == word2:  # 关键词相等，说明相匹配，将该新闻推荐给他
                            count = 1  #
                            num_list += 1
                            break
                    except KeyError:
                        continue
            if count == 1:
                out_text[num_list] = text[i]
                out_title[num_list] = title[i]
                out_time[num_list] = strout[i]
    except ValueError:
        continue
path='new_list.xls'

print(out_text)
print(out_title)
workbook = xlrd.open_workbook(path,formatting_info=True)  # 打开
sheets = workbook.sheet_names()  # 获取表中所有表格数据
worksheet = workbook.sheet_by_name(sheets[0])

length=len(out_text)
rows_old = worksheet.nrows

new_sheet = copy(workbook)  # 将xlrd对象拷贝过去转化为xlwt对象

new_worksheet = new_sheet.get_sheet(0)
i=0
try:
  for key in out_title:
      print('111')
      print(out_title[key])
      rows_old =worksheet.nrows
      new_worksheet.write(i+rows_old, 0, out_title[key].value)
      new_worksheet.write(i + rows_old, 1, out_text[key].value)
      i+=1

except KeyError:
    print('未匹配到推荐新闻')
new_sheet.save(path)
# print(strout)#时间
# print(text)#新闻
# print(title)#标题

# # keyword=TFIDF.tfidf(text)
#
# print(keyword,time,title)