from selenium import webdriver
import time
from .contact_page import ContactPage
import unittest
from util.public_page import PublicPage
from .contact_elem import *
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from test_case.setting.setting_page import SettingPage 


class ContactSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)

        enterCompPage = EnterCompPage(CompInfo.BASE_URL,self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO_YB)
        time.sleep(3)

    def test_click_add_btn(self):
        """往来信息－测试添加按钮是否可用"""
        settingPage = SettingPage(self.driver)
        page = ContactPage(self.driver)
        publicPage = PublicPage(self.driver)
        settingPage.go_to_contact_page(CompInfo.BASE_URL) 
        time.sleep(2)       
        page.click_add_btn()
        time.sleep(2)
        name_loc = self.driver.find_element_by_id(name_elem)
        result = publicPage.is_element_present(name_loc)
        self.assertEqual(result, True)

    def test_add_contact(self):
        """往来信息－测试添加往来信息"""
        settingPage = SettingPage(self.driver)
        page = ContactPage(self.driver)
        publicPage = PublicPage(self.driver)
        settingPage.go_to_contact_page(CompInfo.BASE_URL)
        time.sleep(2)
        page.add_contact()

    def tearDown(self):
        self.driver.quit()

if __name__ == '_main_':
    unittest.main()
