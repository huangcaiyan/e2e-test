from selenium import webdriver
import unittest
import time
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from .revenue_and_expenditure_page import RevenueAndExpenditurePage
from util.read_excel import ReadExcel

# 记收入、支出、互转测试
# 创建于2017-10-16-周二
# caicai

class RecordRevenueAndExpenditureSpec(unittest.TestCase):
    '''记收支'''
    # 收支测试数据地址
    revenue_and_expenditure_data_dir = './test_data/cai/revenue_and_expenditure_data.xlsx'

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

    def test_record_revenue(self):
        """记收入"""
        readExcel = ReadExcel(self.revenue_and_expenditure_data_dir)
        excel_data = readExcel.get_value_in_order(0)
        page.go_to_record_page()
        for revenue_test_data in excel_data:
            page = RevenueAndExpenditurePage(self.driver, CompInfo.BASE_URL, excel_data[0])
            page.recort_revenue_and_expenditure(excel_data)
        # time.sleep(3)
        # page_url = self.driver.current_url
        # self.assertIn('/transaction/list', page_url)

    def test_record_expenditure(self):
        """记支出"""
        readExcel = ReadExcel(self.revenue_and_expenditure_data_dir)
        excel_data = readExcel.get_value_in_order(1)
        for expenditure_test_data in excel_data:
            page = RevenueAndExpenditurePage(
                self.driver, CompInfo.BASE_URL, expenditure_test_data[0])
            page.go_to_record_page()
            page.recort_revenue_and_expenditure(expenditure_test_data)
        time.sleep(3)
        page_url = self.driver.current_url
        self.assertIn('/transaction/list', page_url)

    def test_record_transfer(self):
        """记互转"""
        readExcel = ReadExcel(self.revenue_and_expenditure_data_dir)
        excel_data = readExcel.get_value_in_order(2)
        for transfer_test_data in excel_data:
            page = RevenueAndExpenditurePage(
                self.driver, CompInfo.BASE_URL, transfer_test_data[0])
            page.record_transfer(transfer_test_data)
        time.sleep(3)
        page_url = self.driver.current_url
        self.assertIn('/transaction/list', page_url)

    

