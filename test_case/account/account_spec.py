import time
import os
import sys
import unittest
import xlrd
from selenium import webdriver
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
print(sys.path)

from account.account_page import AccountPage
from util.danger_page import DangerPage
from util.read_excel import ReadExcel
from util.public_page import PublicPage
from util.alert_page import AlertPage
from test_case.login.login_page import LoginPage
from util.enter_company_util import EnterCompany
from config import *
# from test_data.account_data import *


# 账户测试
# 修改于2017-10-10
# meng


class RecordAcountSpec(unittest.TestCase):

    account_test_data_dir = './test_data/account_test_data.xlsx'

    ''' 新增账户测试 '''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # baseUrl = 'https://web-gyz-stage.guanplus.com'
        # self.driver.get(baseUrl)
        ee = EnterCompany(self.driver)
        ee.goToCompany()
        account_page = AccountPage(self.driver)
        account_page.goToAccountModule(BaseUrl) 
        account_page.openAddAcountPage()
        time.sleep(3)

    '''添加银行账户'''
    def test_addaccount_1(self):
        account_page = AccountPage(self.driver) 
        readExcel = ReadExcel(self.account_test_data_dir)
        account_test_data = readExcel.get_value_by_row(0, 1)
        account_page.test_add_bank_account(account_test_data)
    
    '''添加银行账户测试 - 同名账户'''
    def test_same_name(self):
        account_page = AccountPage(self.driver)
        alert_page = AlertPage(self.driver)
        readExcel = ReadExcel(self.account_test_data_dir)
        account_test_data = readExcel.get_value_by_row(0,2)
        account_page.test_add_bank_account(account_test_data)

        # self.driver.switch_to_alert()
        alert_danger_msg = alert_page.get_alert_msg()
        self.assertEqual(alert_danger_msg, account_test_data[6])


    '''添加银行账户测试 - 空名称'''
    def test_empty_name(self):
        account_page = AccountPage(self.driver)
        danger_page = DangerPage(self.driver)
        readExcel = ReadExcel(self.account_test_data_dir)
        account_test_data = readExcel.get_value_by_row(0,3)
        account_page.test_add_bank_account(account_test_data)

        # self.driver.switch_to_alert()
        text_danger_msg = danger_page.get_text_danger_msg()
        self.assertEqual(text_danger_msg, account_test_data[6])





    '''添加微信账户'''
    def test_addaccount_2(self):
        account_page = AccountPage(self.driver)
        readExcel = ReadExcel(self.account_test_data_dir)
        account_test_data_1 = readExcel.get_value_by_row(1, 1)
        account_page.test_add_WeChat_account(account_test_data_1)

    '''添加支付宝账户'''
    def test_addaccount_3(self):
        account_page = AccountPage(self.driver)
        readExcel = ReadExcel(self.account_test_data_dir)
        account_test_data_2 = readExcel.get_value_by_row(2, 1)
        account_page.test_add_Alipay_account(account_test_data_2)

    '''编辑银行账户'''
    


    def tearDown(self):
        self.driver.implicitly_wait(6)



if __name__ == '__main__':
    unittest.main()
    
        