from selenium import webdriver
import unittest
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from .add_stuff_page import AddStuffPage
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from test_case.salary.salary_page import SalaryPage
from test_data.cai.add_stuff_data import *
from util.read_excel import ReadExcel


class AddStuffSpec(unittest.TestCase):

    file_dir = './test_data/cai/add_stuff_data.xlsx'

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(CompInfo.BASE_URL, self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO_YB)

    def test_name_empty(self):
        """添加员工－员工名称为空－红框警示，保存失败"""
        page = AddStuffPage(self.driver)
        readExcel = ReadExcel(self.file_dir)
        excel_data = readExcel.get_value_by_row(0, 2)
        for add_stuff_data in excel_data:
            page.add_stuff_base(add_stuff_data)
        result = page.has_danger_is_show()
        self.assertEqual(result, 1)

    def test_country_empty(self):
        """添加员工－国籍为空－红框提示，保存失败"""
        page = AddStuffPage(self.driver)
        readExcel = ReadExcel(self.file_dir)
        excel_data = readExcel.get_value_by_row(0, 2)
        for add_stuff_data in excel_data:
            page.add_stuff_base(add_stuff_data)
        result = page.has_danger_is_show()
        self.assertEqual(result, 1)

    def test_id_empty(self):
        """添加员工－身份证号为空－红框提示，保存失败"""
        page = AddStuffPage(self.driver)
        readExcel = ReadExcel(self.file_dir)
        excel_data = readExcel.get_value_by_row(0, 3)
        for add_stuff_data in excel_data:
            page.add_stuff_base(add_stuff_data)
        result = page.has_danger_is_show()
        self.assertEqual(result, 1)

    def test_employed_empty(self):
        """添加员工－是否雇员为空－红框提示，保存失败"""
        page = AddStuffPage(self.driver)
        readExcel = ReadExcel(self.file_dir)
        excel_data = readExcel.get_value_by_row(0, 4)
        for add_stuff_data in excel_data:
            page.add_stuff_base(add_stuff_data)
        result = page.has_danger_is_show()
        self.assertEqual(result, 1)

    def test_verify_add_stuff(self):
        """添加员工－添加一位员工－添加成功"""
        page = AddStuffPage(self.driver)
        readExcel = ReadExcel(self.file_dir)
        excel_data = readExcel.get_value_by_row(0, 5)
        for add_stuff_data in excel_data:
            page.add_stuff_base(add_stuff_data)
        time.sleep(3)
        page_url = self.driver.current_url
        self.assertIn('stuff-list', page_url)

    def test_verify_add_labour(self):
        """添加员工－添加一位非雇员－添加成功"""
        page = AddStuffPage(self.driver)
        readExcel = ReadExcel(self.file_dir)
        excel_data = readExcel.get_value_by_row(0, 6)
        for add_stuff_data in excel_data:
            page.add_stuff_base(add_stuff_data)
        time.sleep(3)
        page_url = self.driver.current_url
        self.assertIn('stuff-list', page_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
