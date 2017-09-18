from selenium import webdriver
import os
import sys
import time
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../..'))
from util.public_page import PublicPage
from .contact_elem import *
from util.danger_page import DangerPage


class ContactPage(object):

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 点击添加按钮
    def click_add_btn(self):
        try:
            btn_loc = self.driver.find_element_by_id(add_btn_elem)
            publicPage = PublicPage(self.driver)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print('[ContactPage] There was an exception when click_add_btn=>', str(e))

    # 设置名称
    # name:往来名称
    def set_name(self, name):
        try:
            input_loc = self.driver.find_element_by_id(name_elem)
            publicPage = PublicPage(self.driver)
            publicPage.set_value(input_loc, name)
        except Exception as e:
            print('[ContactPage] There was an exception when set_name=>', str(e))

    # 选择性质
    # drop_name:单位、个人
    def select_property(self, drop_item):
        try:
            drop_loc = self.driver.find_element_by_name(property_dorp_elem)
            publicPage = PublicPage(self.driver)
            publicPage.select_dropdown_item(drop_loc, drop_item)
        except Exception as e:
            print('[ContactPage] There was an exception when select_property=>', str(e))

    # 设置联系人
    # contact_name:联系人名称
    def set_contact_name(self, contact_name):
        try:
            input_loc = self.driver.find_element_by_id(contact_elem)
            publicPage = PublicPage(self.driver)
            publicPage.set_value(input_loc, contact_name)
        except Exception as e:
            print(
                '[ContactPage] There was an exception when set_contact_name=>', str(e))

    # 设置账户名称
    # account_name：账户名称
    def set_account_name(self, account_name):
        try:
            input_loc = self.driver.find_element_by_id(account_elem)
            publicPage = PublicPage(self.driver)
            publicPage.set_value(input_loc, account_name)
        except Exception as e:
            print(
                '[ContactPage] There was an exception when set_account_name=>', str(e))

    # 设置帐号
    # account_num:账户号
    def set_account_num(self, account_num):
        try:
            input_loc = self.driver.find_element_by_id(account_num_elem)
            publicPage = PublicPage(self.driver)
            publicPage.set_value(input_loc, account_num)
        except Exception as e:
            print('[ContactPage] There was an exception when set_account_num=>', str(e))

    # 设置手机号
    #
    def set_phone_num(self, phone_num):
        try:
            input_loc = self.driver.find_element_by_id(phone_num_elem)
            publicPage = PublicPage(self.driver)
            publicPage.set_value(input_loc, phone_num)
        except Exception as e:
            print('[ContactPage] There was an exception when set_phone_num=>', str(e))

    # 保存按钮
    def save(self):
        try:
            btn_loc = self.driver.find_element_by_xpath(save_elem)
            publicPage = PublicPage(self.driver)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print('[ContactPage] There was an exception when save=>', str(e))

    # 取消
    def cancel(self):
        try:
            btn_loc = self.driver.find_element_by_xpath(cancel_elem)
            publicPage = PublicPage(self.driver)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print('[ContactPage] There was an exception when cancel=>', str(e))

    # 关闭弹窗
    def close_modal(self):
        try:
            btn_loc = self.driver.find_element_by_xpath(close_modal_btn_elem)
            publicPage = PublicPage(self.driver)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print('[ContactPage] There was an exception when close_modal=>', str(e))

    # 空警示文字
    def get_danger_msg(self):
        try:
            dangerPage = DangerPage(self.driver)
            dangerPage.get_text_danger_msg()
        except Exception as e:
            print('[ContactPage] There was an exception when get_danger_msg=>', str(e))

    # 添加往来信息整合
    # contact_info:往来信息内容
    def add_contact(self, contact_info):
        self.set_name(contact_info[0])
        self.select_property(contact_info[1])
        self.set_contact_name(contact_info[2])
        self.set_account_name(contact_info[3])
        self.set_account_num(contact_info[4])
        self.set_phone_num(contact_info[5])
        self.save()
