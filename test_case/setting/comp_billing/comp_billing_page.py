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

    # 设置公司名0
    # comp_name：帐套名称
    def set_comp_name(self, comp_name):
        try:
            publicPage = PublicPage(self.driver)
            comp_name_loc = self.driver.find_element_by_name(comp_name_elem)
            publicPage.set_value(comp_name_loc, comp_name)
            publicPage.double_click_elem(comp_name_loc)
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

    # 法定代表人1
    # legal_person_name：法定代表人名称
    def set_legal_person_name(self, legal_person_name):
        try:
            publicPage = PublicPage(self.driver)
            legal_person_name_loc = self.driver.find_element_by_name(
                legal_person_name_name)
            publicPage.set_value(legal_person_name_loc, legal_person_name)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when set_legal_person_name= %s', str(e))

    # 注册资本 2
    # registered_num：注册资本金额
    def set_registered_capital(self, registered_num):
        try:
            publicPage = PublicPage(self.driver)
            registered_capital_loc = self.driver.find_element_by_name(
                registered_capital_name)
            publicPage.set_value(registered_capital_loc, registered_num)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when set_registered_capital= %s', str(e))

    # 省份3
    # prov_name：省份
    def select_prov(self, prov_name):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(priv_dropdown_elem)
            publicPage.select_dropdown_item(drop_loc, prov_name)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when select_prov= %s', str(e))

    # 市 4
    # city_name ：市
    def select_city(self, city_name):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(city_dropdown_elem)
            publicPage.select_dropdown_item(drop_loc, city_name)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when select_city= %s', str(e))

    # 区5
    def select_distr(self, distr_name):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(dist_dropdown_elem)
            publicPage.select_dropdown_item(drop_loc, distr_name)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when select_distr= %s', str(e))

    # 详细地址6
    def set_address(self, address_name):
        try:
            publicPage = PublicPage(self.driver)
            address_name_loc = self.driver.find_element_by_name(
                addr_input_name)
            publicPage.set_value(address_name_loc, address_name)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when set_address= %s', str(e))

    # 设置地址
    def set_pro_city_distr_address(self, prov_name, city_name, distr_name, address_name):
        self.select_prov(prov_name)
        self.select_city(city_name)
        self.select_distr(distr_name)
        self.set_address(address_name)

    # 成立日期
    def select_begin_date(self, day):
        try:
            publicPage = PublicPage(self.driver)
            publicPage.select_date(begin_date_calen_xpath, day)
            time.sleep(1)
        except Exception as e:
            logging.error('there was an exception %s', str(e))

    # 纳税人识别号7
    def set_tax_num(self, num):
        try:
            publicPage = PublicPage(self.driver)
            tax_num_loc = self.driver.find_element_by_name(tax_number_name)
            publicPage.set_value(tax_num_loc, num)
        except expression as e:
            print(
                '[CompBillingPage] There was an exception when set_tax_num= %s', str(e))

    # 行业8
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
            save_button_loc = self.driver.find_element_by_xpath(save_elem)
            return publicPage.click_elem(save_button_loc)
        except Exception as e:
            print('[CompBillingPage] There was an exception when save= %s', str(e))

    # 取消
    def cancel(self):
        try:
            publicPage = PublicPage(self.driver)
            cancel_button_loc = self.driver.find_element_by_xpath(cancel_elem)
            return publicPage.click_elem(cancel_button_loc)
        except Exception as e:
            print('[CompBillingPage] There was an exception when cancel= %s', str(e))

    # 修改公司信息
    def modify_comp_info(self, comp_info):
        self.click_edit()
        time.sleep(2)
        self.set_comp_name(comp_info[0])
        self.set_legal_person_name(comp_info[1])
        self.set_registered_capital(comp_info[2])
        self.set_pro_city_distr_address(
            comp_info[3], comp_info[4], comp_info[5], comp_info[6])
        self.set_tax_num(comp_info[7])
        self.select_industry(comp_info[8])
        self.save()
