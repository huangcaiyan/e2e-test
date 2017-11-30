import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from .login_page import LoginPage
from selenium import webdriver
from comp_info import CompInfo
from util.danger_page import DangerPage
from util.read_excel import ReadExcel


# 登录测试
# 修改于2017-09-29-五
# caicai


class LoginSpec(unittest.TestCase):
    login_test_data_dir = '/Users/huangcaiyan/work/e2e-test/test_data/cai/login_test_data.xlsx'

    @classmethod
    def setUpClass(self):
        self.url = 'https://web-gyz-stage.guanplus.com'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
    #
    # def test_login(self):
    #     login_page = LoginPage(self.url, self.driver)
    #     login_page.login(['18514509382', 'qq123456'])
    #     self.assertEqual("杨春红", self.driver.find_element_by_xpath(
    #         '//*[@id="personalInfoDropdownMenu"]/span').text)

    def test_verify_login(self):
        """登录管有帐"""
        login_page = LoginPage(CompInfo.BASE_URL, self.driver)
        if 'dev' in CompInfo.BASE_URL:
            sheet_index = 0
        elif 'stage' in CompInfo.BASE_URL:
            sheet_index = 1
        elif 'firms' in CompInfo.BASE_URL:
            sheet_index = 2

        read_excel = ReadExcel(self.login_test_data_dir)
        login_test_data = read_excel.get_value_by_row(sheet_index, 1)
        print('login_test_data=>',login_test_data)
        login_page.login(login_test_data)

        page_url = self.driver.current_url
        print('page_url=>', page_url)
        self.assertIn('/app/company-list', page_url)
        print('登录成功！')

    def test_unexit_username(self):
        """ 登录测试－用户不存在 """
        login_page = LoginPage(CompInfo.BASE_URL, self.driver)
        danger_page = DangerPage(self.driver)
        read_excel = ReadExcel(self.login_test_data_dir)
        if 'dev' in CompInfo.BASE_URL:
            sheet_index = 0
        elif 'stage' in CompInfo.BASE_URL:
            sheet_index = 1
        elif 'firms' in CompInfo.BASE_URL:
            sheet_index = 2
        login_test_data = read_excel.get_value_by_row(sheet_index, 2)
        login_page.login(login_test_data)

        error_msg = danger_page.get_error_msg()
        self.assertEqual(error_msg, login_test_data[3])

    def test_wrong_password(self):
        """ 登录测试－密码不正确 """
        login_page = LoginPage(CompInfo.BASE_URL, self.driver)
        danger_page = DangerPage(self.driver)
        read_excel = ReadExcel(self.login_test_data_dir)
        if 'dev' in CompInfo.BASE_URL:
            sheet_index = 0
        elif 'stage' in CompInfo.BASE_URL:
            sheet_index = 1
        elif 'firms' in CompInfo.BASE_URL:
            sheet_index = 2
        login_test_data = read_excel.get_value_by_row(sheet_index, 3)
        login_page.login(login_test_data)

        error_msg = danger_page.get_error_msg()
        self.assertEqual(error_msg, login_test_data[3])

    def test_empty_username(self):
        """ 登录测试－用户名为空 """
        login_page = LoginPage(CompInfo.BASE_URL, self.driver)
        danger_page = DangerPage(self.driver)
        read_excel = ReadExcel(self.login_test_data_dir)
        if 'dev' in CompInfo.BASE_URL:
            sheet_index = 0
        elif 'stage' in CompInfo.BASE_URL:
            sheet_index = 1
        elif 'firms' in CompInfo.BASE_URL:
            sheet_index = 2
        login_test_data = read_excel.get_value_by_row(sheet_index, 4)
        login_page.login(login_test_data)

        input_alert_msg = danger_page.get_input_alert_msg()
        self.assertEqual(input_alert_msg, login_test_data[3])

    def test_empty_password(self):
        """ 登录测试－密码为空 """
        login_page = LoginPage(CompInfo.BASE_URL, self.driver)
        read_excel = ReadExcel(self.login_test_data_dir)
        if 'dev' in CompInfo.BASE_URL:
            sheet_index = 0
        elif 'stage' in CompInfo.BASE_URL:
            sheet_index = 1
        elif 'firms' in CompInfo.BASE_URL:
            sheet_index = 2
        login_test_data = read_excel.get_value_by_row(sheet_index, 5)
        login_page.login(login_test_data)

        input_alert_msg = login_page.get_input_error('password')
        self.assertEqual(input_alert_msg, login_test_data[3])

    def test_typeerror_username(self):
        """ 登录测试－手机号码格式错误 """
        login_page = LoginPage(CompInfo.BASE_URL, self.driver)
        danger_page = DangerPage(self.driver)
        read_excel = ReadExcel(self.login_test_data_dir)
        if 'dev' in CompInfo.BASE_URL:
            sheet_index = 0
        elif 'stage' in CompInfo.BASE_URL:
            sheet_index = 1
        elif 'firms' in CompInfo.BASE_URL:
            sheet_index = 2
        login_test_data = read_excel.get_value_by_row(sheet_index, 6)
        login_page.login(login_test_data)

        input_alert_msg = danger_page.get_input_alert_msg()
        self.assertEqual(input_alert_msg, login_test_data[3])


if __name__ == "__main__":
    unittest.main()
