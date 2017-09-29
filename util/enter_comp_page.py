from selenium import webdriver
import time
from test_case.login.login_page import LoginPage
from .public_page import PublicPage

class EnterCompPage:

    # location
    create_comp_xpath = '//*[@id="body"]/company-list/div[1]/div[3]/div[2]/button[1]'

    def __init__(self, driver):
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
        comp_name_loc = self.driver.find_element_by_link_text(
            enter_comp_info[2])
        comp_name_loc.click()
        # publicPage.click_elem(comp_name_loc)
        time.sleep(5)
        page_url = self.driver.current_url
        if 'home-page' in page_url:
            print('进入帐套成功！当前帐套名称为： ', self.get_comp_name(enter_comp_info[2]))
        else:
            print('————————————进入公司失败 ！————————————')

    # 创建帐套
    def create_comp(self, create_comp_info):
        self.set_account_book_name(create_comp_info[0])
        self.set_legal_person_name(create_comp_info[1])
        self.set_registered_capital(create_comp_info[2])
        self.select_address(create_comp_info[3],create_comp_info[4],create_comp_info[5])
        self.select_setup_date(create_comp_info[6],create_comp_info[7],create_comp_info[8])
        self.set_tax_num(create_comp_info[9])
        self.select_industry(create_comp_info[10])
        self.select_property(create_comp_info[11])
        self.select_enable_date(create_comp_info[12])

