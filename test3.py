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

num=100
filepath = 'news.xls'
sheet='test'
user_fpath='user.xls'
num_list=0
out_text={}#文章
out_title={}#标题
out_time={}#时间

for i in range(1,num):
    try:
            text,time,title=rw_new.rd(filepath,i,sheet)
            keyword = TFIDF.tfidf(text)
            count = 0
            for line in keyword:
                new_file = xlrd.open_workbook(user_fpath)
                sheet1 = new_file.sheet_by_name('user')
                row = sheet1.nrows
                for j in range(1, row):
                    words = sheet1.cell(j, 0)
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
                out_text[num_list] = text
                out_title[num_list] = title
                out_time[num_list] = time
    except ValueError:
        continue

path='new_list_test.xls'

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
