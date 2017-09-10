from selenium import webdriver
import time
from util.public_page import PublicPage
from .comp_billing_elem import *

# 帐套信息
# 创建于20170801
# caicai
class CompBillingPage:
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

# 点击编辑
    def click_edit(self):
        try:
            publicPage = PublicPage(self.driver)
            edit_loc = self.driver.find_element_by_xpath(edit_xpath)
            publicPage.click_elem(edit_loc)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when click_edit= %s', str(e))


# 设置公司名
    def set_comp_name(self, comp_name):
        try:
            publicPage = PublicPage(self.driver)
            comp_name_loc = self.driver.find_element_by_name(comp_name_name)
            publicPage.set_value(comp_name_loc, comp_name)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when set_comp_name- %s', str(e))


# 获取公司名
    def get_comp_name(self):
        try:
            publicPage = PublicPage(self.driver)
            comp_name_loc = self.driver.find_element_by_id(comp_name_text_id)
            publicPage.get_value(comp_name_loc)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when get_comp_name= %s', str(e))


# 法定代表人
    def set_legal_person_name(self, legal_person_name):
        try:
            publicPage = PublicPage(self.driver)
            legal_person_name_loc = self.driver.find_element_by_name(
                legal_person_name_name)
            publicPage.set_value(legal_person_name_loc, legal_person_name)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when set_legal_person_name= %s', str(e))


# 注册资本
    def set_registered_capital(self, registered_num):
        try:
            publicPage = PublicPage(self.driver)
            registered_capital_loc = self.driver.find_element_by_name(
                registered_capital_name)
            publicPage.set_value(registered_capital_loc, registered_num)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when set_registered_capital= %s', str(e))


# 省份
    def select_prov(self, prov_name):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(priv_dropdown_name)
            publicPage.select_dropdown_item(drop_loc, prov_name)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when select_prov= %s', str(e))

    def select_city(self, city_name):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(city_dropdown_name)
            publicPage.select_dropdown_item(drop_loc, city_name)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when select_city= %s', str(e))


# 区
    def select_distr(self, distr_name):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(dist_dropdown_name)
            publicPage.select_dropdown_item(drop_loc, distr_name)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when select_distr= %s', str(e))


# 详细地址
    def set_address(self, address_name):
        try:
            publicPage = PublicPage(self.driver)
            address_name_loc = self.driver.find_element_by_name(
                addr_input_name)
            publicPage.set_value(address_name_loc, address_name)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when set_address= %s', str(e))

# 成立日期
    def select_begin_date(self, day):
        try:
            publicPage = PublicPage(self.driver)
            publicPage.select_date(begin_date_calen_xpath, day)
            time.sleep(1)
        except Exception as e:
            logging.error('there was an exception %s', str(e))

# 删除成立日期
    def dele_begin_date(self):
        try:
            publicPage = PublicPage(self.driver)
            date_loc = self.driver.find_element_by_xpath(begin_date_dele_xpath)
            publicPage.click_elem(date_loc)
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when dele_begin_date= %s', str(e))

# 纳税人识别号
    def set_tax_num(self, num):
        try:
            publicPage = PublicPage(self.driver)
            tax_num_loc = self.driver.find_element_by_name(tax_number_name)
            publicPage.set_value(tax_num_loc, num)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when set_tax_num= %s', str(e))


# 行业
    def select_industry(self, indus_name):
        try:
            publicPage = PublicPage(self.driver)
            indust_loc = self.driver.find_element_by_name(
                industry_dropdown_name)
            publicPage.select_dropdown_item(indust_loc, indus_name)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when select_industry= %s', str(e))

# 服务截止日期
    def select_service_deadline(self, day):
        try:
            publicPage = PublicPage(self.driver)
            publicPage.select_date(service_deadline_xpath, day)
            time.sleep(1)
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when select_service_deadline= %s', str(e))


# 保存
    def save(self):
        try:
            publicPage = PublicPage(self.driver)
            save_button = self.driver.find_element_by_css_selector(
                self.save_css)
            publicPage.clic
        except Exception as e:
            print('[CompBillingPage] There was an exception when save= %s', str(e))


# 取消
    def cancel(self):
        try:
            publicPage = PublicPage(self.driver)
            cancel_button = self.driver.find_element_by_css_selector(
                self.cancel_css)
            publicPage.scroll_to_elem(cancel_button)
            return cancel_button.click()
        except Exception as e:
            print('[CompBillingPage] There was an exception when cancel= %s', str(e))


# 修改公司信息
    def modify_comp_info(self, comp_info):
        self.click_edit()
        time.sleep(2)
        self.set_comp_name(comp_info[0])
        self.set_legal_person_name(comp_info[1])
        self.set_registered_capital(comp_info[2])
        self.select_prov(comp_info[3])
        self.select_city(comp_info[4])
        self.select_distr(comp_info[5])
        self.set_address(comp_info[6])
        self.select_begin_date(comp_info[7])
        self.set_tax_num(comp_info[8])
        self.select_industry(comp_info[9])
        self.select_service_deadline(comp_info[10])
        self.save()
        time.sleep(2)
