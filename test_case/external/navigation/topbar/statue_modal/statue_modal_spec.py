from selenium import webdriver
import unittest
import time

from util.enter_comp_page import EnterCompPage
from util.public_page import PublicPage
from comp_info import CompInfo
from ..topbar_page import TopBarPage
from .statue_modal_page import StatueModalPage


# @Time :18/1/22 下午4:52
# @Author :huangcaiyan
# @File : statue_modal_spec
# @Software : PyCharm


class StatueModalSpec(unittest.TestCase):

    @classmethod
    def setUpClass( self ):
        self.driver = webdriver.Chrome()
        global publicPage
        publicPage = PublicPage(self.driver)
        publicPage.max_window()
        self.driver.implicitly_wait(30)

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    @classmethod
    def tearDownClass( self ):
        self.driver.quit()

    def test_get_posting_modal_body_text( self ):
        topBarPage = TopBarPage(self.driver)
        page = StatueModalPage(self.driver)
        topBarPage.click_operation_btn('过帐')
        time.sleep(2)
        page.get_posting_modal_body_text()


if __name__ == '__main__':
    unittest.main()
