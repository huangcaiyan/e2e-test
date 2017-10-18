from selenium import webdriver
import unittest
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../../'))
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from .record_transaction_page import RecordTransactionPage
from util.read_excel import ReadExcel

# 记收入、支出、互转测试
# 创建于2017-10-16-周二
# caicai


class RecordTransactionSpec(unittest.TestCase):
    '''记收支'''
    # 收支测试数据地址
    revenue_and_expenditure_data_dir = './test_data/cai/record_transaction_data.xlsx'

    @classmethod
    def setUpClass(self):
        # self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1280, 800)

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_record_income(self):
        """测试记多条收入"""
        readExcel = ReadExcel(self.revenue_and_expenditure_data_dir)
        page = RecordTransactionPage(
            self.driver, CompInfo.BASE_URL, 'Income')
        page.go_to_record_transaction_page()
        excel_data = readExcel.get_value_in_order(0)
        for income_test_data in excel_data:
            page.record_income_and_outcome(income_test_data)
            print('income_test_data=>', income_test_data)
        time.sleep(3)

    def test_record_outcome(self):
        """测试记多条支出"""
        readExcel = ReadExcel(self.revenue_and_expenditure_data_dir)
        page = RecordTransactionPage(self.driver, CompInfo.BASE_URL, 'Outcome')
        page.go_to_record_transaction_page()
        excel_data = readExcel.get_value_in_order(1)
        for outcome_test_data in excel_data:
            page.record_income_and_outcome(outcome_test_data)
            print('outcome_test_data=>', outcome_test_data)
        time.sleep(3)

    def test_record_transfer(self):
        """测试记多条互转"""
        readExcel = ReadExcel(self.revenue_and_expenditure_data_dir)
        page = RecordTransactionPage(self.driver, CompInfo.BASE_URL, 'Outcome')
        page.go_to_record_transaction_page()
        excel_data = readExcel.get_value_in_order(1)
        for transfer_test_data in excel_data:
            page.record_transfer(transfer_test_data)
            print('transfer_test_data=>', transfer_test_data)
        time.sleep(3)
