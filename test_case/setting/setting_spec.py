from selenium import webdriver
import os
import sys 
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import unittest
from util.enter_comp_page import EnterCompPage
from .setting_page import SettingPage 
from .setting_elem import *
from comp_info import CompInfo

# 设置页面
# 创建于2017-09-06-三
# caicai
class SettingSpec(unittest.TestCase):
    '''
    设置页面测试用例
    '''
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    # url跳转测试
    def test_go_to_comp_billing_page(self):
        """测试－去帐套信息页面"""
        page = SettingPage(self.driver)
        page.go_to_setting_page(CompInfo.BASE_URL)
        current_url = self.driver.current_url
        self.assertIn(comp_billing_url,current_url)

    def test_go_to_contact_page(self):
        """测试－去往来信息页面"""
        page = SettingPage(self.driver)
        page.go_to_contact_page(CompInfo.BASE_URL)
        current_url = self.driver.current_url
        self.assertIn(contact_url,current_url)

    def test_go_to_mutil_user_page(self):
        """测试－去用户管理页面"""
        page = SettingPage(self.driver)
        page.go_to_mutil_user_page(CompInfo.BASE_URL)
        current_url = self.driver.current_url
        self.assertIn(mutil_user_url,current_url)

    def test_go_to_partnerset_page(self):
        """测试－去股东页面"""
        page = SettingPage(self.driver)
        page.go_to_partnerset_page(CompInfo.BASE_URL)
        current_url = self.driver.current_url
        self.assertIn(partner_set_url,current_url)
     
    def test_go_to_tax_rate_page(self):
        """测试－去股东页面"""
        page = SettingPage(self.driver)
        page.go_to_tax_rate_page(CompInfo.BASE_URL)
        current_url = self.driver.current_url
        self.assertIn(tax_rate_url,current_url)
        

    # tab 切换测试
    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()

