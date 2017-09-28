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
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
# 往来信息
# 创建于 2017-09-28-四
# caicai


class ContactSpec(unittest.TestCase):

    # 添加往来测试数据
    add_contact_data_dir = './test_data/cai/add_contact_data.xlsx'


    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1280,800)

        enterCompPage = EnterCompPage(CompInfo.BASE_URL,self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO_YB)

    def test_show_add_modal(self):
        """往来信息－测试点击添加按钮显示添加modal框"""
        page = ContactPage(self.driver)
        publicPage = PublicPage(self.driver)
        page.click_add_btn()
        time.sleep(2)
        elem_loc = self.driver.find_element_by_xpath(contact_property_elem)
        result = publicPage.is_element_present(elem_loc)
        self.assertEqual(result,1)

    def test_name_empty(self,contact_info):
        """往来信息－测试往来名称为空，保存失败"""
        page = ContactPage(self.driver)
        publicPage = PublicPage(self.driver)
        dangerPage = DangerPage(self.driver)
        readExcel = ReadExcel(self.add_contact_data_dir)
        excel_data = readExcel.get_value_by_row(0,1)
        for add_contact_data in excel_data:
            page.add_contact(add_contact_data)
        result = dangerPage.get_text_danger_msg()
        self.assertEqual(result,excel_data[7])
        





    def tearDown(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
