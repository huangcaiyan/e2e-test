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
from util.danger_page import DangerPage
# 添加员工
# 创建于2017-10-11-三
# caicai

class AddStuffSpec(unittest.TestCase):
    '''添加员工测试'''

    file_dir = './test_data/cai/add_stuff_data.xlsx'

    @classmethod
    def setUpClass(self):
        # 登录->进入账套
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1280, 800)

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # 添加雇员 校验
    def test_verify_add_stuff(self):
        """添加员工－添加一位员工－添加成功"""
        page = AddStuffPage(self.driver)
        readExcel = ReadExcel(self.file_dir)
        excel_data = readExcel.get_value_by_row(0, 5)
        page.add_stuff_base(excel_data)
        time.sleep(5)
        page_url = self.driver.current_url
        print('page_url=>', page_url)
        self.assertIn('stuff-list', page_url)

    # 添加非雇员 校验
    def test_verify_add_labour(self):
        """添加员工－添加一位非雇员－添加成功"""
        page = AddStuffPage(self.driver)
        readExcel = ReadExcel(self.file_dir)
        excel_data = readExcel.get_value_by_row(0, 6)
        page.add_stuff_base(excel_data)
        time.sleep(5)
        page_url = self.driver.current_url
        print('page_url=>', page_url)
        self.assertIn('stuff-list', page_url)

    # 必填项为空 校验
    def test_name_empty(self):
        """添加员工－员工名称为空－红框警示，保存失败"""
        page = AddStuffPage(self.driver)
        readExcel = ReadExcel(self.file_dir)
        excel_data = readExcel.get_value_by_row(0, 1)
        page.add_stuff_base(excel_data)
        result = page.has_danger_is_show()
        self.assertEqual(result, 1)

    # 必填项为空 校验
    def test_country_empty(self):
        """添加员工－国籍为空－红框提示，保存失败"""
        page = AddStuffPage(self.driver)
        readExcel = ReadExcel(self.file_dir)
        excel_data = readExcel.get_value_by_row(0, 2)
        page.add_stuff_base(excel_data)
        result = page.has_danger_is_show()
        self.assertEqual(result, 1)

    # 必填项为空 校验
    def test_id_empty(self):
        """添加员工－身份证号为空－红框提示，保存失败"""
        page = AddStuffPage(self.driver)
        readExcel = ReadExcel(self.file_dir)
        excel_data = readExcel.get_value_by_row(0, 3)
        page.add_stuff_base(excel_data)
        result = page.has_danger_is_show()
        self.assertEqual(result, 1)

    # 必填项为空 校验
    def test_employed_empty(self):
        """添加员工－是否雇员为空－红框提示，保存失败"""
        page = AddStuffPage(self.driver)
        readExcel = ReadExcel(self.file_dir)
        excel_data = readExcel.get_value_by_row(0, 4)
        page.add_stuff_base(excel_data)
        result = page.has_danger_is_show()
        self.assertEqual(result, 1)


if __name__ == '_main_':
    unittest.main()
