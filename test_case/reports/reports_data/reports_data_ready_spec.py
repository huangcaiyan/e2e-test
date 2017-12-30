from selenium import webdriver
import unittest
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../../'))
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from util.read_excel import ReadExcel
from test_case.invoice.record_invoice.record_invoice_page import RecordInvoicePage
from test_case.transaction.record_transaction.record_transaction_page import RecordTransactionPage
from util.public_page import PublicPage
from util.danger_page import DangerPage
from util.alert_page import AlertPage
from selenium.webdriver.support.ui import WebDriverWait
from test_case.invoice.record_invoice.record_invoice_elem import *

# 记发票测试
# 创建于2017-10-17-周三
# caicai


class ReportDataReadySpec(unittest.TestCase):
    '''记发票测试'''
    # 发票测试数据地址
    # record_invoice_data_dir = './test_data/cai/record_invoice_data.xlsx'
    record_invoice_data_dir = './test_data/cai/往来辅助核算明细表映射验证.xlsx'  # 收票0，开票1,收入2，支出3，互转4

    @classmethod
    def setUpClass(self):
        # def setUp(self):
        # self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    @classmethod
    def tearDownClass(self):
        # def tearDown(self):
        self.driver.quit()
    # 纪录完所有数据，收票列表本月收票总额为263,097.00

    def test_record_input_invoice(self):
        """cai-记多条收票 测试"""
        readExcel = ReadExcel(self.record_invoice_data_dir)
        excel_data = readExcel.get_value_in_order(0)
        dangerPage = DangerPage(self.driver)
        alertPage = AlertPage(self.driver)
        page = RecordInvoicePage(self.driver, CompInfo.BASE_URL, 'input')
        page.go_to_record_invoice_page()
        try:
            for input_invoice_data in excel_data:
                page.record_input_invoice(input_invoice_data)
                page.submit('save_and_new')
                print('input_invoice_data=>', input_invoice_data)
            time.sleep(3)
            alert_msg = alertPage.get_alert_msg()
            if '发票保存成功' in alert_msg:
                self.assertIn('发票保存成功', alert_msg)
            elif alert_msg == '请完善相关信息' or alert_msg == '':
                print('[test_record_output_invoice]－－记收票失败－－aler_msg=', alert_msg)
                self.assertEqual(1, 0)
                exit()
        except Exception as e:
            danger_msg = dangerPage.get_alert_danger_msg()
            if danger_msg == '请完善相关信息':
                print(input_invoice_data[8] + '－－－－－－记收票失败－－－－－－')
            else:
                print('[RecordInvoiceSpec]－－记收票失败－－错误原因', str(e))
            # self.driver.quit()

    # 纪录完所有开票数据，开票列表本月收票总额为146,863.35
    def test_record_output_invoice(self):
        """cai-记多条开票 测试"""
        page = RecordInvoicePage(self.driver, CompInfo.BASE_URL, 'output')
        readExcel = ReadExcel(self.record_invoice_data_dir)
        excel_data = readExcel.get_value_in_order(1)
        dangerPage = DangerPage(self.driver)
        alertPage = AlertPage(self.driver)
        page.go_to_record_invoice_page()
        try:
            for output_invoice_data in excel_data:
                page.record_invoice(output_invoice_data)
                page.submit('save_and_new')
                print('output_invoice_data=>', output_invoice_data)
            time.sleep(3)
            alert_msg = alertPage.get_alert_msg()
            if alert_msg == '保存成功':
                self.assertEqual(alert_msg, '保存成功')
            elif alert_msg == '请完善相关信息' or alert_msg == '':
                print('[test_record_output_invoice]－－记开票失败－－aler_msg=', alert_msg)
                self.assertEqual(1, 0)
        except Exception as e:
            danger_msg = dangerPage.get_alert_danger_msg()
            if danger_msg == '请完善相关信息':
                print(input_invoice_data[8] + '－－－－－－记开票失败－－－－－－')
            else:
                print('[RecordInvoiceSpec]－－记开票失败－－错误原因', str(e))
            self.driver.quit()

    def test_record_income(self):
        """测试记多条收入"""
        readExcel = ReadExcel(self.revenue_and_expenditure_data_dir)
        publicPage = PublicPage(self.driver)
        dangerPage = DangerPage(self.driver)
        alertPage = AlertPage(self.driver)
        page = RecordTransactionPage(
            self.driver, CompInfo.BASE_URL, 'Income')
        page.go_to_record_transaction_page()
        excel_data = readExcel.get_value_in_order(2)
        try:
            for income_test_data in excel_data:
                page.record_income_and_outcome(income_test_data)
                print('income_test_data=>', income_test_data)
            alert_msg = alertPage.get_alert_msg()
            self.assertIn('保存成功', alert_msg)
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
        alertPage = AlertPage(self.driver)
        page = RecordTransactionPage(self.driver, CompInfo.BASE_URL, 'Outcome')
        page.go_to_record_transaction_page()
        excel_data = readExcel.get_value_in_order(3)
        try:
            for outcome_test_data in excel_data:
                page.record_income_and_outcome(outcome_test_data)
                print('outcome_test_data=>', outcome_test_data)
            alert_msg = alertPage.get_alert_msg()
            self.assertIn('保存成功', alert_msg)
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
        alertPage = AlertPage(self.driver)
        page = RecordTransactionPage(
            self.driver, CompInfo.BASE_URL, 'accountTransfers')
        excel_data = readExcel.get_value_in_order(4)
        page.go_to_record_transaction_page()
        try:
            for transfer_test_data in excel_data:
                page.record_transfer(transfer_test_data)
                print('transfer_test_data=>', transfer_test_data)
            alert_msg = alertPage.get_alert_msg()
            self.assertIn('保存成功', alert_msg)
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
