from selenium import webdriver
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../..'))
import unittest
from .partner_set_elem import *
from util.public_page import PublicPage
from ..setting_page import SettingPage


class PartnersetPage(object):

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 点击添加按钮
    def click_add_btn(self):
        try:
            publicPage = PublicPage(self.driver)
            add_btn_loc = self.driver.find_element_by_xpath(add_btn_elem)
            publicPage.click_elem(add_btn_loc)
            input_loc = self.driver.find_element_by_xpath(partner_name_elem)
            if publicPage.is_element_present(input_loc):
                print('[PartnerSetPage]click_add_btn－－点击添加按钮 成功！－－')
            else:
                print('[PartnerSetPage]click_add_btn－－点击添加按钮 失败!－－')
                exit()
        except Exception as e:
            print('[PartnerSetPage]click_add_btn－－点击添加按钮 失败－－失败原因是＝>', str(e))
            exit()

    # 设置股东名称
    def set_partnerset_name(self, partnerset_name):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(partner_name_elem)
            publicPage.set_value(input_loc, partnerset_name)
        except Exception as e:
            print('[PartnerSetPage]set_partnerset_name－－设置股东名称 失败－－失败原因是＝>', str(e))
            exit()

    # 输入实缴金额
    def set_actual_paid(self, amount):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(actual_paid_elem)
            publicPage.set_value(input_loc,amount)
        except Exception as e:
            print('[PartnerSetPage]set_actual_paid－－设置实缴金额 失败－－失败原因是＝>', str(e))
            exit()

    def submit(self, btn_name):
        try:
            if btn_name == 'save':
                btn_elem = save_btn_elem
                btn_name = '保存按钮'
            elif btn_name == 'cancel':
                btn_elem = cancel_btn_elem
                btn_name = '取消按钮'
            else:
                return False
            btn_loc = self.driver.find_element_by_xpath(btn_elem)
            publicPage = PublicPage(self.driver)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print('[PartnerSetPage]submit－－点击' +
                  btn_name + ' 失败－－失败原因是＝>', str(e))
            exit()

    def close_modal(self):
        try:
            publicPage = PublicPage(self.driver)            
            btn_loc = self.driver.find_element_by_xpath(close_modal_btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print('[PartnerSetPage]close_modal－－关闭modal框失败 失败－－失败原因是＝>', str(e))
            exit()
        
    def add_partnerset(self,partnerset_info):
        page_url = self.driver.current_url
        publicPage = PublicPage(self.driver)
        add_btn_loc = self.driver.find_element_by_xpath(add_btn_elem)        
        if publicPage.is_element_present(add_btn_loc):
            random_num = publicPage.random_num(100000)
            if partnerset_info[0] == '':
                name = partnerset_info[0]
            elif partnerset_info[0] == 'hello':
                today = time.strftime('%Y-%m-%d')
                name = partnerset_info[0] + today
            else:
                name = partnerset_info[0] + random_num
            self.set_partnerset_name(name)
            self.set_actual_paid(partnerset_info[1])
            self.submit('save')
        else:
            print('[PartnersetPage]add_partnerset－－去股东页面失败－－当前页面url＝>',page_url)
        