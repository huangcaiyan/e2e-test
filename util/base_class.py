import unittest
from selenium import webdriver

from util.public_page import PublicPage
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo


class BaseClass(unittest.TestCase):
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        publicPage = PublicPage(self.driver)
        publicPage.max_window()

        self.driver.implicitly_wait(30)

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    def tearDownClass(self):
        print('测试用例运行结束！')
        self.driver.quit()

