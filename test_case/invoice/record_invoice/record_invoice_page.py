from selenium import webdriver
import time
import sys
import os
# sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from util.public_page import PublicPage
from .record_invoice_elem import *

# 记发票测试
# 创建于2017-10-17-周三
# caicai


class RecordInvoicePage():
    """记发票测试"""

    # base_url:主页地址
    # invoice_type:(input,output)
    def __init__(self, driver, base_url, invoice_io):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.base_url = base_url
        self.invoice_io = invoice_io

    def go_to_record_invoice_page(self):
        self.driver.get(self.base_url + '/app/invoice/tab/new-' +
                        self.invoice_io + '-invoice')
        if self.invoice_io == 'input':
            page_name = '记收票页面'
        elif self.invoice_io == 'output':
            page_name = '记开票页面'
        else:
            return 'error'
        page_url = self.driver.current_url
        if self.invoice_io in page_url:
            print('[RecordInvoicePage]－－－－－－成功进入' + page_name + '－－－－－－')
        else:
            print('[RecordInvoicePage]－－－－－－去记发票页面 失败－－－－－－')
            self.driver.quit()

    # 选择发票类型
    # invoice_type:开票（普票、专票、无票），收票（普票、专票）
    def select_invoice_type(self, invoice_type):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(
                record_invoice_base_xpath + self.invoice_io + invoice_type_drop_elem)
            publicPage.select_dropdown_item(drop_loc, invoice_type)
        except Exception as e:
            print('[RecordInvoicePage] －－选择发票类型失败－－失败原因是->', str(e))

    # 选择发票状态
    # invoice_status:(税控自开，税务代开)
    def select_invoice_status(self, invoice_status):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(
                record_invoice_base_xpath + self.invoice_io + invoice_status_drop_elem)
            publicPage.select_dropdown_item(drop_loc, invoice_status)
        except Exception as e:
            print('[RecordInvoicePage]－－选择发票状态失败－－失败原因是->', str(e))

    # 选择对方信息
    def select_contact(self, contact):
        try:
            if self.invoice_io == 'input':
                contact_drop_elem = input_contact_drop_elem
            elif self.invoice_io == 'output':
                contact_drop_elem = output_contact_drop_elem
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(
                record_invoice_base_xpath + self.invoice_io + contact_drop_elem)
            publicPage.select_dropdown_item(drop_loc, contact)
        except Exception as e:
            print('[RecordInvoicePage]－－选择对方信息失败－－失败原因是->', str(e))

    # 填写发票
    def set_invoice_num(self, invoice_num):
        try:
            if self.invoice_io == 'input':
                invice_num = input_invoice_num_elem
            elif self.invoice_io == 'output':
                invice_num = output_invoice_num_elem
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(
                record_invoice_base_xpath + self.invoice_io + invice_num)
            publicPage.select_dropdown_item(drop_loc, invoice_num)
        except Exception as e:
            print('[RecordInvoicePage]－－填写发票号失败－－失败原因是->', str(e))

    # 选择类别
    def select_category(self, category):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(
                record_invoice_base_xpath + self.invoice_io + category_drop_elem)
            publicPage.select_dropdown_item(drop_loc, category)
        except Exception as e:
            print('[RecordInvoicePage]－－选择类别失败－－失败原因是->', str(e))

    # 选择部门性质
    def select_department(self, department):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(
                record_invoice_base_xpath + self.invoice_io + department_drop_elem)
            publicPage.select_dropdown_item(drop_loc, category)
        except Exception as e:
            print('[RecordInvoicePage]－－选择部门性质失败－－失败原因是->', str(e))

    # 选择税率
    def select_tax_rate(self, tax_rate):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(
                record_invoice_base_xpath + self.invoice_io + department_drop_elem)
            publicPage.select_dropdown_item(drop_loc, category)
        except Exception as e:
            print('[RecordInvoicePage]－－选择部门性质失败－－失败原因是->', str(e))

    # 选择进项税类别
    def select_input_tax_category(self, input_tax_category):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(
                record_invoice_base_xpath + self.invoice_io + input_tax_category_drop_elem)
            publicPage.select_dropdown_item(drop_loc, input_tax_category)
        except Exception as e:
            print('[RecordInvoicePage]－－选择进项税类别失败－－失败原因是->', str(e))

    # 设置价税合计
    def set_total(self, total):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                record_invoice_base_xpath + self.invoice_io + total_elem)
            publicPage.set_value(input_loc, total)
        except Exception as e:
            print('[RecordInvoicePage]－－设置价税合计失败－－失败原因是->', str(e))

    # 备注
    def set_attachment(self):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                record_invoice_base_xpath + self.invoice_io + attachment_elem)
            publicPage.set_value(input_loc, total)
        except Exception as e:
            print('[RecordInvoicePage]－－设置备注失败－－失败原因是->', str(e))

    # 点击保存并新增
    def submit(self, btn_name):
        try:
            if btn_name == 'save_and_new':
                btn_elem = save_and_new_btn_elem
                submit_name = '保存并新增'
            elif btn_name == 'save':
                btn_elem = save_btn_elem
                submit_name = '保存'
            elif btn_name == 'cancel':
                btn_elem = cancel_btn_elem
                submit_name = '取消'
            publicPage = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(
                record_invoice_base_xpath + self.invoice_io + btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print('[RecordInvoicePage]－－' +
                  submit_name + '失败－－失败原因是->', str(e))

    # 记发票
    def record_invoice(self, invoice_data):
        self.select_invoice_type(invoice_data[0])
        self.select_contact(invoice_data[1])
        invoice_num = PublicPage(self.driver).eight_random_nums()
        if self.invoice_io == 'input':
            if invoice_data[0] == '专票':
                self.set_invoice_num(invoice_data[2] + invoice_num)
                self.select_input_tax_category(invoice_data[6])
            self.select_category(invoice_data[3])
            self.select_department(invoice_data[4])
            self.select_tax_rate(invoice_data[5])

        elif self.invoice_io == 'output':
            if invoice_data[0] == '普票' or invoice_data[0] == '专票':
                self.set_invoice_num(invoice_data[3] + invoice_num)
            self.select_contact(invoice_data[2])
            self.select_category(invoice_data[4])
            self.select_department(invoice_data[5])
            self.select_tax_rate(invoice_data[6])
        self.set_total(invoice_data[7])
        self.set_attachment(invoice_data[8])

    # 类别转义
    def category_index(self, category):
        try:
            p_c_index = []
            if sel == 'input':
                if category == '福利费':
                    p_c_index = [0, 0]
                elif category == '劳务费':
                    p_c_index = [0, 1]
                elif category == '招待费':
                    p_c_index = [1, 0]
                elif category == '办公费':
                    p_c_index = [1, 1]
                elif category == '快递费':
                    p_c_index = [1, 2]
                elif category == '通讯费':
                    p_c_index = [1, 3]
                elif category == '维修费':
                    p_c_index = [1, 4]
                elif category == '财产保险费':
                    p_c_index = [1, 5]
                elif category == '设备租赁费':
                    p_c_index = [1, 6]
                elif category == '银行费用':
                    p_c_index = [1, 7]
                elif category == '差旅费':
                    p_c_index = [2, 0]
                elif category == '交通费':
                    p_c_index = [2, 1]
                elif category == '汽油费':
                    p_c_index = [2, 2]
                elif category == '路桥费':
                    p_c_index = [2, 3]
                elif category == '汽车维修费':
                    p_c_index = [2, 4]
                elif category == '汽车保险费':
                    p_c_index = [2, 5]
                elif category == '物流费':
                    p_c_index = [2, 6]
                elif category == '房租费':
                    p_c_index = [3, 0]
                elif category == '物业费':
                    p_c_index = [3, 1]
                elif category == '水费':
                    p_c_index = [3, 2]
                elif category == '电费':
                    p_c_index = [3, 3]
                elif category == '仓储费':
                    p_c_index = [3, 4]
                elif category == '装修费':
                    p_c_index = [3, 5]
                elif category == '广告费':
                    p_c_index = [4, 0]
                elif category == '宣传费':
                    p_c_index = [4, 1]
                elif category == '研发费':
                    p_c_index = [4, 2]
                elif category == '会议费':
                    p_c_index = [4, 3]
                elif category == '服务费':
                    p_c_index = [4, 4]
                elif category == '咨询费':
                    p_c_index = [4, 5]
                elif category == '认证费':
                    p_c_index = [4, 6]
                elif category == '专利费':
                    p_c_index = [4, 7]
                elif category == '工会经费':
                    p_c_index = [4, 8]
                elif category == '其他':
                    p_c_index = [4, 9]
                elif category == '行政罚款':
                    p_c_index = [5, 0]
                elif category == '税务滞纳金':
                    p_c_index = [5, 1]
                elif category == '印花税':
                    p_c_index = [6, 0]
                elif category == '残保金':
                    p_c_index = [6, 1]
                elif category == '减免税款':
                    p_c_index = [6, 2]
                elif category == '原材料':
                    p_c_index = [7, 0]
                elif category == '商品产品':
                    p_c_index = [7, 1]
            elif self.invoice_io == 'output':
                if category == '商品销售':
                    p_c_index = [0, 0]
                elif category == '服务收入':
                    p_c_index = [1, 0]
            else:
                return 'error'
        except Exception as e:
            print('[RecordInvoicePage]－－－发票类别转义失败－－－失败原因是->', str(e))
