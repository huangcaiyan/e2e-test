import sys
import os
import unittest
import time
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from .login_page import LoginPage
from util.jsonToPython_util import JsonToPython
from selenium import webdriver
from util.public_page import PublicPage
from comp_info import CompInfo
from util.alert_page import AlertPage
from util.danger_page import DangerPage
from util.read_excel import ReadExcel
from test_data.cai.login_data import *

# 登录测试
# 修改于2017-09-29-五
# caicai


class LoginSpec(unittest.TestCase):

    login_test_data_dir = './test_data/cai/login_test_data.xlsx'

    def setUp(self):
        # self.url = 'https://web-gyz-stage.guanplus.com'
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)

    def test_login(self):
        loginPage = LoginPage(self.url, self.driver)
        loginPage.login(['18514509382', 'qq123456'])
        self.assertEqual("杨春红", self.driver.find_element_by_xpath(
            '//*[@id="personalInfoDropdownMenu"]/span').text)

    def test_verify_login(self):
        """登录管有帐"""
        loginpage = LoginPage(CompInfo.BASE_URL, self.driver)
        readExcel = ReadExcel(self.login_test_data_dir)
        if 'dev' in CompInfo.BASE_URL:
            sheet_index = 0
        elif 'stage' in CompInfo.BASE_URL:
            sheet_index = 1
        elif 'firms' in CompInfo.BASE_URL:
            sheet_index = 2
        excel_data = readExcel.get_value_by_row(sheet_index, 1)
        for login_test_data in excel_data:
            loginpage.login(login_test_data)

        page_url = self.driver.current_url
        self.assertIn('/app/company-list', page_url)
        print('登录成功！')

    def test_unexit_username(self):
        """ 登录测试－用户不存在 """
        loginpage = LoginPage(CompInfo.BASE_URL, self.driver)
        readExcel = ReadExcel(self.login_test_data_dir)
        if 'dev' in CompInfo.BASE_URL:
            sheet_index = 0
        elif 'stage' in CompInfo.BASE_URL:
            sheet_index = 1
        elif 'firms' in CompInfo.BASE_URL:
            sheet_index = 2
        excel_data = readExcel.get_value_by_row(sheet_index, 2)
        for login_test_data in excel_data:
            loginpage.login(login_test_data)

        publicPage = publicPage(self.driver)
        alert_msg = alertpage.get_alert_msg()
        self.assertEqual(alert_msg, excel_data[3])

    def test_wrong_password(self):
        """ 登录测试－密码不正确 """
        loginpage = LoginPage(CompInfo.BASE_URL, self.driver)
        readExcel = ReadExcel(self.login_test_data_dir)
        if 'dev' in CompInfo.BASE_URL:
            sheet_index = 0
        elif 'stage' in CompInfo.BASE_URL:
            sheet_index = 1
        elif 'firms' in CompInfo.BASE_URL:
            sheet_index = 2
        excel_data = readExcel.get_value_by_row(sheet_index, 3)
        for login_test_data in excel_data:
            loginpage.login(login_test_data)

        alertpage = AlertPage(self.driver)
        alert_msg = alertpage.get_alert_msg()
        self.assertEqual(alert_msg, excel_data[3])

    def test_empty_username(self):
        """ 登录测试－用户名为空 """
        loginpage = LoginPage(CompInfo.BASE_URL, self.driver)
        readExcel = ReadExcel(self.login_test_data_dir)
        if 'dev' in CompInfo.BASE_URL:
            sheet_index = 0
        elif 'stage' in CompInfo.BASE_URL:
            sheet_index = 1
        elif 'firms' in CompInfo.BASE_URL:
            sheet_index = 2
        excel_data = readExcel.get_value_by_row(sheet_index, 4)
        for login_test_data in excel_data:
            loginpage.login(login_test_data)

        dangerpage = DangerPage(self.driver)
        danger_msg = dangerpage.get_text_danger_msg()
        self.assertEqual(danger_msg, excel_data[3])

    def test_empty_password(self):
        """ 登录测试－密码为空 """
        loginpage = LoginPage(CompInfo.BASE_URL, self.driver)
        readExcel = ReadExcel(self.login_test_data_dir)
        if 'dev' in CompInfo.BASE_URL:
            sheet_index = 0
        elif 'stage' in CompInfo.BASE_URL:
            sheet_index = 1
        elif 'firms' in CompInfo.BASE_URL:
            sheet_index = 2
        excel_data = readExcel.get_value_by_row(sheet_index, 5)
        for login_test_data in excel_data:
            loginpage.login(login_test_data)

        dangerpage = DangerPage(self.driver)
        danger_msg = dangerpage.get_text_danger_msg()
        self.assertEqual(danger_msg, excel_data[3])

    def test_typeerror_username(self):
        """ 登录测试－手机格式不正确 """
        loginpage = LoginPage(CompInfo.BASE_URL, self.driver)
        readExcel = ReadExcel(self.login_test_data_dir)
        if 'dev' in CompInfo.BASE_URL:
            sheet_index = 0
        elif 'stage' in CompInfo.BASE_URL:
            sheet_index = 1
        elif 'firms' in CompInfo.BASE_URL:
            sheet_index = 2
        excel_data = readExcel.get_value_by_row(sheet_index, 6)
        for login_test_data in excel_data:
            loginpage.login(login_test_data)

        dangerpage = DangerPage(self.driver)
        danger_msg = dangerpage.get_text_danger_msg()
        self.assertEqual(danger_msg, excel_data[3])

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
