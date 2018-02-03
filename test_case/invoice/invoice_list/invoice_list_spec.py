from selenium import webdriver
import unittest
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo


class InvoiceListSpec(unittest.TestCase):

    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)




