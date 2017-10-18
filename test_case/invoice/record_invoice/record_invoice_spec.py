from selenium import webdriver
import unittest
import time
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from util.read_excel import ReadExcel
from .record_invoice_page import RecordInvoicePage
from util.public_page import PublicPage
from util.danger_page import DangerPage

# 记发票测试
# 创建于2017-10-17-周三
# caicai


class RecordInvoiceSpec(unittest.TestCase):
    '''记发票测试'''
    # 发票测试数据地址
    record_invoice_data_dir = './test_data/cai/record_invoice_data.xlsx'

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

    def test_record_input_invoice(self):
        """记多条收票 测试"""
        page = RecordInvoicePage(self.driver, CompInfo.BASE_URL, 'input')
        readExcel = ReadExcel(self.record_invoice_data_dir)
        excel_data = readExcel.get_value_in_order(0)
        dangerPage = DangerPage(self.driver)
        page.go_to_record_invoice_page()
        try:
            for input_invoice_data in excel_data:
                page.record_invoice(input_invoice_data)
                page.submit('save_and_new')
                print('income_test_data=>', income_test_data)
            time.sleep(3)
        except Exception as e:
            danger_msg = dangerPage.get_alert_danger_msg()
            if danger_msg == '请完善相关信息':
                print(input_invoice_data[8] + '－－－－－－记收票失败－－－－－－')
            else:
                print('[RecordInvoiceSpec]－－记收票失败－－错误原因', str(e))
            self.driver.quit()

    def test_record_output_invoice(self):
        """记多条开票 测试"""
        page = RecordInvoicePage(self.driver, CompInfo.BASE_URL, 'input')
        readExcel = ReadExcel(self.record_invoice_data_dir)
        excel_data = readExcel.get_value_in_order(1)
        dangerPage = DangerPage(self.driver)
        page.go_to_record_invoice_page()        
        try:
            for input_invoice_data in excel_data:
                page.record_invoice(input_invoice_data)
                page.submit('save_and_new')                
                print('income_test_data=>', income_test_data)
            time.sleep(3)
        except Exception as e:
            danger_msg = dangerPage.get_alert_danger_msg()
            if danger_msg == '请完善相关信息':
                print(input_invoice_data[8] + '－－－－－－记开票失败－－－－－－')
            else:
                print('[RecordInvoiceSpec]－－记开票失败－－错误原因', str(e))
            self.driver.quit()
            
