import xlrd
import unittest

"""
读取excel
更新于 2017-12-08-五
"""


class ReadExcel(object):
    def __init__(self, file_dir):
        self.file_dir = file_dir

    def get_value_in_order(self, sheet_name):
        """
        顺序获取整个sheet的值
        :param sheet_name:sheet的名字或者索引；
        :return:返回这个table的值；
        """
        data = xlrd.open_workbook(self.file_dir)
        if type(sheet_name) == int:
            table = data.sheet_by_index(sheet_name)
        elif type(sheet_name) == str:
            table = data.sheet_by_name(sheet_name)
        else:
            table = None
        nrows = table.nrows
        ncols = table.ncols
        table_value = []
        for rownum in range(1, nrows):
            row_value = []
            for colnum in range(ncols):
                cel_value = table.cell(rownum, colnum).value
                row_value.append(cel_value)
            table_value.append(row_value)
        return table_value

    def get_value_by_row(self, sheet_name, row_num):
        """
        顺序获取指定行的值
        :param sheet_name: sheet的名字或者索引；
        :param row_num: 行号索引；
        :return: 返回某一行的所有值；
        """
        data = xlrd.open_workbook(self.file_dir)
        if type(sheet_name) == int:
            table = data.sheet_by_index(sheet_name)
        elif type(sheet_name) == str:
            table = data.sheet_by_name(sheet_name)
        else:
            table = None
        ncols = table.ncols
        row_value = []
        for colnum in range(ncols):
            cel_value = table.cell_value(row_num, colnum)
            row_value.append(cel_value)
        return row_value


# 测试读取excel函数
class ReadExcelTest(unittest.TestCase):
    def setUp(self):
        self.file_dir = '../test_data/cai/login_test_data.xlsx'

    def tearDown(self):
        pass

    def test_get_value_in_order(self):
        read_excel = ReadExcel(self.file_dir)
        table_data = read_excel.get_value_in_order('stage')
        print('table_data1=>', table_data)

    def test_get_value_by_row(self):
        read_excel = ReadExcel(self.file_dir)
        row_data = read_excel.get_value_by_row('stage', 2)
        print('row_data2=>', row_data)


if __name__ == '__main__':
    unittest.main()
    # suites = unittest.TestSuite()

    # suites.addTest(ReadExcelTest('test_get_value_in_order'))
    # suites.addTest(ReadExcelTest('test_get_value_by_row'))
