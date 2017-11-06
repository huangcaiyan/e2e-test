from selenium import webdriver
import time
import unittest
from invoice_list_page import TransactionListPage
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo


class InvoiceListSpec(unittest.TestCase):

    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1280, 800)

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    def test_get_input_invoice_list_total(self):
        


    def tearDownClass(self):
        self.driver.quit()
