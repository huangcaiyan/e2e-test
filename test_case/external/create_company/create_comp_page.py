from selenium import webdriver
import time
from util.public_page import PublicPage
from .create_comp_elem import *

"""
进入帐套
创建于2017-09-29-五
caicai
"""


class CreateCompPage(object):
    def __init__(self, driver):
        self.driver = driver

    def set_accounting_book_name(self, account_book_name):
        """
        :param account_book_name:帐套名称
        """
        try:
            public_page = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_name(comp_name_elem)
            random_num = public_page.random_num(1000)
            if account_book_name == '':
                book_name = account_book_name
            else:
                book_name == account_book_name + random_num
            public_page.set_value(input_loc, book_name)
        except Exception as e:
            print(
                '[CreateCompPage]set_accounting_book_name－－设置帐套名称失败－－失败原因=>', str(e))

    def set_legal_person_name(self, legal_person_name):
        """
        :param legal_person_name: 法人代表名字
        """
        try:
            public_page = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_name(
                legal_person_name_elem)
            public_page.set_value(input_loc, legal_person_name)
        except Exception as e:
            print(
                '[CreateCompPage]set_legal_person_name－－设置法定代表人失败－－失败原因=>', str(e))

    def set_registered_capital(self, registered_capital):
        """
        :param registered_capital: 注册资本（string）
        :return:
        """
        try:
            public_page = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_name(
                registered_capital_elem)
            public_page.set_value(input_loc, registered_capital)
        except Exception as e:
            print(
                '[CreateCompPage]set_registered_capital－－设置注册资本失败－－失败原因=>', str(e))

    def select_prov(self, prov):
        """
        :param prov: 省份
        """
        try:
            public_page = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(prov_drop_elem)
            public_page.select_dropdown_item(drop_loc, prov)
        except Exception as e:
            print('[CreateCompPage]select_prov－－选择省份失败－－失败原因=>', str(e))

    def select_city(self, city):
        """
        :param city: 市名
        """
        try:
            public_page = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(city_drop_elem)
            public_page.select_dropdown_item(drop_loc, city)
        except Exception as e:
            print('[CreateCompPage]select_city－－选择省份失败－－失败原因=>', str(e))

    def select_dist(self, dist):
        """
        :param dist: 区
        """
        try:
            public_page = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(dist_drop_elem)
            public_page.select_dropdown_item(drop_loc, dist)
        except Exception as e:
            print('[CreateCompPage]select_dist－－选择省份失败－－失败原因=>', str(e))

    def select_address(self, prov, city, dist):
        """
        :param prov: 省份
        :param city: 市
        :param dist: 区
        """
        self.select_prov(prov)
        self.select_city(city)
        self.select_dist(dist)

    def select_setup_date(self, year, month, day):
        """
        :param year: 年份，eg：2017
        :param month: 月份，eg：一月
        :param day: 日期，eg：1
        :return:成立日期
        """
        try:
            public_page = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_id(setup_date_elem)
            public_page.select_date_by_ymd(drop_loc, year, month, day)
        except Exception as e:
            print(
                '[CreateCompPage]select_setup_date－－选择年月日失败－－失败原因=>', str(e))

    def set_tax_num(self, tax_num):
        """
        :param tax_num: 税号（string）
        """
        try:
            public_page = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_name(tax_num_elem)
            random_num = public_page.random_num(1000000)
            if tax_num == '':
                num = tax_num
            else:
                num = tax_num + random_num
            public_page.set_value(input_loc, num)
        except Exception as e:
            print('[CreateCompPage]set_tax_num－－设置税号失败－－失败原因=>', str(e))

    def select_industry(self, industry):
        """
        :param industry:行业性质
        """
        try:
            public_page = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(indust_drop_elem)
            public_page.select_dropdown_item(drop_loc, industry)
        except Exception as e:
            print(
                '[CreateCompPage]select_industry－－选择行业失败－－失败原因=>', str(e))

    def select_property(self, account_property):
        """
        :param account_property: 帐套性质，可选值：一般纳税人、小规模纳税人
        """
        try:
            public_page = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(property_elem)
            public_page.select_dropdown_item(drop_loc, account_property)
        except Exception as e:
            print(
                '[CreateCompPage]select_property－－选择帐套性质失败－－失败原因=>', str(e))

    def select_enable_date(self, begin_date):
        """
        :param begin_date: 其中帐套日期，eg：1、2、3...
        """
        try:
            public_page = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(enable_date_drop_elem)
            public_page.click_elem(drop_loc)
            month_loc = self.driver.find_element_by_css_selector(month_elem)
            month = month_loc.text
            if month == begin_date:
                month_loc.click()
            else:
                return '选择启用帐套日期 失败！'
        except Exception as e:
            print(
                '[CreateCompPage]select_enable_date－－设置启用日期失败－－失败原因=>', str(e))

    def submit(self, btn_name):
        """
        保存／取消
        :param btn_name: 按钮名称，可选值：保存、取消；
        :return:点击按钮；
        """
        try:
            if btn_name == 'save':
                btn_elem = create_btn_elem
                operation_name = '保存'
            elif btn_name == 'cancel':
                btn_elem = cancel_btn_elem
                operation_name = '取消'
            btn_loc = self.driver.find_element_by_xpath(btn_elem)
            public_page = PublicPage(self.driver)
            public_page.click_elem(btn_loc)
        except Exception as e:
            print(
                '[CreateCompPage]submit－－' + operation_name + '失败－－失败原因=>', str(e))

    # 创建帐套
    def create_comp(self, create_comp_info):
        """
        :param create_comp_info: 创建帐套数据
        """
        if create_comp_info[11] == '一般纳税人':
            accounting_book_name = create_comp_info[0] + yb
        elif create_comp_info[11] == '小规模纳税人':
            accounting_book_name = create_comp_info[0] + xgm
        self.set_accounting_book_name(accounting_book_name)
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
