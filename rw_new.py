import xlrd
import xlwt
from xlutils.copy import copy

#读取某篇新闻
def rd(filepath,num,sheet):
    text = ''

    new_file = xlrd.open_workbook(filepath)

    sheet = new_file.sheet_by_name(sheet)

    text = sheet.cell(num, 1)
    time = sheet.cell(num, 4)
    title = sheet.cell(num,5)
    return text,time,title


#读取当天全部新闻
def rd_all(filepath):
    text = {}
    time ={}
    title={}
    new_file = xlrd.open_workbook(filepath)

    sheet = new_file.sheet_by_name('国内')
    row=sheet.nrows
    col=sheet.ncols
    print(row)#行
    print(col)#列
    for i in range(1,row):
        text[i] = sheet.cell(i, 1)
        time[i] = sheet.cell(i, 4)
        title[i] = sheet.cell(i, 5)
    return text,time,title
#写入词表
def wt(value,user_fpath,time):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(user_fpath,formatting_info=True)  # 打开
    sheets = workbook.sheet_names()  # 获取表中所有表格数据
    worksheet = workbook.sheet_by_name(sheets[0])
    rows_old = worksheet.nrows

    new_sheet = copy(workbook)  # 将xlrd对象拷贝过去转化为xlwt对象

    new_worksheet = new_sheet.get_sheet('user')

    # new_sheet.add_sheet('user3')#创建新表
    for i in range(0, index):
        if value[i][1]>=0.6:#相似度>0.7，表示该词用户感兴趣，添加进兴趣词表里
            new_worksheet.write(i + rows_old, 0,value[i][0])#兴趣词
            new_worksheet.write(i + rows_old, 1,value[i][1])#相似度
            new_worksheet.write(i + rows_old, 2,value[i][1])#相似度
            new_worksheet.write(i + rows_old, 3,time)  # 时间
        else:
            continue
    new_sheet.save('user.xls')



    # print(times[-2::])  # 日
    # print(times[5:7])  # 月

# print(strout)
# print(title)
# print(text)