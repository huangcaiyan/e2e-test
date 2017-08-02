# import hashlib
# import itertools

# def test():
#     md5 = hashlib.md5()
#     md5.update('how to use md5 in python hashlib'.encode('utf-8'))
#     print(md5.hexdigest())

# def test1():
#     sha1 = hashlib.sha1()
#     sha1.update('qq123456'.encode('utf-8'))
#     print(sha1.hexdigest())

# def test3():
#     natuals = itertools.count(1)
#     for n in natuals:
#         print(n)

# def test4():
#     cs = itertools.cycle('abc')
#     for c in cs:
#         print(c)

# def test5():
#     outcome = [['1','现金','内部代表'],
#     ['1','招商银行','内部代表'],
#     ['1','羊羊羊微信','内部代表'],
#     ['1','羊羊羊支付宝','内部代表']]
#     ns = itertools.repeat(outcome,3)
#     for n in ns:
#         print(n)
    
# def test6():
#     natuals = itertools.count(1)
#     ns = itertools.takewhile(lambda x:x<=10,natuals)
#     print('sds' + str(list(ns)))

# def test7():
#     for key,group in itertools.groupby('AAABBBCCAA'):
#         print(key,list(group))

# test7()
# class Query(object):

#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print('Begin')
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')

#     def query(self):
#         print('Query info about %s...' % self.name)
# with Query('Bob') as q:
#     q.query()
# from openpyxl.reader.excel import load_workbook
import xlrd
def test():
    wb = xlrd.open_workbook('F:\\autoTest_workspace\\python_code\\e2e-test\\test_data\\收支.xlsx') # 打开文件  
    # sh = wb.sheet_by_name('考试成绩')  
    # sh=wb.sheet_by_index(0)#第一个表  
    sh = wb.sheet_by_name(u'记收入测试数据')
    # sheetNames = wb.sheet_names() # 查看包含的工作表  
    # 获得工作表的两种方法  
    # sh = wb.sheet_by_index(0)  
    # sh = wb.sheet_by_name(u'Sheet1')  
    # 单元格的值  
    # cellA1 = sh.cell(0,0)  
    # cellA1Value = cellA1.value  
    # # 第一列的值  
    # for r in sh.get_rows():
    #     print(r)

    incomePara = []
    for i in range(1,sh.nrows):
        # print(i)
        rowValueList = sh.row_values(i)
        if '利息收入' == rowValueList[3]:
            rowValueList[3] = ['1','1']
        if '回收借出资金(收入)' == rowValueList[3]:
            rowValueList[3] = ['2','1'] 
        # incomePara.append(rowValueList)
        # for row in rowValueList:
        #     if '利息收入' == row[3]:
        #         row[3] = ['1','1']
        #     if '回收借出资金(收入)' == row[3]:
        #         row[3] = ['2','1']
        print(rowValueList)

    # rowValueList = sh.row_values(1)
    # print(rowValueList)
    
    # colVList = sh.col_values(3)
    # for col in colVList:
    #     if '利息收入' == col：


test()
