import sys
import os
import unittest
import time
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from .login_page import LoginPage
from util.jsonToPython_util import JsonToPython
from selenium import webdriver
from test_data.cai.login_data import *
from comp_info import CompInfo
from util.alert_page import AlertPage
from util.danger_page import DangerPage

class LoginSpec(unittest.TestCase):
    def setUp(self):
        self.url = 'https://web-gyz-stage.guanplus.com'
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30) 

    def test_login(self):
        loginPage = LoginPage(self.url, self.driver)
        loginPage.login(['18514509382','qq123456'])       
        self.assertEqual("杨春红",self.driver.find_element_by_xpath('//*[@id="personalInfoDropdownMenu"]/span').text)

    def test_verify_login(self):
        """登录管有帐"""
        loginpage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginpage.login(VERIFY_LOGIN)

        current_url = self.driver.current_url
        self.assertIn('/app/company-list', current_url)
        print('登录成功！')

    def test_unexit_username(self):
        """ 用户不存在 """
        loginpage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginpage.login(UNEXIT_USERNAME)

        alertpage = AlertPage(self.driver)
        alert_msg = alertpage.get_alert_msg()
        self.assertEqual(alert_msg, '此用户不存在')

    def test_wrong_password(self):
        """ 密码不正确 """
        loginpage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginpage.login(WRONG_PASSWORD)

        alertpage = AlertPage(self.driver)
        alert_msg = alertpage.get_alert_msg()
        self.assertEqual(alert_msg, '密码不正确')

    def test_empty_username(self):
        """ 用户名为空 """
        loginpage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginpage.login(EMPTY_USERNAME)

        dangerpage = DangerPage(self.driver)
        danger_msg = dangerpage.get_text_danger_msg()
        self.assertEqual(danger_msg, '请填写手机')

    def test_empty_password(self):
        """ 密码为空 """
        loginpage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginpage.login(EMPTY_PASSWORD)

        dangerpage = DangerPage(self.driver)
        danger_msg = dangerpage.get_text_danger_msg()
        self.assertEqual(danger_msg, '请填写密码')

    def test_typeerror_username(self):
        """ 手机格式不正确 """
        loginpage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginpage.login(TYPEERROR_USERNAME)

        dangerpage = DangerPage(self.driver)
        danger_msg = dangerpage.get_text_danger_msg()
        self.assertEqual(danger_msg, '手机格式不正确')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
