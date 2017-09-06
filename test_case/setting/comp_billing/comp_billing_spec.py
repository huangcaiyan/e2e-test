from selenium import webdriver
import unittest
import time
import os
import sys 
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from .util.enter_company_util import EnterCompany
from comp_info import CompInfo
from .util.public_page import PublicPage
from util.alert_page import AlertPage
from test_data.cai.comp_billing_data import CompBillingData

# 帐套信息
# 于2017-09-06-三
# caicai
class CompBillingSpec(unittest.TestCase):

    # 进入公司
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompany = EnterCompany(CompInfo.BASE_URL,self.driver)
        enterCompany.enter_comp(CompInfo.ENTER_COMP_INFO_YB)

    def test_edit_comp_info(self):
        """ 编辑帐套信息测试"""
        publicPage = PublicPage(self.driver)
        alertPage = AlertPage(self.driver)
        page = CompBillingPage(self.driver)
        page.modify_comp_info(CompBillingData.MODIFY_COMP_INFO)
        alertPage.get_alert_msg()
        comp_name = page.get_comp_name()
        self.assertEqual(comp_name, CompBillingData.MODIFY_COMP_INFO[0])