from selenium import webdriver
import time
from test_case.login.login_page import LoginPage
from .public_page import PublicPage
from test_case.login.login_elem import *



class EnterCompPage:

    # location
    comp_name_elem = '//*[@id="CompanyDropdownMenu"]/a'
    create_comp_xpath = '//*[@id="body"]/company-list/div[1]/div[3]/div[2]/button[1]'

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 获取当前帐套名称
    def get_comp_name(self, comp_name):
        publicPage = PublicPage(self.driver)
        current_comp_name_loc = self.driver.find_element_by_link_text(
            comp_name)
        name_text = publicPage.get_value(current_comp_name_loc)
        return name_text

    # 进入公司
    # comp_name 公司名称
    def enter_comp(self, enter_comp_info):
        loginPage = LoginPage(enter_comp_info[0], self.driver)
        publicPage = PublicPage(self.driver)
        loginPage.login(enter_comp_info[1])
        time.sleep(3)
        try:
            comp_name_loc = self.driver.find_element_by_link_text(
                enter_comp_info[2])
            # self.driver.execute_script(
                # 'return arguments[0].scrollIntoView();', comp_name_loc)
            # self.driver.execute_script('window.scrollBy(0,600')
            # comp_name_loc.click()
            # self.driver.execute_script()
            # self.driver.execute_script("window.scrollTo(0, 1600)")
            # publicPage.scroll_to_elem(comp_name_loc)
            # time.sleep(1)
            # publicPage.scroll_to_elem(comp_name_loc)
            # comp_name_loc.click()
            publicPage.click_elem(comp_name_loc)
            time.sleep(5)
            if publicPage.is_element_present(self.driver.find_element_by_xpath(self.comp_name_elem)):
                print('[EnterCompPage]－－－－－－进入帐套成功！－－－－－－')
        except Exception as e:
            print('[EnterCompPage]＝＝＝＝＝＝进入帐套失败！＝＝＝＝＝＝')
            exit()

    # 创建帐套
    def create_comp(self, create_comp_info):
        self.set_account_book_name(create_comp_info[0])
        self.set_legal_person_name(create_comp_info[1])
        self.set_registered_capital(create_comp_info[2])
        self.select_address(
            create_comp_info[3], create_comp_info[4], create_comp_info[5])
        self.select_setup_date(
            create_comp_info[6], create_comp_info[7], create_comp_info[8])
        self.set_tax_num(create_comp_info[9])
        self.select_industry(create_comp_info[10])
        self.select_property(create_comp_info[11])
        self.select_enable_date(create_comp_info[12])
