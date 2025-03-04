from selenium import webdriver
import time
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../..'))
import unittest
from .contact_elem import *
from util.public_page import PublicPage

"""
往来性质页面
修改：2017-11-09-四
caicai
"""


class ContactPage(object):
    """
    往来信息页面
    """

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    def click_add_btn(self):
        """
        :return: 点击保存按钮
        """
        try:
            publicPage = PublicPage(self.driver)
            click_loc = self.driver.find_element_by_id(add_btn_elem)
            publicPage.click_elem(click_loc)
        except Exception as e:
            print('[ContactPage]click_add_btn－－点击添加按钮失败－－失败原因是=>', str(e))

    def set_name(self, contact_name):
        """
        :param contact_name: 往来名称
        """
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_id(name_elem)
            publicPage.set_value(input_loc, contact_name)
        except Exception as e:
            print('[ContactPage]set_name－－设置往来名称失败－－失败原因是=>', str(e))

    def select_contact_property(self, contact_property):
        """
        :param contact_property:往来性质，可选值（ 单位、个人）
        """
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(contact_property_elem)
            publicPage.select_dropdown_item(drop_loc, contact_property)
        except Exception as e:
            print('[ContactPage]select_contact_property－－设置往来性质失败－－失败原因是=>', str(e))

    def set_contact(self, contact):
        """
        :param contact: 联系人名称
        """
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_id(contact_elem)
            publicPage.set_value(input_loc, contact)
        except Exception as e:
            print('[ContactPage]set_contact－－设置联系人失败－－失败原因是=>', str(e))

    def set_account_name(self, account_name):
        """
        :param account_name: 账户名称
        """
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_id(account_name_elem)
            publicPage.set_value(input_loc, account_name)
        except Exception as e:
            print('[ContactPage]set_account_name－－设置账户名称失败－－失败原因是=>', str(e))

    def set_account_num(self, account_num):
        """
        :param account_num:  帐号
        """
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_id(account_num_elem)
            publicPage.set_value(input_loc, account_num)
        except Exception as e:
            print('[ContactPage]set_account_num－－设置帐号失败－－失败原因是=>', str(e))

    def set_phone_num(self, phone_num):
        """
        :param phone_num: 手机号
        """
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_id(phone_num_elem)
            publicPage.set_value(input_loc, phone_num)
        except Exception as e:
            print('[ContactPage]set_phone_num－－设置手机号失败－－失败原因是=>', str(e))

    def submit(self, btn_name):
        """
        :param btn_name: 按钮名称，可选值（save，cancel）
        :return: 保存，取消
        """
        print('btn_name=>', btn_name)
        if btn_name == 'cancel':
            btn_elem = cancel_btn_elem
            operation_name = '取消'
        else:
            btn_elem = save_btn_elem
            operation_name = '保存'
        try:
            publicPage = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print('[ContactPage]submit－－' +
                  operation_name + '失败－－失败原因是=>', str(e))

    def close_modal(self):
        """
        :return: 关闭添加往来窗口
        """
        try:
            publicPage = PublicPage(self.driver)
            click_loc = self.driver.find_element_by_xpath(close_btn_elem)
            publicPage.click_elem(click_loc)
        except Exception as e:
            print('[ContactPage] There was an exception when close_modal=>', str(e))

    def add_contact(self, contact_info):
        """
        :param contact_info: 添加往来信息数据
        contact_info[0]:名称
        contact_info[1]:性质
        contact_info[2]:联系人
        contact_info[3]:账户名称
        contact_info[4]:账号
        contact_info[5]:手机号
        """
        publicPage = PublicPage(self.driver)
        num = str(publicPage.random_num(1000000))
        self.click_add_btn()
        time.sleep(2)
        publicPage.switch_to_add_contact_modal_dialog()
        if contact_info[0] == '' or contact_info[0] == '其他' or contact_info[0] == '内部代表':
            self.set_name(contact_info[0])
        else:
            self.set_name(contact_info[0] + num)
        self.select_contact_property(contact_info[1])
        if contact_info[1] == '单位':
            self.set_contact(contact_info[2])
        self.set_account_name(contact_info[3])
        self.set_account_num(contact_info[4])
        self.set_phone_num(contact_info[5])
