from selenium import webdriver
import unittest
import time
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from util.read_excel import ReadExcel
from .record_invoice_page import RecordInvoicePage
from util.public_page import PublicPage
from util.danger_page import DangerPage
from util.alert_page import AlertPage
from selenium.webdriver.support.ui import WebDriverWait
from .record_invoice_elem import *

# 记发票测试
# 创建于2017-10-17-周三
# caicai


class RecordInvoiceSpec(unittest.TestCase):
    '''记发票测试'''
    # 发票测试数据地址
    record_invoice_data_dir = './test_data/cai/record_invoice_data.xlsx'

    @classmethod
    def setUpClass(self):
        # def setUp(self):
        # self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # self.driver.set_window_size(1280, 800)
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
        excel_data = readExcel.get_value_in_order(1)
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
                print('[test_record_output_invoice]－－记收票失败－－aler_msg=',alert_msg)                
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
        excel_data = readExcel.get_value_in_order(2)
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
                print('[test_record_output_invoice]－－记开票失败－－aler_msg=',alert_msg)
                self.assertEqual(1, 0)
        except Exception as e:
            danger_msg = dangerPage.get_alert_danger_msg()
            if danger_msg == '请完善相关信息':
                print(input_invoice_data[8] + '－－－－－－记开票失败－－－－－－')
            else:
                print('[RecordInvoiceSpec]－－记开票失败－－错误原因', str(e))
            self.driver.quit()


if __name__ == '_main_':
    unittest.main()
