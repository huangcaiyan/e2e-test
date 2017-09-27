import time
import os
import sys
from selenium import webdriver
from account_page import AccountPage
import unittest
from account_page import AccountPage
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))

from test_case.login.login_page import LoginPage
from util.enter_company_util import EnterCompany
from config import *
from test_data.account_data import *



class RecordAcountSpec(unittest.TestCase):
    ''' 新增账户测试 '''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # baseUrl = 'https://web-gyz-stage.guanplus.com'
        # self.driver.get(baseUrl)
        EnterCompany(self.driver,Environment)
        account_page = AccountPage(self.driver)
        account_page.goToAccountModule(BaseUrl) 
        account_page.openAddAcountPage()
        time.sleep(3)

    '''添加银行账户'''
    def test_addaccount_1(self):
    
        account_page = AccountPage(self.driver) 
        account_page.test_add_bank_account(account_data)
        time.sleep(3)

    '''添加微信账户'''
    def test_addaccount_2(self):
        account_page = AccountPage(self.driver)
        account_page.test_add_WeChat_account(account_data_1)

    '''添加支付宝账户'''
    def test_addaccount_3(self):
        account_page = AccountPage(self.driver)
        account_page.test_add_Alipay_account(account_data_2)

    '''编辑银行账户'''
    


    def tearDown(self):
        self.driver.implicitly_wait(6)



if __name__ == '__main__':
    unittest.main()
    
        