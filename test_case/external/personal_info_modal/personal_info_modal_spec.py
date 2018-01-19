from selenium import webdriver
import unittest
import time

from util.public_page import PublicPage
from test_case.login.login_page import LoginPage
from comp_info import CompInfo
from .personal_info_modal_page import PersonalInfoModalPage


# @Time :18/1/19 上午11:46
# @Author :huangcaiyan
# @File : personal_info_modal_spec
# @Software : PyCharm

class PersonalInfoModalSpec(unittest.TestCase):
    data = [CompInfo.LOGIN_DATA[1], 'qq123456', 'qq12345', 'save']

    @classmethod
    def setUpClass( self ):
        self.driver = webdriver.Chrome()

        publicPage = PublicPage(self.driver)
        publicPage.max_window()
        self.driver.implicitly_wait(30)

        loginPage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginPage.login(CompInfo.LOGIN_DATA)

    @classmethod
    def tearDownClass( self ):
        self.driver.quit()

    def test_verify_modify_password( self ):
        """"""
        page = PersonalInfoModalPage(self.driver)
        page.modify_password(self.data)
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
