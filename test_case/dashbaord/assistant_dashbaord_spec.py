import unittest,sys,os
from selenium import webdriver
from time import sleep
import xlrd
from openpyxl import load_workbook
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from config import *
from .assistant_dashbaord_page import AssistantDashbaordPage
from util.enter_company_util import EnterCompany
from test_case.import_file.import_output_invoice_file import ImportOutputInvoiceFile
from test_case.import_file.import_bank_bill_file import ImportBankBillFile
from test_case.import_file.import_staff_file import ImportStaffFile


class AssistantDashbaordSPec(unittest.TestCase):
    '''助理首页测试'''

    @classmethod
    def setUpClass(self):
        # self.driver = Driver
        self.driver = webdriver.Chrome()
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '创建公司.xlsx')
        loginSh = wb.sheet_by_name(u'登陆账号')
        loginData = loginSh.row_values(1)
        wb1 = load_workbook('写入数据.xlsx')
        sheet = wb1.get_sheet_by_name('已创建的公司')
        companyName = sheet['A2'].value
        loginData.append(companyName)
        EnterCompany(self.driver,[BaseUrl,loginData])

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test1(self):
        '''导入开票'''
        dashboardPage = AssistantDashbaordPage(self.driver)
        dashboardPage.clickImportOutputInvoiceButton()
        importFile = ImportOutputInvoiceFile(self.driver)
        importFile.importOutputInvoiceFile('F:\\autoTest_workspace\\python_code\\e2e-test\\test_data\\导入开票(一般纳税人).xlsx')
        # importFile.importOutputInvoiceFile(os.path.dirname(__file__) + '/../../test_data/' + '导入开票(一般纳税人).xlsx')
        self.assertEqual(BaseUrl + '/app/invoice/output-invoice',self.driver.current_url)

    def test2(self):
        '''导入对账单'''
        dashboardPage = AssistantDashbaordPage(self.driver)
        dashboardPage.goAssistanDashbaordPage(BaseUrl)
        dashboardPage.clickChooseAccountImport()
        importFile = ImportBankBillFile(self.driver)
        importFile.importMapping('F:\\autoTest_workspace\\python_code\\e2e-test\\test_data\\导入招商银行对账单.xlsx')
        self.assertIn(BaseUrl + '/app/reconcile/detail/history',self.driver.current_url)

    def test3(self):
        '''导入员工'''
        dashboardPage = AssistantDashbaordPage(self.driver)
        dashboardPage.goAssistanDashbaordPage(BaseUrl)
        dashboardPage.clickImportStaffButton()
        importFile = ImportStaffFile(self.driver)
        importFile.importStaffFile('F:\\autoTest_workspace\\python_code\\e2e-test\\test_data\\导入员工.xlsx')
        self.assertEqual(BaseUrl+'/app/salary/stuff-list',self.driver.current_url)

if __name__ =='__main__':
    unittest.main()