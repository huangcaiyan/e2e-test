from selenium import webdriver
import time
from test_case.login.login_page import LoginPage
from .public_page import PublicPage
from .enter_comp_elem import *


class EnterCompPage:

    # location
    create_comp_xpath = '//*[@id="body"]/company-list/div[1]/div[3]/div[2]/button[1]'

    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    # 帐套名称
    def set_account_book_name(self, account_book_name):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_name(comp_name_elem)
            publicPage.set_value(input_loc, account_book_name)
        except Exception as e:
            print(
                '[EnterCompPage] There was an exception when set_account_book_name=>', str(e))

    # 法定代表人
    def set_legal_person_name(self, legal_person_name):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_name(
                legal_person_name_elem)
            publicPage.set_value(input_loc, legal_person_name)
        except Exception as e:
            print(
                '[EnterCompPage] There was an exception when set_legal_person_name=>', str(e))

    # 注册资本
    def set_registered_capital(self, registered_capital):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_name(
                registered_capital_elem)
            publicPage.set_value(input_loc, registered_capital)
        except Exception as e:
            print(
                '[EnterCompPage] There was an exception when set_registered_capital=>', str(e))

    # 选择省份
    def select_prov(self, prov):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(prov_drop_elem)
            publicPage.select_dropdown_item(drop_loc, prov)
        except Exception as e:
            print('[EnterCompPage] There was an exception when select_prov=>', str(e))

    # 选择市
    def select_city(self, city):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(city_drop_elem)
            publicPage.select_dropdown_item(drop_loc, city)
        except Exception as e:
            print('[EnterCompPage] There was an exception when select_city=>', str(e))

    # 选择区
    def select_dist(self, dist):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(dist_drop_elem)
            publicPage.select_dropdown_item(drop_loc, dist)
        except Exception as e:
            print('[EnterCompPage] There was an exception when select_dist=>', str(e))

    # 选择成立日期
    # year:年份
    # month：月份
    # day：日期
    def select_setup_date(self, year, month, day):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_id(setup_date_elem)
            publicPage.select_date_by_ymd(drop_loc, year, month, day)
        except Exception as e:
            print(
                '[EnterCompPage] There was an exception when select_setup_date=>', str(e))

    # 税号
    def set_tax_num(self, tax_num):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_name(tax_num_elem)
            publicPage.set_value(input_loc, tax_num)
        except Exception as e:
            print('[EnterCompPage] There was an exception when set_tax_num=>', str(e))

    # 行业
    def select_industry(self, industry):
        try:
            publicPage = PublicPage(self.driver)
            dorp_loc = self.driver.find_element_by_name(indust_drop_elem)
            publicPage.select_dropdown_item(drop_loc, industry)
        except Exception as e:
            print(
                '[EnterCompPage] There was an exception when select_industry=>', str(e))

    # 帐套性质
    # account_property:帐套性质
    def select_property(self, account_property):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(property_elem)
            publicPage.select_dropdown_item(drop_loc, account_property)
        except Exception as e:
            print(
                '[EnterCompPage] There was an exception when select_property=>', str(e))

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
        loginPage = LoginPage(self.url, self.driver)
        publicPage = PublicPage(self.driver)
        loginPage.login(enter_comp_info[0])
        comp_name_loc = self.driver.find_element_by_link_text(
            enter_comp_info[1])
        # comp_name_loc.click()
        publicPage.click_elem(comp_name_loc)
        time.sleep(5)
        page_url = self.driver.current_url
        if 'home-page' in page_url:
            print('进入帐套成功！当前帐套名称为： ', self.get_comp_name(enter_comp_info[1]))
        else:
            print('————————————进入公司失败 ！————————————')

    # 创建帐套
    create_comp(self, create_comp_info)
