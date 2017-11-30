from selenium import webdriver
import unittest
import os
import sys
import time
from util.public_page import PublicPage
from .contact_page import ContactPage
from .contact_elem import *
from util.read_excel import ReadExcel
from util.danger_page import DangerPage
from util.alert_page import AlertPage
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from ..setting_page import SettingPage
# 往来信息
# 创建于 2017-09-28-四
# caicai


class ContactSpec(unittest.TestCase):
    ''' 添加往来测试'''

    # 添加往来测试数据
    add_contact_data_dir = './test_data/cai/contact_test_data.xlsx'

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_show_add_modal(self):
        """1.往来信息－测试点击添加按钮显示添加modal框"""
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL)
        page = ContactPage(self.driver)
        publicPage = PublicPage(self.driver)
        settingPage.go_to_contact_page()

        page.click_add_btn()
        time.sleep(2)
        if publicPage.wait_until_loader_disapeared() == False:
            elem_loc = self.driver.find_element_by_xpath(contact_property_elem)
            result = elem_loc.is_displayed()
            print('result=>', result)            
            self.assertEqual(result, 1)
        else:
            print('往来信息－测试点击添加按钮显示添加modal框---失败！')
            self.assertEqual(1,0)

    def test_name_empty(self):
        """2.往来信息－测试往来名称为空，保存失败"""
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL)
        page = ContactPage(self.driver)
        publicPage = PublicPage(self.driver)
        readExcel = ReadExcel(self.add_contact_data_dir)
        dangerPage = DangerPage(self.driver)

        settingPage.go_to_contact_page()
        add_contact_data = readExcel.get_value_by_row(0, 1)
        page.add_contact(add_contact_data)
        page.submit('save')

        result = dangerPage.get_text_danger_msg()
        self.assertEqual(result, add_contact_data[7])
        print('result=>', result)

    def test_phone_num_typeError(self):
        """3.往来信息－手机号格式不正确，提示‘手机格式不正确’，保存失败"""
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL)
        page = ContactPage(self.driver)
        publicPage = PublicPage(self.driver)
        dangerPage = DangerPage(self.driver)
        readExcel = ReadExcel(self.add_contact_data_dir)

        settingPage.go_to_contact_page()
        add_contact_data = readExcel.get_value_by_row(0, 2)
        page.add_contact(add_contact_data)
        page.submit('save')

        result = dangerPage.get_text_danger_msg()
        self.assertEqual(result, add_contact_data[7])
        print('result=>', result)

    def test_contact_input_show(self):
        """4.往来信息－测试性质为单位时－联系人输入框 显示"""
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL)
        page = ContactPage(self.driver)
        publicPage = PublicPage(self.driver)
        readExcel = ReadExcel(self.add_contact_data_dir)

        settingPage.go_to_contact_page()
        add_contact_data = readExcel.get_value_by_row(0, 3)
        page.add_contact(add_contact_data)
        page.submit('save')

        contact_loc = self.driver.find_element_by_id(contact_elem)
        result = publicPage.is_element_present(contact_loc)
        self.assertEqual(result, 1)
        print('result=>', result)

    def test_contact_property_is_unit(self):
        """5.往来信息－测试 添加一个性质为单位的往来，添加成功"""
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL)
        page = ContactPage(self.driver)
        alertPage = AlertPage(self.driver)
        publicPage = PublicPage(self.driver)
        readExcel = ReadExcel(self.add_contact_data_dir)

        settingPage.go_to_contact_page()
        add_contact_data = readExcel.get_value_by_row(0, 4)
        page.add_contact(add_contact_data)
        page.submit('save')

        result = alertPage.get_alert_msg()
        self.assertEqual(result, add_contact_data[7])
        print('result=>', result)

    def test_contact_property_is_personal(self):
        """6.往来信息－测试 添加一个性质为个人的往来，添加成功"""
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL)
        page = ContactPage(self.driver)
        alertPage = AlertPage(self.driver)
        publicPage = PublicPage(self.driver)
        readExcel = ReadExcel(self.add_contact_data_dir)

        settingPage.go_to_contact_page()
        add_contact_data = readExcel.get_value_by_row(0, 5)
        page.add_contact(add_contact_data)
        page.submit('save')

        result = alertPage.get_alert_msg()
        self.assertEqual(result, add_contact_data[7])
        print('result=>', result)

    def test_edit_contact(self):
        """7.往来信息－测试 编辑往来，编辑成功"""
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL)
        page = ContactPage(self.driver)
        alertPage = AlertPage(self.driver)
        publicPage = PublicPage(self.driver)
        readExcel = ReadExcel(self.add_contact_data_dir)

        settingPage.go_to_contact_page()
        add_contact_data = readExcel.get_value_by_row(0, 6)
        page.add_contact(add_contact_data)
        page.submit('save')

        result = alertPage.get_alert_msg()
        self.assertEqual(result, add_contact_data[7])
        print('result=>', result)

    def test_name_repeat(self):
        """8.往来信息－测试往来名称重复，保存失败"""
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL)
        page = ContactPage(self.driver)
        publicPage = PublicPage(self.driver)
        readExcel = ReadExcel(self.add_contact_data_dir)
        alertPage = AlertPage(self.driver)

        settingPage.go_to_contact_page()
        add_contact_data = readExcel.get_value_by_row(0, 7)
        page.add_contact(add_contact_data)
        page.submit('save')

        result = alertPage.get_alert_msg()
        self.assertEqual(result, add_contact_data[7])
        print('result=>', result)


if __name__ == '_main_':
    unittest.main()
