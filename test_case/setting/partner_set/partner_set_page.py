from selenium import webdriver
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../..'))
import unittest
from .partner_set_elem import *
from util.public_page import PublicPage
from ..setting_page import SettingPage
from comp_info import CompInfo


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
            publicPage.set_value(input_loc, amount)
        except Exception as e:
            print('[PartnerSetPage]set_actual_paid－－设置实缴金额 失败－－失败原因是＝>', str(e))
            exit()

    def submit(self, btn_name):
        try:
            if btn_name == 'save':
                btn_elem = save_btn_elem
                btn_name = '保存按钮'
            else:
                btn_elem = cancel_btn_elem
                btn_name = '取消按钮'
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

    def add_partnerset(self, partnerset_info):
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL)
        publicPage = PublicPage(self.driver)
        settingPage.go_to_partnerset_page()
        if publicPage.wait_until_loader_disapeared() == False:
            if 'partner-set' in self.driver.current_url:
                random_num = publicPage.random_num(100000)
                if partnerset_info[0] == '':
                    name = partnerset_info[0]
                elif partnerset_info[0] == 'hello':
                    today = time.strftime('%Y-%m-%d')
                    name = partnerset_info[0] + today
                else:
                    name = partnerset_info[0] + str(random_num)

                self.click_add_btn()
                time.sleep(1)
                self.set_partnerset_name(name)
                self.set_actual_paid(partnerset_info[1])
        else:
            print('[PartnersetPage]add_partnerset－－去股东页面失败－－当前页面url＝>',
                  self.driver.current_url)

    # 股东列表页面
    # 股东名称
    def click_edit_btn(self, name):
        publicPage = PublicPage(self.driver)
        names_elem = '//*[@id="departmentName"]'
        name_locs = self.driver.find_element_by_xpath(names_elem)
        if name_locs.text == name:
            edit_elem = names_elem + \
                '../following-sibling::td/button[@id="editDepartmentInfo"]'
            print('edit_elem=>', edit_elem)
            edit_loc = self.driver.find_element_by_xpath(edit_elem)
            publicPage.click_elem(elem_loc)
        else:
            print('列表中不存在名为' + name + '的股东')
            exit()

    def eidt_partnerset(self, edit_partnerset_info):
        settingPage = SettingPage(self.driver, CompInfo.BASE_URL)
        publicPage = PublicPage(self.driver)

        settingPage.go_to_partnerset_page()
        if publicPage.wait_until_loader_disapeared() == False:
            if '/app/setting/partner-set' in self.driver.current_url:
                random_num = publicPage.random_num(100000)
                self.click_edit_btn(edit_partnerset_info[0])
                time.sleep(1)
                self.set_partnerset_name(
                    edit_partnerset_info[1] + str(random_num))
            else:
                print('[PartnersetPage]eidt_partnerset－－去股东页面失败－－')
                exit()
        else:
            print('[PartnersetPage]eidt_partnerset－－页面加载超时－－')
            exit()

    # 获取表格行数；
    # def get_row_nums(self, row_xpath):
    #     row_elems = self.driver.find_elements_by_xpath(row_xpath)
    #     print('row_elems=>', row_elems)
    #     row_nums = len(row_elems)
    #     return row_nums

    def get_row_nums(self):
        row_elems = self.driver.find_elements_by_tag_name('tr')
        print('row_elems=>', row_elems)
        row_nums = len(row_elems)
        return row_nums

    # # 获取股东数脚标（以数组的形式存储）
    # def get_row_indexs(self, row_xpath):
    #     row_nums = self.get_row_nums(row_xpath)
    #     print('row_nums=',row_nums)
    #     row_indexs = []
    #     for i in range(row_nums):
    #         row_indexs.append(i)
    #     return row_indexs

    # 获取股东数脚标（以数组的形式存储）
    def get_row_indexs(self):
        row_nums = self.get_row_nums()
        print('row_nums=', row_nums)
        row_indexs = []
        for i in range(row_nums):
            row_indexs.append(i)
        print('row_indexs=', row_indexs)
        return row_indexs

    # 获取表格每行中的表元素集的值；
    # 获取股东名称
    # def get_names(self,row_xpath):
    #     names = []
    #     for i in self.get_row_indexs(row_xpath):
    #         name = self.driver.find_elements_by_xpath(row_xpath)[i].text
    #         names.append(name)
    #     return names

    # 获取表格每行中的表元素集的值；
    # 获取股东名称
    def get_names(self, name_td_index):
        names = []
        for i in self.get_row_indexs():
            if i == 0:
                i = i + 1
            name_loc = self.driver.find_elements_by_tag_name('tr')[i].find_elements_by_tag_name('td')[name_td_index].find_element_by_tag_name('span')
            print('i = >', i)
            name = name_loc.text
            print('name=>', name)
            names.append(name)
        return names

    # 获取表元素对应的行次；
    # def get_item_index(self, row_xpath, item_name):
    #     names = self.get_names(row_xpath)
    #     index = 0
    #     for name in names:
    #         if name == item_name:
    #             index = names.index(name)
    #             print('index=>', index)
    #     return index

    def get_item_index(self, name_td_index, item_name):
        names = self.get_names(name_td_index)
        index = 0
        for name in names:
            if name == item_name:
                index = names.index(name)
                print('index=>', index)
        return index

    def click_operation_btn(self, name_td_index, item_name, btn_td_index, btn_name):
        tr_index = self.get_item_index(name_td_index, item_name)
        if btn_name == 'edit':
            btn_index = 0
        elif btn_name == 'delete':
            btn_index = 1
        btn_loc = self.driver.find_elements_by_tag_name('tr')[tr_index].find_elements_by_tag_name(
            'td')[btn_td_index].find_elements_by_tag_name('button')[btn_index]
        return btn_loc.click()
