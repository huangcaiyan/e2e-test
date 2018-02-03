from selenium import webdriver
import unittest
import time, xlwt, xlrd
from xlutils.copy import copy
from xlwt import Style
from openpyxl import load_workbook

from util.public_page import PublicPage
from .topbar_elem import *


# @Time :18/1/22 上午11:20
# @Author :huangcaiyan
# @File : topbar_page
# @Software : PyCharm


class TopBarPage:

    def __init__( self, driver ):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    # －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    # 进入帐套前
    def get_account_company_name( self ):
        """
        :return:代帐公司名称
        """
        publicPage = PublicPage(self.driver)
        name_loc = self.driver.find_element_by_xpath(account_company_name_elem)
        return publicPage.get_value(name_loc)

    def get_login_user_name( self ):
        """
        :return:登陆用户用户名称
        """
        publicPage = PublicPage(self.driver)
        name_loc = self.driver.find_element_by_xpath(login_user_name_elem)
        return publicPage.get_value(name_loc)

    def click_modify_password_link( self ):
        """
        :return:点击修改密码链接
        """
        publicPage = PublicPage(self.driver)
        name = self.get_login_user_name()
        open_list_loc = self.driver.find_element_by_link_text(name)
        publicPage.click_elem(open_list_loc)
        link_loc = self.driver.find_element_by_link_text('修改密码')
        publicPage.click_elem(link_loc)
        time.sleep(2)

    def click_logout_link( self ):
        """
        :return: 点击退出系统按钮
        """
        publicPage = PublicPage(self.driver)
        link_loc = self.driver.find_element_by_link_text('退出')
        publicPage.click_elem(link_loc)

    @staticmethod
    def write_data( data, file_name ):
        # file_dir = './test_data/cai/external/external_data.xlsx'
        work_book = load_workbook(file_name)
        work_sheet = work_book.get_sheet_by_name('会计分配')
        work_sheet['A2'] = data
        work_book.save(file_name)

    @staticmethod
    def write_excel( row, col, string, style=Style.default_style ):
        """
        :param row:行索引
        :param col:列索引
        :param string:写入的内容
        :param style:样式
        :return:将数据写入指定的excel中
        """
        rb = xlrd.open_workbook('./test_data/cai/external/external_data.xlsx')
        work_book = copy(rb)
        work_sheet = work_book.get_sheet(1)
        work_sheet.write(row, col, string, style)
        work_book.save('./test_data/cai/external/external_data.xlsx')

    # －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
    # 进入帐套页面
    def get_comp_name( self ):
        """
        :return:获取当前帐套名称
        """
        publicPage = PublicPage(self.driver)
        text_loc = self.driver.find_element_by_xpath(comp_name_elem)
        return publicPage.get_value(text_loc)

    def logout_current_company( self ):
        """
        :return:点击退出当前帐套按钮
        """
        publicPage = PublicPage(self.driver)
        btn_loc = self.driver.find_element_by_xpath(comp_name_elem)
        publicPage.click_elem(btn_loc)

    def get_current_accounting_period( self, period_or_statue=None ):
        """
        获取当前会计期间、帐套状态
        :period_or_statue : 想要返回的值，可选值（period:会计期间，statue:帐套状态，空：返回两个值
        :return:会计期间：2018-08 　 进行中(accounting_period:当前跨季期间2018-08，
        　
        """
        publicPage = PublicPage(self.driver)
        text_loc = self.driver.find_element_by_xpath(accounting_period_elem)
        values = publicPage.get_value(text_loc)
        value = values.split(' ')
        accounting_period = value[0].split('：')[1]
        accounting_statue = value[2]
        if period_or_statue == 'period':
            print('accounting_period=', accounting_period)
            return accounting_period
        elif period_or_statue == 'statue':
            print('accounting_statue=', accounting_statue)
            return accounting_statue
        else:
            print('accounting_period=', accounting_period, ',accounting_statue=', accounting_statue)
            return accounting_period, accounting_statue

    def click_operation_btn( self, operation_name ):
        """
        :operation_name:操作名称｛ 驳回审核，提交审核（计提），结转、再次结转、过帐、反过帐｝
        :items:['驳回审核', '提交审核(计提)', '结转', '再次结转', '过账', '反过账']
        :return:点击顶部导航栏的操作按钮（进行提交审核、结转、过帐、反过帐；）
        """
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(operation_drop_elem)
        publicPage.click_elem(drop_loc)
        time.sleep(1)
        items_loc = self.driver.find_element_by_css_selector('.dropdown-menu').find_elements_by_css_selector(
            '.dropdown-item')
        items = []
        for item_loc in items_loc:
            item_text = item_loc.text
            items.append(item_text)
        if operation_name == '驳回审核' and items[0] != '' and items_loc[0].is_enabled():
            print('当前操作是', operation_name)
            return publicPage.click_elem(items_loc[0])
        elif operation_name == '提交审核' and items[1] != '' and items_loc[1].is_enabled():
            print('当前操作是', operation_name)
            return publicPage.click_elem(items_loc[1])
        elif operation_name == '结转' and items[2] != '' and items_loc[2].is_enabled():
            print('当前操作是', operation_name)
            return publicPage.click_elem(items_loc[2])
        elif operation_name == '再次结转' and items[3] != '' and items_loc[3].is_enabled():
            print('当前操作是', operation_name)
            return publicPage.click_elem(items_loc[3])
        elif operation_name == '过帐' and items[4] != '' and items_loc[4].is_enabled():
            print('当前操作是', operation_name)
            return publicPage.click_elem(items_loc[4])
        elif operation_name == '反过帐' and items[5] != '' and items_loc[5].is_enabled():
            print('当前操作是', operation_name)
            return publicPage.click_elem(items_loc[5])
        else:
            print('operation_name输入错误，请重新输入！')
            return None
