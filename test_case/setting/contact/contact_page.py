from selenium import webdriver
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../..'))
import unittest
from .contact_elem import *
from util.public_page import PublicPage
from test_case.setting.setting_page import SettingPage


class ContactPage(object):

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    def click_add_btn(self):
        try:
            publicPage = PublicPage(self.driver)
            click_loc = self.driver.find_element_by_id(add_btn_elem)
            publicPage.click_elem(click_loc)
        except Exception as e:
            print(
                '[ContactPage] There was an exception when click_add_btn=>', str(e))

    # 设置往来名称
    # contact_name: 往来名称
    def set_name(self, contact_name):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_id(name_elem)
            publicPage.set_value(input_loc, contact_name)
        except Exception as e:
            print(
                '[ContactPage] There was an exception when seet_contact_name=>', str(e))

    # 往来性质：
    # contact_property:单位、个人
    def select_contact_property(self, contact_property):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(contact_property_elem)
            publicPage.select_dropdown_item(drop_loc, contact_property)
        except Exception as e:
            print(
                '[ContactPage] There was an exception when select_contact_property=>', str(e))

    # 联系人
    # contact_name：联系人名称
    def set_contact(self, contact):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_id(contact_elem)
            publicPage.set_value(input_loc, contact)
        except Exception as e:
            print(
                '[ContactPage] There was an exception when set_contact_name=>', str(e))

    # 账户名称
    # account_name：账户名
    def set_account_name(self, account_name):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_id(account_name_elem)
            publicPage.set_value(input_loc, account_name)
        except Exception as e:
            print(
                '[ContactPage] There was an exception when set_account_name=>', str(e))

    # 帐号
    # account_num：帐号
    def set_account_num(self, account_num):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_id(account_num_elem)
            publicPage.set_value(input_loc, account_num)
        except Exception as e:
            print('[ContactPage] There was an exception when set_account_num=>', str(e))

    # 手机号
    # phone_num:手机号
    def set_phone_num(self, phone_num):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_id(phone_num_elem)
            publicPage.set_value(input_loc, phone_num)
        except Exception as e:
            print('[ContactPage] There was an exception when set_phone_num=>', str(e))

    # 保存
    def save(self):
        try:
            publicPage = PublicPage(self.driver)
            click_loc = self.driver.find_element_by_xpath(save_btn_elem)
            publicPage.click_elem(click_loc)
        except Exception as e:
            print('[ContactPage] There was an exception when save=>', str(e))

    # 取消按钮
    def cancel(self):
        try:
            publicPage = PublicPage(self.driver)
            click_loc = self.driver.find_element_by_xpath(cancel_btn_elem)
            publicPage.click_elem(click_loc)
        except Exception as e:
            print('[ContactPage] There was an exception when cancel=>', str(e))

    # 关闭添加往来信息窗口
    def close_modal(self):
        try:
            publicPage = PublicPage(self.driver)
            click_loc = self.driver.find_element_by_xpath(close_btn_elem)
            publicPage.click_elem(click_loc)
        except Exception as e:
            print('[ContactPage] There was an exception when close_modal=>', str(e))

    # 
    def click_edit_btn(self):
        elem = self.driver.find_elements_by_xpath('//tr[contrains(td,1)]')
        print('elem=>',elem.location)


    # 添加往来
    # contact_info[0]:名称
    # contact_info[1]:性质
    # contact_info[2]:联系人
    # contact_info[3]:账户名称
    # contact_info[4]:账号
    # contact_info[5]:手机号
    def add_contact(self, contact_info):
        publicPage = PublicPage(self.driver)
        num = str(publicPage.random_num(1000000))
        self.click_add_btn()
        time.sleep(2)
        publicPage.switch_to_add_contact_modal_dialog()
        if contact_info[0] == '' or contact_info[0]=='其他' or contact_info[0]=='内部代表':
            self.set_name(contact_info[0])
        else:
            self.set_name(contact_info[0] + num)
        self.select_contact_property(contact_info[1])
        if contact_info[1] == '单位':
            self.set_contact(contact_info[2])
        self.set_account_name(contact_info[3])
        self.set_account_num(contact_info[4])
        self.set_phone_num(contact_info[5])
        self.save()
