from selenium import webdriver
import unittest
import time
from .user_setting_page import UserSettingPage
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo



class UserSettingSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    def test_go_to_comp_billing_page(self):
        page = UserSettingPage(self.driver)
        page.click_user_name()
        page.go_to_setting_page('帐套信息')
        self.assertIn('/app/setting/company-billing', self.driver.current_url)
