from selenium import webdriver
import unittest
import time

from util.public_page import PublicPage
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from .topbar_page import TopBarPage


# @Time :18/1/22 上午11:20
# @Author :huangcaiyan
# @File : topbar_spec
# @Software : PyCharm


class TopBarSpec(unittest.TestCase):
    @classmethod
    def setUpClass( self ):
        self.driver = webdriver.Chrome()

        publicPage = PublicPage(self.driver)
        publicPage.max_window()
        self.driver.implicitly_wait(30)

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    @classmethod
    def tearDownClass( self ):
        self.driver.quit()

    def test_get_current_period( self ):
        """测试 获取当前会计期间"""
        page = TopBarPage(self.driver)
        current_accounting_period = page.get_current_accounting_period('period')
        self.assertIn('2017-12', current_accounting_period)

    def test_get_current_comp_statue( self ):
        """测试 获取当前帐套状态"""
        page = TopBarPage(self.driver)
        current_accounting_period = page.get_current_accounting_period('statue')
        self.assertIn('进行中', current_accounting_period)
        time.sleep()

    def test_get_operation_item( self ):
        """测试 获取操作按钮下拉可选值"""
        page = TopBarPage(self.driver)
        page.click_operation_btn('过帐')


if __name__ == '__main__':
    unittest.main()
