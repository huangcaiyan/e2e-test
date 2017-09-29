import xlrd
import xlwt
from datetime import date, datetime


class ReadExcel(object):
    def __init__(self, file_dir):
        self.file_dir = file_dir

    # 获取所有sheets
    def get_sheets(self):
        workbook = xlrd.open_workbook(self.file_dir)
        return workbook.sheets()

    # 顺序获取所有excel单元格值
    def get_value_in_order(self, sheet_index):
        sheets = self.get_sheets()
        print(sheets)
        values = []
        s = sheets[sheet_index]
        # print('s=', s)
        for row in range(s.nrows):
            if row != 0:
                col_value = []
                for col in range(s.ncols):
                    value = (str(s.cell(row, col).value))
                    col_value.append(value)
                values.append(col_value)
        print('values=>', values)
        return values

    # 读取某一sheet中的某一行的值
    def get_value_by_row(self, sheet_index, row_index):
        sheets = self.get_sheets()
        values = []
        s = sheets[sheet_index]
        print('sheet_index=>', sheet_index)
        print('row_index=>', row_index)
        for row in range(row_index):
            if row != 0:
                col_value = []
                for col in range(s.ncols):
                    value = (str(s.cell(row, col).value))
                    col_value.append(value)
                values.append(col_value)
        print('values=>', values)
        return values
