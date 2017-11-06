import time
import sys
import unittest
import os
from selenium import webdriver
# sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../../'))

from test_case.reports.cashFlows_statement.cashFlows_statement_page import CashFlowsPage
from comp_info_1 import CompInfo
from util.read_excel import ReadExcel
from test_case.login.login_page import LoginPage
from util.enter_company_util import EnterCompany
from config import *

# 现金流量表数据校验
# 修改与2017-11-06
# meng


class CashFlowsSpec(unittest.TestCase):

    cashFlows_test_data_dir = './test_data/cai/record_transaction_data.xlsx'

    
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        

        # 进入账套
        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

        # 进入现金流量表页面
        cashFlows_page = CashFlowsPage(self.url, self.driver)        
        cashFlows_page.goToCashFlowsModule(BaseUrl)


    def tearDownClass(self):
        self.driver.quit()

    
    def test_cashFlows_1(self):
        ''' 行次1数值测试'''
        cashFlows_page = CashFlowsPage(self.url, self.driver)
        readExcel = ReadExcel(self.cashFlows_test_data_dir)
        cashFlows_page.get_table_content(".table","第一行第三列")

