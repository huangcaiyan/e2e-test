from selenium import webdriver
import unittest
from  xml
from lxml import etree

from util.public_page import PublicPage
from .comp_list_elem import *
from comp_info import CompInfo
from test_case.login.login_page import LoginPage


class CompListPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome()

    # 点击创建帐套按钮
    def click_create_comp_btn(self):
        try:
            public_page = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(create_comp_btn_elem)
            # public_page.click_elem(btn_loc)
            html = etree.HTML()
        except Exception as e:
            print('[CompListPage]点击创建帐套按钮失败=>', str(e))

    def get_accounting_book_property(self, accounting_book_name):
        table = self.driver.find_element_by_tag_name('table')
        trList = table.find_elements_by_tag_name('tr')
        print('trList=>', trList)
        table_value = []
        for row in trList:
            tdList = row.find_elements_by_tag_name('td')
            cell_value = []
            for col in tdList:
                value = col.text
                cell_value.append(value)
            table_value.append(cell_value)
        print('table_value=>', table_value)

        for name in cell_value:
            if accounting_book_name == name:
                tr_index = cell_value.index()
            print('tr_index=>', tr_index)

        accounting_book_property_elem = '//*[@id="company-table"]/tbody/tr[' + tr_index + ']/td[3]/div/span'
        accounting_book_property_loc = self.driver.find_element_by_xpath(accounting_book_property_elem)
        accounting_book_property = accounting_book_property_loc.text
        print('accounting_book_property=>', accounting_book_property)
        return accounting_book_property

    # 进入帐套
    def enter_comp(self, comp_name):
        try:
            public_page = PublicPage(self.driver)
            comp_loc = self.driver.find_element_by_link_text(comp_name)
            public_page.click_elem(comp_loc)
        except Exception as e:
            print('[CompListPage]enter_comp：进入帐套失败，失败原因=>', str(e))


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    # def test_get_accounting_book_property(self):
    #     page = CompListPage(self.driver)
    #     p = page.get_accounting_book_property(CompInfo.COMP_NAME)
    #     self.assertEqual(p,'小规模纳税人')

    def test_click_create_comp_btn(self):
        loginPage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginPage.login(CompInfo.LOGIN_DATA)
        page = CompListPage(self.driver)
        page.click_create_comp_btn()


if __name__ == '__main__':
    unittest.main()
