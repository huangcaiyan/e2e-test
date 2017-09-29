from selenium import webdriver
import unittest
import os
import time
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
'''
进入帐套
创建于2017-09-28-四
caicai
'''


class EnterCompSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_enter_comp(self):
        page = EnterCompPage(self.driver)
        page.enter_comp(CompInfo.ENTER_COMP_INFO)

    def tearDown(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
