from openpyxl import load_workbook
from openpyxl import Workbook
import sys,os
# import getpass

def write_to_excel():
    print(os.path)
    wb = load_workbook('F:\\autoTest_workspace\\python_code\\e2e-test\\test_data\\写入数据.xlsx')
    sheet = wb.get_sheet_by_name('已创建的公司')
    sheet['A4'] = '来连连看'
    wb.save(os.path.dirname(__file__) + '/../test_data/' +'写入数据.xlsx')
    print('write success')

def read_excel():
    wb = load_workbook('写入数据.xlsx')
    sheet = wb.get_sheet_by_name('已创建的公司')
    print(sheet['A2'].value)

# write_to_excel()
read_excel()