import xlrd
import xlwt
from xlutils.copy import copy
import math

day = 19

user_fpath='user.xls'
#衰减系数
a=0.9
new_file = xlrd.open_workbook(user_fpath)
sheets = new_file.sheet_names()  # 获取表中所有表格数据
sheet = new_file.sheet_by_name(sheets[0])
new_sheet = copy(new_file)  # 将xlrd对象拷贝过去转化为xlwt对象

new_worksheet = new_sheet.get_sheet('user')
row = sheet.nrows
for i in range(1,row):
    time = sheet.cell(i, 3).value
    sim=sheet.cell(i,2).value
    num=int(time[-2::])
    if num-day==1 or num-day==-1:
        print(sim)
        sim=math.pow(sim*10,a)
        print('1111')
        print(sim)
        new_sheet = copy(new_file)  # 将xlrd对象拷贝过去转化为xlwt对象

        new_worksheet = new_sheet.get_sheet('user')
        new_worksheet.write(i,2,sim/10)

        new_sheet.save('user.xls')
        new_file = xlrd.open_workbook(user_fpath)
        sheets = new_file.sheet_names()  # 获取表中所有表格数据
        sheet = new_file.sheet_by_name(sheets[0])
        sim_r=sheet.cell(i,2).value
        print(sim_r)
