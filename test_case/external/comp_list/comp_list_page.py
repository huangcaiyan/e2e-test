from selenium import webdriver
import unittest, time

from util.public_page import PublicPage
from .comp_list_elem import *
from comp_info import CompInfo
from test_case.login.login_page import LoginPage


class CompListPage(object):
    def __init__( self, driver ):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def go_create_ways_page( self ):
        """
        页面跳转至创建帐套方式页面
        """
        publicPage = PublicPage(self.driver)
        self.driver.get(CompInfo.BASE_URL + '/create-ways')
        if not publicPage.wait_until_loader_disapeared():
            if '/create-ways' in self.driver.current_url:
                print('创建帐套方式页面now')
            else:
                print('－－去创建帐套方式页面 失败！')
                exit()
        else:
            print('－－加载效果未消失，请求超时！')

    def go_to_create_comp_page( self ):
        """
        页面跳转至创建帐套页面
        """
        publicPage = PublicPage(self.driver)
        self.driver.get(CompInfo.BASE_URL + '/create-company')
        if not publicPage.wait_until_loader_disapeared():
            if '/create-company' in self.driver.current_url:
                print('创建帐套页面now')
            else:
                print('－－去创建帐套页面失败！')
                exit()
        else:
            print('－－加载效果未消失，请求超时！')
            exit()

    # 点击创建帐套按钮
    def click_create_comp_btn( self ):
        try:
            public_page = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(create_comp_btn_elem)
            public_page.click_elem(btn_loc)
        except Exception as e:
            print('[CompListPage]点击创建帐套按钮失败=>', str(e))

    def get_accounting_book_property( self, accounting_book_name ):
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

    def enter_comp( self, comp_name ):
        """
        :param comp_name: 帐套名称
        :return: 点击帐套名称进入帐套
        """
        try:
            public_page = PublicPage(self.driver)
            comp_loc = self.driver.find_element_by_link_text(comp_name)
            public_page.click_elem(comp_loc)
        except Exception as e:
            print('[CompListPage]enter_comp：进入帐套失败，失败原因=>', str(e))


class Test(unittest.TestCase):
    def setUp( self ):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def tearDown( self ):
        self.driver.quit()

    def test_click_create_comp_btn( self ):
        loginPage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginPage.login(CompInfo.LOGIN_DATA)
        page = CompListPage(self.driver)
        page.click_create_comp_btn()

    def test_go_to_create_ways_page( self ):
        publicPage = PublicPage(self.driver)
        loginPage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginPage.login(CompInfo.LOGIN_DATA)
        page = CompListPage(self.driver)
        if not publicPage.wait_until_loader_disapeared():
            page.go_create_ways_page()
        time.sleep(2)
        self.assertIn('create-ways', self.driver.current_url)

    def test_go_to_create_company_page( self ):
        publicPage = PublicPage(self.driver)
        loginPage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginPage.login(CompInfo.LOGIN_DATA)
        page = CompListPage(self.driver)
        if not publicPage.wait_until_loader_disapeared():
            page.go_to_create_comp_page()
        time.sleep(2)
        self.assertIn('create-company', self.driver.current_url)


if __name__ == '__main__':
    unittest.main()
