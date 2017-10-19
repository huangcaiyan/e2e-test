from selenium import webdriver
import time
import sys 
import os
# sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from util.public_page import PublicPage
from .income_outcome_elem import *

# 记收入、支出、互转测试
# 创建于2017-10-16-周二
# caicai


class RecordTransactionPage():
    """记收入支出互转测试"""

    # base_url:主页地址
    # record_type:（Income，Ountcome，accountTransfers）
    # record_name：（income,outcome,accounttransfers)
    def __init__(self, driver, base_url, record_type):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.base_url = base_url
        self.record_type = record_type
        if self.record_type == 'Income':
            self.record_name = 'income'
        elif self.record_type == 'Outcome':
            self.record_name = 'outcome'
        elif self.record_type == 'accountTransfers':
            self.record_name = 'accounttransfers'

    # 去记收入、支出、互转页面
    def go_to_record_transaction_page(self):
        try:
            self.driver.get(
                self.base_url + '/app/transaction/detail/' + self.record_type)
            time.sleep(3)
            page_url =self.driver.current_url
            if self.record_type in page_url:
                print('[RecordTransactionPage]－－－') 
        except Exception as e:
            print(
                '[RevenueAndExpenditurePage] There was an exception when go_to_record_page=>', str(e))

    # －－－记收支－－－
    #  选择账户
    # record_name:(income,outcome)
    # account_name:账户名称
    def select_account(self, account_name):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(
                page_base_xpath_elem + self.record_name + account_drop_end_xpath_elem)
            publicPage.select_dropdown_item(drop_loc, account_name)
        except Exception as e:
            print(
                '[RevenueAndExpenditurePage] There was an exception when select_account=>', str(e))

    # 选择往来
    # account_name:(income,outcome)
    # contact_name：往来名称
    def select_contact(self, contact_name):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(
                page_base_xpath_elem + self.record_name + contact_drop_end_xpath_elem)
            publicPage.select_dropdown_item(drop_loc, contact_name)
        except Exception as e:
            print(
                '[RevenueAndExpenditurePage] There was an exception when select_contact=>', str(e))

    

    # 选择类别
    # category：类别名称(收入／支出)
    def select_category(self, category):
        try:
            publicPage = PublicPage(self.driver)
            print(self.category_index(category))
            p_index = self.category_index(category)[0]
            c_index = self.category_index(category)[1]

            drop_loc = self.driver.find_element_by_xpath(
                page_base_xpath_elem + self.record_name + category_drop_end_xpath_elem)
            publicPage.click_elem(drop_loc)

            parent_loc = self.driver.find_elements_by_css_selector(parent_elem)[
                p_index]
            publicPage.click_elem(parent_loc)

            child_loc = self.driver.find_elements_by_css_selector(child_elem)[
                c_index]
            return publicPage.click_elem(child_loc)
        except Exception as e:
            print(
                '[RevenueAndExpenditurePage] There was an exception when select_category=>', str(e))

    # 输入总金额
    # total：金额(收入／支出)
    def set_total(self, total):
        try:
            if self.record_type == 'accountTransfers':
                input_elem = transfer_total_elem
            else:
                input_elem = total_elem
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                page_base_xpath_elem + self.record_name + input_elem)
            publicPage.set_value(input_loc, total)
        except Exception as e:
            print(
                '[RevenueAndExpenditurePage] There was an exception when set_total=>', str(e))

    # 输入标签
    # attachment：标签内容(收入／支出)
    def set_attachment(self, attachment):
        try:
            if self.record_type == 'accountTransfers':
                input_elem = transfer_attachment_elem
            else:
                input_elem = attachment_elem
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                page_base_xpath_elem + self.record_name + input_elem)
            publicPage.set_value(input_loc, attachment)
        except Exception as e:
            print(
                '[RevenueAndExpenditurePage] There was an exception when set_attachment=>', str(e))
                

    # 点击保存并新增按钮(收入／支出)
    def click_save_and_new_btn(self):
        try:
            if self.record_type == 'accountTransfers':
                btn_elem = transfer_save_and_new_btn_elem
            else:
                btn_elem = save_and_new_btn_elem
            publicPage = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(
                page_base_xpath_elem + self.record_name + btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print(
                '[RevenueAndExpenditurePage] There was an exception when click_save_and_new_btn=>', str(e))

    # 点击保存按钮(收入／支出)
    def click_save_btn(self):
        try:
            if self.record_type == 'accountTransfers':
                btn_elem = transfer_save_btn_elem
            else:
                btn_elem = save_btn_elem
            publicPage = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(
                page_base_xpath_elem + self.record_name + btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print(
                '[RevenueAndExpenditurePage] There was an exception when click_save_btn=>', str(e))

    # 点击取消按钮(收入／支出)
    def click_cancel_btn(self):
        try:
            if self.record_type == 'accountTransfers':
                btn_elem == transfer_cancel_btn_elem
            else:
                btn_elem = cancel_btn_elem
            publicPage = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(
                page_base_xpath_elem + self.record_name + btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print(
                '[RevenueAndExpenditurePage] There was an exception when click_cancel_btn=>', str(e))

    # －－－记互转－－－
    # 选择转出转入账户
    # output_account：转出账户
    # input_account：转入账户
    def select_transfer_account(self, output_account, input_account):
        try:
            publicPage = PublicPage(self.driver)
            output_drop_loc = self.driver.find_element_by_xpath(
                page_base_xpath_elem + self.record_name + output_account_drop_elem)
            publicPage.select_dropdown_item(output_drop_loc, output_account)

            input_drop_loc = self.driver.find_element_by_xpath(
                page_base_xpath_elem + self.record_name + input_account_drop_elem)
            publicPage.select_dropdown_item(input_drop_loc, input_account)
        except Exception as e:
            print(
                '[RevenueAndExpenditurePage] There was an exception when select_transfer_account=>', str(e))

    # 记收入／支出
    def record_income_and_outcome(self, revenue_and_expenditure_data):
        self.select_account(revenue_and_expenditure_data[2])
        self.select_contact(revenue_and_expenditure_data[3])
        self.select_category(revenue_and_expenditure_data[4])
        self.set_total(revenue_and_expenditure_data[5])
        self.set_attachment(revenue_and_expenditure_data[6])
        self.click_save_and_new_btn()
        time.sleep(2)

    # 记互转
    def record_transfer(self, transfer_data):
        self.select_transfer_account(transfer_data[2], transfer_data[3])
        self.set_total(transfer_data[4])
        self.set_attachment(transfer_data[5])
        self.click_save_and_new_btn()

    # 类别index
    # category：类别名称
    # p_c_arr = [parent_index,child_index]
    def category_index(self, category):
        try:
            p_c_arr = []
            if self.record_name == 'income':
                if category == '利息收入':
                    p_c_arr = [0, 0]
                    return p_c_arr
                elif category == '回收借出资金(收入)':
                    p_c_arr = [1, 0]
                    return p_c_arr
                elif category == '收到临时借入款(收入)':
                    p_c_arr = [1, 1]
                    return p_c_arr
                elif category == '收回投资利息(收入)':
                    p_c_arr = [2, 0]
                    return p_c_arr
                elif category == '收回投资本金(收入)':
                    p_c_arr = [2, 1]
                    return p_c_arr
                elif category == '收到投资款':
                    p_c_arr = [2, 2]
                    return p_c_arr
                elif category == '银行贷款(收入)':
                    p_c_arr = [2, 3]
                    return p_c_arr
                elif category == '应收账款':
                    p_c_arr = [3, 0]
                    return p_c_arr
            elif self.record_name == 'outcome':
                if category == '银行费用':
                    p_c_arr = [0, 0]
                    return p_c_arr
                elif category == '临时借出资金':
                    p_c_arr = [1, 0]
                    return p_c_arr
                elif category == '归还临时借入':
                    p_c_arr = [1, 1]
                    return p_c_arr
                elif category == '对外投资款':
                    p_c_arr = [2, 0]
                    return p_c_arr
                elif category == '归还银行贷款':
                    p_c_arr = [2, 1]
                    return p_c_arr
                elif category == '贷款利息':
                    p_c_arr = [2, 2]
                    return p_c_arr
                elif category == '应付工资奖金':
                    p_c_arr = [3, 0]
                    return p_c_arr
                elif category == '应付社保费':
                    p_c_arr = [3, 1]
                    return p_c_arr
                elif category == '应付公积金':
                    p_c_arr = [3, 2]
                    return p_c_arr
                elif category == '应付劳务费':
                    p_c_arr = [3, 3]
                    return p_c_arr
                elif category == '应交增值税':
                    p_c_arr = [4, 0]
                    return p_c_arr
                elif category == '应交城建税':
                    p_c_arr = [4, 1]
                    return p_c_arr
                elif category == '应交教育附加':
                    p_c_arr = [4, 2]
                    return p_c_arr
                elif category == '应交地方教育附加':
                    p_c_arr = [4, 3]
                    return p_c_arr
                elif category == '应交个税':
                    p_c_arr = [4, 4]
                    return p_c_arr
                elif category == '应交印花税':
                    p_c_arr = [4, 5]
                    return p_c_arr
                elif category == '应交所得税':
                    p_c_arr = [4, 6]
                    return p_c_arr
                elif category == '应付账款':
                    p_c_arr = [5, 0]
                    return p_c_arr
            else:
                print(record_name + '－－－－－－选择类别失败－－－－－－')
        except Exception as e:
            print(
                '[RevenueAndExpenditurePage] There was an exception when category_index=>', str(e))
