from selenium import webdriver
import unittest
import time

from util.public_page import PublicPage
from .statue_modal_elem import *
from ..topbar_page import TopBarPage


# @Time :18/1/22 下午4:52
# @Author :huangcaiyan
# @File : statue_modal_page
# @Software : PyCharm


class StatueModalPage:

    def __init__( self, driver ):
        self.driver = driver

    def reject( self ):
        """
        :return: 驳回审核
        """
        topBarPage = TopBarPage(self.driver)
        publicPage = PublicPage(self.driver)
        topBarPage.click_operation_btn('驳回审核')
        self.reject_submit('是')
        publicPage.wait_until_loader_disapeared()

    def submission( self ):
        """
        :return:提交审核（计提）
        """
        topBarPage = TopBarPage(self.driver)
        publicPage = PublicPage(self.driver)
        topBarPage.click_operation_btn('提交审核（计提）')
        publicPage.wait_until_loader_disapeared()

    def carry_forward( self ):
        """
        :return: 结转
        """
        publicPage = PublicPage(self.driver)
        topBarPage = TopBarPage(self.driver)
        topBarPage.click_operation_btn('结转')
        self.carry_forward_submit('知道了')
        publicPage.wait_until_loader_disapeared()

    def re_carry_forward( self ):
        """
        :return:再次结转
        """
        publicPage = PublicPage(self.driver)
        topBarPage = TopBarPage(self.driver)
        topBarPage.click_operation_btn('再次结转')
        self.carry_forward_submit('直接结转')
        publicPage.wait_until_loader_disapeared()

    def posting( self ):
        """
        :return: 过帐
        """
        publicPage = PublicPage(self.driver)
        topBarPage = TopBarPage(self.driver)
        topBarPage.click_operation_btn('过帐')
        self.submit('过帐')
        publicPage.wait_until_loader_disapeared()

    def reverse_posting( self ):
        """
        :return:反过帐
        """
        publicPage = PublicPage(self.driver)
        topBarPage = TopBarPage(self.driver)
        topBarPage.click_operation_btn('反过帐')
        publicPage.wait_until_loader_disapeared()

    # ------------------------------------------------------------------------------------------------------------------
    # 弹窗确认
    def reject_submit( self, btn_name ):
        """
        :param btn_name:可选值（是、否）
        :return:确认 驳回审核、取消 驳回审核
        """
        if btn_name == '是':
            btn_elem = dismission_confirm_btn_elem
        elif btn_name == '否':
            btn_elem = dismission_confirm_btn_elem
        else:
            btn_elem = None
            print('[reject_submit]btn_name输入错误，请重新输入！')
        publicPage = PublicPage(self.driver)
        btn_loc = self.driver.find_element_by_xpath(btn_elem)
        publicPage.click_elem(btn_loc)

    def carry_forward_submit( self, btn_name ):
        """
        :param btn_name:可选值（查看科目余额表、知道了）
        :return:结转 确认
        """
        if btn_name == '查看科目余额表':
            btn_elem = account_balance_sheet_btn_elem
        elif btn_name == '知道了':
            btn_elem = carry_forward_ok_btn_elem
        else:
            print('[carry_forward_submit]btn_name输入错误，请重新输入')
        publicPage = PublicPage(self.driver)
        btn_loc = self.driver.find_element_by_xpath(btn_elem)
        publicPage.click_elem(btn_loc)

    def re_carry_forward_submit( self, btn_name ):
        """
        :param btn_name:弹窗按钮名称，可选值（重新整理、直接结转）
        :return:再次结转 确认
        """
        if btn_name == '重新整理':
            btn_elem = re_organize_btn_elem
            name = '重新整理凭证编号'
        elif btn_name == '直接结转':
            btn_elem = direct_carry_forward_btn_elem
            name = '直接结转'
        else:
            print('[re_carry_forward_submit]btn_name输入错误，请重新输入')
        publicPage = PublicPage(self.driver)
        btn_loc = self.driver.find_element_by_xpath(btn_elem)
        print('[当前操作是：', name)
        publicPage.click_elem(btn_loc)

        topBarPage = TopBarPage(self.driver)
        topBarPage.click_operation_btn('')

    def posting_submit( self, btn_name ):
        """
        :param btn_name:弹窗按钮名称，可选值（过帐、取消）
        :return:过帐 确认
        """
        if btn_name == '过帐':
            btn_elem = posting_confirm_elem
            name = '确认过帐'
        elif btn_name == '取消':
            btn_elem = posting_cancel_elem
            name = '取消过帐'
        else:
            btn_elem = None
            print('[posting_submit]btn_name输入错误，请重新输入')
        btn_loc = self.driver.find_element_by_xpath(btn_elem)
        publicPage = PublicPage(self.driver)
        print('[当前操作是：', name)
        publicPage.click_elem(btn_loc)

    # ------------------------------------------------------------------------------------------------------------------
    # 弹窗
    def get_modal_title( self ):
        """
        :return:弹窗标题
        """
        publicPage = PublicPage(self.driver)
        title_loc = self.driver.find_element_by_css_selector(modal_title_elem)
        publicPage.get_value(title_loc)

    def get_modal_body_text( self ):
        """
        :return:弹窗提示内容
        """
        publicPage = PublicPage(self.driver)
        text_loc = self.driver.find_element_by_xpath(modal_body_text_elem)
        publicPage.get_value(text_loc)
