import unittest,sys,os
from time import sleep
import xlrd
from openpyxl import load_workbook
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from config import *
from .account_dashboard_page import AccountDashbaordPage
from util.enter_company_util import EnterCompany
from util.driver_util import Driver
from test_case.import_file.import_output_invoice_file import ImportOutputInvoiceFile
from test_case.import_file.import_bank_bill_file import ImportBankBillFile
from test_case.import_file.import_staff_file import ImportStaffFile


class AccountDashbaordSPec(unittest.TestCase):
    '''会计首页测试'''

    def setUp(self):
        self.driver = Driver().get_driver()
        enterCompany = EnterCompany(self.driver)
        enterCompany.goToCompany()

    def tearDown(self):
        self.driver.quit()

    def test1(self):
        '''结转'''
        dashboardPage = AccountDashbaordPage(self.driver)
        dashboardPage.clickDropDown(0)
        dashboardPage.clickIKnowButton()
        self.assertIn(BaseUrl + '/app/home-page/accounting',self.driver.current_url)
        

    def test2(self):
        '''过账'''
        dashboardPage = AccountDashbaordPage(self.driver)
        dashboardPage.clickDropDown(2)
        dashboardPage.clickPostButton()
        self.assertIn(BaseUrl + '/app/home-page/assist',self.driver.current_url)

    def test3(self):
        '''导入员工'''
        dashboardPage = AssistantDashbaordPage(self.driver)
        dashboardPage.goAssistanDashbaordPage(BaseUrl)
        dashboardPage.clickImportStaffButton()
        importFile = ImportStaffFile(self.driver)
        importFile.importStaffFile('F:\\autoTest_workspace\\python_code\\e2e-test\\test_data\\导入员工.xlsx')
        self.assertEqual(BaseUrl+'/app/salary/stuff-list',self.driver.current_url)

    def test4(self):
        '''提交审核'''

        dashboardPage = AssistantDashbaordPage(self.driver)
        dashboardPage.goAssistanDashbaordPage(BaseUrl)
        dashboardPage.clickSubmit()
        self.assertEqual(BaseUrl + '/app/home-page/accounting',self.driver.current_url)


if __name__ =='__main__':
    unittest.main()