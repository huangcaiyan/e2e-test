from selenium import webdriver
import unittest
import time
from .sidebar_page import SidebarPage
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo


class SidebarSpec(unittest.TestCase):

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

    def test_get_current_account_period(self):
        page = SidebarPage(self.driver)
        page.get_account_status()


if __name__ == '_main_':
    unittest.main()
