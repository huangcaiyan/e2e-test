import time
import logging
from util.public_page import PublicPage
from .comp_billing_elem import *
from selenium.common.exceptions import NoSuchElementException
import traceback
"""
帐套信息
创建于20170801
修改于20171229
caicai
"""


class CompBillingPage:
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    def click_edit(self):
        """
        :return: 点击编辑事件
        """
        try:
            publicPage = PublicPage(self.driver)
            edit_loc = self.driver.find_element_by_xpath(edit_xpath)
            publicPage.click_elem(edit_loc)
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when click_edit= %s', str(e))

    # 设置公司名0
    def set_comp_name(self, comp_name):
        """
        :param comp_name: 帐套名称；
        """
        try:
            publicPage = PublicPage(self.driver)
            comp_name_loc = self.driver.find_element_by_name(comp_name_elem)
            publicPage.set_value(comp_name_loc, comp_name)
        except NoSuchElementException as e:
            logging.error('查找的页面元素不存在，异常堆栈信息：'+str(traceback.format_exc()))
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when set_comp_name- %s', str(e))

    def get_comp_name(self):
        """
        :return: 帐套名称
        """
        try:
            publicPage = PublicPage(self.driver)
            comp_name_loc = self.driver.find_element_by_id(comp_name_text_id)
            print('comp_name')
            return publicPage.get_value(comp_name_loc)
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when get_comp_name= %s', str(e))

    # 法定代表人1
    def set_legal_person_name(self, legal_person_name):
        """
        :param legal_person_name: 法定代表人名称
        """
        try:
            publicPage = PublicPage(self.driver)
            legal_person_name_loc = self.driver.find_element_by_name(
                legal_person_name_name)
            publicPage.set_value(legal_person_name_loc, legal_person_name)
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when set_legal_person_name= %s', str(e))

    # 注册资本 2
    def set_registered_capital(self, registered_num):
        """
        :param registered_num: 注册资本
        """
        try:
            publicPage = PublicPage(self.driver)
            registered_capital_loc = self.driver.find_element_by_name(
                registered_capital_name)
            publicPage.set_value(registered_capital_loc, registered_num)
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when set_registered_capital= %s', str(e))

    # 省份3
    def select_prov(self, prov_name):
        """
        :param prov_name: 省份
        """
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(priv_dropdown_elem)
            publicPage.select_dropdown_item(drop_loc, prov_name)
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when select_prov= %s', str(e))

    # 市 4
    def select_city(self, city_name):
        """
        :param city_name: 市
        """
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(city_dropdown_elem)
            publicPage.select_dropdown_item(drop_loc, city_name)
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when select_city= %s', str(e))

    # 区5
    def select_distr(self, distr_name):
        """
        :param distr_name:区
        """
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(dist_dropdown_elem)
            publicPage.select_dropdown_item(drop_loc, distr_name)
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when select_distr= %s', str(e))

    # 详细地址6
    def set_address(self, address_name):
        """
        :param address_name: 详细地址
        """
        try:
            publicPage = PublicPage(self.driver)
            address_name_loc = self.driver.find_element_by_name(
                addr_input_name)
            publicPage.set_value(address_name_loc, address_name)
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when set_address= %s', str(e))

    # 设置地址
    def set_pro_city_distr_address(self, prov_name, city_name, distr_name, address_name):
        """
        :param prov_name: 省份
        :param city_name: 市
        :param distr_name: 区
        :param address_name: 详细地址
        """
        self.select_prov(prov_name)
        self.select_city(city_name)
        self.select_distr(distr_name)
        self.set_address(address_name)

    # 成立日期
    def select_begin_date(self, day):
        """
        :param day: 日期，eg：1
        """
        try:
            publicPage = PublicPage(self.driver)
            publicPage.select_date(begin_date_calen_xpath, day)
            time.sleep(1)
        except Exception as e:
            logging.error('there was an exception %s', str(e))

    # 纳税人识别号7
    def set_tax_num(self, num):
        """
        :param num: 纳税人识别号
        """
        try:
            publicPage = PublicPage(self.driver)
            tax_num_loc = self.driver.find_element_by_name(tax_number_name)
            publicPage.set_value(tax_num_loc, num)
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when set_tax_num= %s', str(e))

    # 行业8
    def select_industry(self, indus_name):
        """
        :param indus_name: 行业名称
        """
        try:
            publicPage = PublicPage(self.driver)
            indust_loc = self.driver.find_element_by_name(
                industry_dropdown_name)
            publicPage.select_dropdown_item(indust_loc, indus_name)
        except Exception as e:
            print(
                '[CompBillingPage] There was an exception when select_industry= %s', str(e))

    # 服务截止日期
    def select_service_deadline(self, day):
        """
        :param day: 服务截止日期，eg：1
        """
        try:
            publicPage = PublicPage(self.driver)
            publicPage.select_date(service_deadline_xpath, day)
            time.sleep(1)
        except Exception as e:
            print(
                '[CompBillingPage]select_service_deadline设置服务截止日期失败，错误原因是＝>', str(e))

    def submit(self, btn_name):
        """
        :param btn_name: 按钮名称，可选值（save，cancel）
        :return:保存或取消
        """
        if btn_name == 'save':
            btn_elem = save_elem
            btn = '保存'
        elif btn_name == 'cancel':
            btn_elem = cancel_elem
            btn = '取消'
        else:
            btn_elem = None
            print('按钮定位失败')
            exit()
        try:
            public_page = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(btn_elem)
            return public_page.click_elem(btn_loc)
        except Exception as e:
            print('[CompBillingPage]submit' + btn + '失败！错误原因是＝>', str(e))
            exit()



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
