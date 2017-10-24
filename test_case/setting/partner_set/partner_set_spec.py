from selenium import webdriver
import unittest
import os
import sys
import time
from util.public_page import PublicPage
from .partner_set_page import PartnersetPage
from .partner_set_elem import *
from util.read_excel import ReadExcel
from util.danger_page import DangerPage
from util.alert_page import AlertPage
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from ..setting_page import SettingPage
# 往来信息
# 创建于 2017-10-24-二
# caicai


class PartnersetSpec(unittest.TestCase):
    ''' 股东 测试'''

    # 股东 测试数据
    partnerset_test_data_dir = './test_data/cai/partnerset_test_data.xlsx'

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
        """测试 点击添加股东按钮是否有效，点击添加按钮，股东modal框显示"""
        page = PartnersetPage(self.driver)
        publicPage = PublicPage(self.driver) 
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL)

        settingPage.go_to_partnerset_page() 
        if 'partner-set' in self.driver.current_url:
            page.click_add_btn()
            input_loc = self.driver.find_element_by_xpath(partner_name_elem)
            result = publicPage.is_element_present(input_loc)
            self.assertEqual(result, True)
        else:
            print('[PartnersetSpec]test_click_add_btn －－去 股东页面 失败－－')       

    def test_partnerset_empty(self):
        """测试 股东名称为空，保存失败，提示‘请填写名称’"""
        page = PartnersetPage(self.driver)
        dangerPage = DangerPage(self.driver)
        readExcel = ReadExcel(self.partnerset_test_data_dir)
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL) 
        
        settingPage.go_to_partnerset_page() 
        if 'partner-set' in self.driver.current_url:
            partnerset_test_data = readExcel.get_value_by_row(0, 1)
            page.add_partnerset(partnerset_test_data)
            time.sleep(1)
            result = dangerPage.get_text_danger_msg()
            self.assertEqual(result, partnerset_test_data[3])
        else:
            print('[PartnersetSpec]test_partnerset_empty －－去 股东页面 失败－－') 

    def test_actual_paid_empty(self):
        """测试 实缴金额为空，保存成功"""
        page = PartnersetPage(self.driver)
        alertPage = AlertPage(self.driver)
        readExcel = ReadExcel(self.partnerset_test_data_dir)
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL)         

        settingPage.go_to_partnerset_page()         
        if 'partner-set' in self.driver.current_url:
            partnerset_test_data = readExcel.get_value_by_row(0, 2)
            page.add_partnerset(partnerset_test_data)
            time.sleep(1)
            result = alertPage.get_alert_msg()
            self.assertEqual(result, partnerset_test_data[3])
        else:
            print('[PartnersetSpec]test_actual_paid_empty －－去 股东页面 失败－－')

    def test_partset_name_repeat(self):
        """测试 股东名称重复，保存失败，提示‘股东名称不能重复’"""
        page = PartnersetPage(self.driver)
        alertPage = AlertPage(self.driver)
        readExcel = ReadExcel(self.partnerset_test_data_dir)
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL) 
        
        settingPage.go_to_partnerset_page()                 
        if 'partner-set' in self.driver.current_url:
            partnerset_test_data = readExcel.get_value_by_row(0, 3)
            page.add_partnerset(partnerset_test_data)
            time.sleep(1)
            result = alertPage.get_alert_msg()
            self.assertEqual(result, partnerset_test_data[3])
        else:
            print('[PartnersetSpec]test_partset_name_repeat －－去 股东页面 失败－－')


if __name__ == '_main_':
    unittest.main()
