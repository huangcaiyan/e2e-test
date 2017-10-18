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
from util.public_page import PublicPage
from util.danger_page import DangerPage
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
        publicPage = PublicPage(self.driver)
        dangerPage = DangerPage(self.driver)
        page = RecordTransactionPage(
            self.driver, CompInfo.BASE_URL, 'Income')
        page.go_to_record_transaction_page()
        excel_data = readExcel.get_value_in_order(0)
        try:
            for income_test_data in excel_data:
                page.record_income_and_outcome(income_test_data)
                print('income_test_data=>', income_test_data)
            time.sleep(3)
        except Exception as e:
            danger_msg = dangerPage.get_alert_danger_msg()
            if danger_msg == '请填写完整！':
                print(income_test_data[6] + '－－－－－－记收入失败－－－－－－')
            else:
                print('[RecordTransactionSpec]－－记收入失败－－错误原因', str(e))
            self.driver.quit()

    def test_record_outcome(self):
        """测试记多条支出"""
        readExcel = ReadExcel(self.revenue_and_expenditure_data_dir)
        dangerPage = DangerPage(self.driver)
        page = RecordTransactionPage(self.driver, CompInfo.BASE_URL, 'Outcome')
        page.go_to_record_transaction_page()
        excel_data = readExcel.get_value_in_order(1)
        try:
            for outcome_test_data in excel_data:
                page.record_income_and_outcome(outcome_test_data)
                print('outcome_test_data=>', outcome_test_data)
            time.sleep(3)
        except Exception as e:
            danger_msg = dangerPage.get_alert_danger_msg()
            if danger_msg == '请填写完整！':
                print('－－记 ' + income_test_data[6] +
                      '失败－－' + '，错误原因＝>', danger_msg)
                self.driver.quit()
            else:
                print('[RecordTransactionSpec]－－记支出失败－－错误原因', str(e))
            self.driver.quit()

    def test_record_transfer(self):
        """测试记多条互转"""
        readExcel = ReadExcel(self.revenue_and_expenditure_data_dir)
        dangerPage = DangerPage(self.driver)
        page = RecordTransactionPage(
            self.driver, CompInfo.BASE_URL, 'accountTransfers')
        page.go_to_record_transaction_page()
        excel_data = readExcel.get_value_in_order(2)
        try:
            for transfer_test_data in excel_data:
                page.record_transfer(transfer_test_data)
                print('transfer_test_data=>', transfer_test_data)
            time.sleep(3)
        except Exception as e:
            danger_msg = dangerPage.get_alert_danger_msg()
            if danger_msg == '金额不能为0' or danger_msg == '账户不能为空' or danger_msg == '账户不能相同':
                print('－－记 ' + income_test_data[5] +
                      '失败－－' + '，错误原因＝>', danger_msg)
                self.driver.quit()
            else:
                print('[RecordTransactionSpec]－－记互转失败－－错误原因', str(e))
            self.driver.quit()


if __name__ == '_main_':
    unittest.main()
