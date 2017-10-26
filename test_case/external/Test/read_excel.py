import xlrd

class readExcel(object):

    def __init__(self,path):
        self.path = path

    @property
    def get_sheet(self):
        # 获得索引
        x1 = xlrd.open_workbook(self.path)
        sheet = x1.sheet_by_index(0)
        return sheet

    @property
    def get_row(self):
        # 获得行数
        row = self.get_sheet.nrows
        return row

    @property
    def get_col(self):
        # 获得列数
        col = self.get_sheet.ncols
        return col

    # 分别获取每一列的数值
    @property
    def get_name(self):
        TestName = []
        for i in range(1,self.get_row):
            TestName.append(self.get_sheet.cell_value(i,0))
        return TestName

    @property
    def get_data(self):
        TestData = []
        for i in range(1,self.get_row):
            TestData.append(self.get_sheet.cell_value(i,1))
        return TestData
    
    @property
    def get_url(self):
        TestUrl = []
        for i in range(1,self.get_row):
            TestUrl.append(self.get_sheet.cell_value(i,2))
        return TestUrl

    @property
    def get_method(self):
        TestMethod = []
        for i in range(1,self.get_row):
            TestMethod.append(self.get_sheet.cell_value(i,3))
        return TestMethod

    @property
    def get_uid(self):
        TestUid = []
        for i in range(1,self.get_row):
            TestUid.append(self.get_sheet.cell_value(i,4))
        return TestUid

    @property
    def get_code(self):
        TestCode = []
        for i in range(1,self.get_row):
            TestCode.append(self.get_sheet.cell_value(i,5))
        return TestCode