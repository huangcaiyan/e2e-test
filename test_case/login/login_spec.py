import sys
import os
import unittest
import time
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from login_page import LoginPage
from util.jsonToPython_util import JsonToPython
from selenium import webdriver


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.url = 'https://web-gyz-stage.guanplus.com'
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(6) 

    def test_login(self):
        loginPage = LoginPage(self.url, self.driver)
        loginPage.login(['18514509382','qq123456'])       
        self.assertEqual("杨春红",self.driver.find_element_by_xpath('//*[@id="personalInfoDropdownMenu"]/span').text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
