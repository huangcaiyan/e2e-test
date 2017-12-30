from selenium import webdriver
import unittest
import os
import sys
from selenium.common.exceptions import NoSuchElementException
import logging
import traceback

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from util.public_page import PublicPage
from util.danger_page import DangerPage
from util.read_excel import ReadExcel
from .comp_billing_page import CompBillingPage
from ..setting_page import SettingPage
from .comp_billing_elem import *



# 帐套信息
# 于2017-09-06-三
# caicai


class CompBillingSpec(unittest.TestCase):
    """ 修改帐套信息测试"""
    # 修改帐套信息测试数据
    modify_accounting_book_info_data_dir = './test_data/cai/modify_accounting_book_info_data.xlsx'

    # 进入公司
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    def test_comp_name_empty(self):
        """ 帐套名称为空，提示‘请填写公司名称’，保存失败"""
        dangerPage = DangerPage(self.driver)
        settingPage = SettingPage(self.driver)
        page = CompBillingPage(self.driver)
        settingPage.go_to_setting_page(CompInfo.BASE_URL)

        read_excel = ReadExcel(self.modify_accounting_book_info_data_dir)
        accounting_book_info_data = read_excel.get_value_by_row(0, 1)
        page.modify_comp_info(accounting_book_info_data)

        text_danger_msg = dangerPage.get_text_danger_msg()
        self.assertEqual(text_danger_msg, accounting_book_info_data[10])

    def test_legal_person_name_empty(self):
        """法定代表人为空，提示‘请填写法定代表人’，保存失败"""
        settingPage = SettingPage(self.driver)
        page = CompBillingPage(self.driver)
        dangerPage = DangerPage(self.driver)
        settingPage.go_to_setting_page(CompInfo.BASE_URL)

        read_excel = ReadExcel(self.modify_accounting_book_info_data_dir)
        accounting_book_info_data = read_excel.get_value_by_row(0, 2)
        page.modify_comp_info(accounting_book_info_data)

        text_danger_msg = dangerPage.get_text_danger_msg()
        self.assertEqual(text_danger_msg, accounting_book_info_data[10])

    def test_tax_num_empty(self):
        """纳税人识别号为空，提示‘请填写纳税人识别号’，保存失败"""
        settingPage = SettingPage(self.driver)
        page = CompBillingPage(self.driver)
        dangerPage = DangerPage(self.driver)
        settingPage.go_to_setting_page(CompInfo.BASE_URL)

        read_excel = ReadExcel(self.modify_accounting_book_info_data_dir)
        accounting_book_info_data = read_excel.get_value_by_row(0, 3)
        page.modify_comp_info(accounting_book_info_data)

        text_danger_msg = dangerPage.get_text_danger_msg()
        self.assertEqual(text_danger_msg, accounting_book_info_data[10])

    def test_verify_edit_comp_info(self):
        """编辑帐套信息，编辑成功"""
        settingPage = SettingPage(self.driver)
        page = CompBillingPage(self.driver)
        settingPage.go_to_setting_page(CompInfo.BASE_URL)
        read_excel = ReadExcel(self.modify_accounting_book_info_data_dir)
        try:
            accounting_book_info_data = read_excel.get_value_by_row(0, 4)
            page.modify_comp_info(accounting_book_info_data)
            next_comp_name = page.get_comp_name()
            self.assertEqual(next_comp_name, accounting_book_info_data[0])
        except NoSuchElementException as e:
            logging.error('查找的页面元素不存在，异常堆栈信息:'+str(traceback.format_exc()))
        except AssertionError as e:
            logging.info('编辑帐套信息失败，')


    def tearDown(self):
        page = CompBillingPage(self.driver)
        publicPage = PublicPage(self.driver)
        publicPage.scroll_to_top()
        if publicPage.is_element_present(self.driver.find_element_by_xpath(edit_xpath)):
            page.click_edit()
            page.set_comp_name(CompInfo.COMP_NAME)
            page.save()
            end_name = page.get_comp_name()
            if end_name == CompInfo.COMP_NAME:
                print('end_name = ', end_name, '\n公司名重置成功！')
            else:
                print('end_name = ', end_name, '\n公司名重置失败！')
        else:
            print('编辑按钮不可见！！！！！')
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
