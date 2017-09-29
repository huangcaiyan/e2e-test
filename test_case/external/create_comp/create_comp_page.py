from selenium import webdriver
import time
from util.public_page import PublicPage
from .create_comp_elem import *
'''
进入帐套
创建于2017-09-29-五
caicai
'''


class CreateCompPage(object):

    def __init__(self, driver):
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

    # 住所
    def select_address(self, prov, city, dist):
        self.select_prov(prov)
        self.select_city(city)
        self.select_dist(dist)

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

    # 启用帐套日期
    def select_enable_date(self, begin_date):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(enable_date_drop_elem)
            publicPage.click_elem(drop_loc)
            month_loc = self.driver.find_element_by_css_selector(month_elem)
            month = month_loc.text
            if month == begin_date:
                month_loc.click()
            else:
                return '选择启用帐套日期 失败！'
        except Exception as e:
            print(
                '[EnterCompPage] There was an exception when select_enable_date=>', str(e))

    # 创建
    def save(self):
        try:
            publicPage = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(create_btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print(
                '[EnterCompPage] There was an exception when save=>', str(e))

    # 取消
    def cancel(self):
        try:
            publicPage = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(create_btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print(
                '[EnterCompPage] There was an exception when cancel=>', str(e))

    # 创建帐套
    def create_comp(self, create_comp_info):
        publicPage = PublicPage(self.driver)
        random_num = publicPage.random_num(10000)
        self.set_account_book_name(create_comp_info[0] + random_num)
        self.set_legal_person_name(create_comp_info[1])
        self.set_registered_capital(create_comp_info[2])
        self.select_address(
            create_comp_info[3], create_comp_info[4], create_comp_info[5])
        self.select_setup_date(
            create_comp_info[6], create_comp_info[7], create_comp_info[8])
        self.set_tax_num(create_comp_info[9] + random_num)
        self.select_industry(create_comp_info[10])
        self.select_property(create_comp_info[11])
        self.select_enable_date(create_comp_info[12])
