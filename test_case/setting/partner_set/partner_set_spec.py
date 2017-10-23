from selenium import webdriver
import unittest
import os
import sys
import time
from util.public_page import PublicPage
from partner_set_page import PartnersetPage
from partner_set_elem import *
from util.read_excel import ReadExcel
from util.danger_page import DangerPage
from util.alert_page import AlertPage
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from ..setting_page import SettingPage
# 往来信息
# 创建于 2017-09-28-四
# caicai


class PartnersetSpec(unittest.TestCase):
    ''' 添加往来测试'''

    # 添加往来测试数据
    # partnerset_test_data = './test_data/cai/contact_test_data.xlsx'

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1280, 800)

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_click_add_btn(self):
        """测试 添加股东按钮是否有效，点击添加按钮，股东modal框显示"""
        settingPage = SettingPage(self.driver,CompInfo.BASE_URL)
        page = PartnersetPage(self.driver)
        publicPage = PublicPage(self.driver)
        settingPage.go_to_partnerset_page()
        try:
            page.click_add_btn()
            input_loc = self.driver.find_element_by_xpath(partner_name_elem)
            result = publicPage.is_element_present(input_loc)
            self.assertEqual(result, True)
        except Exception as e:
            print('[PartnersetSpec]－－测试 添加股东按钮是否有效 失败－－')

    def test_partnerset_empty(self):
        page = PartnersetPage(self.driver)
        publicPage = PublicPage(self.driver)
        try:
            page.add_partnerset()



        