from selenium import webdriver
import os
import sys
import time
import unittest
from .create_comp_page import CreateCompPage
from util.read_excel import ReadExcel
from util.public_page import PublicPage
from util.enter_comp_page import EnterCompPage
'''
进入帐套
创建于2017-09-29-五
caicai
'''


class CreateCompSpec(unittest.TestCase):
    create_account_book_data_dir = '.test_data/cai/create_account_book_data.xlsx'

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def create_account_book_empty_comp_name(self, account_book_info):
        """创建帐套-帐套名称为空,红框提醒保存失败"""
        page = CreateCompPage(self.driver)
        publicPage = PublicPage(self.driver)
        readExcel = ReadExcel(self.create_account_book_data_dir)
        excel_date = readExcel.get_value_by_row(0,1)
        for account_book_data in excel_date:
            page.create_comp(account_book_data)
            page
        result = publicPage.has_danger_is_show()
        self.assertEqual(result, 1)
        self.assertNotIn('company-list', self.driver.current_url)

    def create_account_book_empty_legal_person(self, account_book_info):
        """创建帐套－法定代表人为空，红框提醒，保存失败"""
        page = CreateCompPage(self.driver)
        publicPage = PublicPage(self.driver)
        readExcel = ReadExcel(self.create_account_book_data_dir)
        excel_date = readExcel.get_value_by_row(0,2)
        for account_book_data in excel_date:
            page.create_comp(account_book_data)
        result = publicPage.has_danger_is_show()
        self.assertEqual(result, 1)
        self.assertNotIn('company-list', self.driver.current_url)

    def create_account_book_empty_legal_person(self, account_book_info):
        """创建帐套－成立日期为空，红框提醒，保存失败"""
        page = CreateCompPage(self.driver)
        publicPage = PublicPage(self.driver)
        readExcel = ReadExcel(self.create_account_book_data_dir)
        excel_date = readExcel.get_value_by_row(0,2)
        for account_book_data in excel_date:
            page.create_comp(account_book_data)
        result = publicPage.has_danger_is_show()
        self.assertEqual(result, 1)
        self.assertNotIn('company-list', self.driver.current_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
