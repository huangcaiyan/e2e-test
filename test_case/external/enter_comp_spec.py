from selenium import webdriver
import unittest
import os
import time
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo

class EnterCompSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()


    def test_enter_comp(self):
        page = EnterCompPage(CompInfo.BASE_URL,self.driver)
        page.enter_comp(CompInfo.ENTER_COMP_INFO_YB)


    def tearDown(self):
        self.driver.quit()

if __name__ == '_main_':
    unittest.main()

        