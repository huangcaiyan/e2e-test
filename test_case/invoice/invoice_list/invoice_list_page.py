from selenium import webdriver
import time
from util.public_page import PublicPage
from invoice_list_elem import *


class InvoiceListPage(object):
    # base_url:主页地址
    # invoice_io:(input,output)
    def __init__(self, driver, base_url, invoice_io):
        self.driver = webdriver.Chrome()
        self.driver = driver
        self.base_url = base_url
        self.invoice_io = invoice_io
        if self.invoice_io == 'input':
            global page_name = '收票'
        elif self.invoice_io == 'output':
            global page_name = '开票'
        else:
            print(
                '[InvoiceListPage]－－获取 self.invoice_io 失败 \nself.invoice_io =', self.invoice_io)

    # 去开／收票列表页面
    def go_to_invoice_list_page(self):
        try:
            publicPage = PublicPage(self.driver)
            page_url = self.base_url + '/app/invoice/' + self.invoice_io + '-invoice'
            self.driver.get(page_url)
            if publicPage.wait_until_loader_disapeared() == False:
                curent_url = self.driver.current_url
                if curent_url == page_url:
                    print('[InvoiceListPage]go_to_invoice_list_page －－去'+self.invoice_io + '页面 成功！－－')
                else:
                    print('[InvoiceListPage]go_to_invoice_list_page ＋＋去'+self.invoice_io + '页面 失败！＋＋')
            else:
                print('[InvoiceListPage]go_to_invoice_list_page ＋＋去'+self.invoice_io + '页面 失败！＋＋ \n失败原因：一直显示正在家在的状态，超时！')
        except Exception as e:
            print('[InvoiceListPage]go_to_invoice_list_page ＋＋去'+self.invoice_io + '页面 失败！＋＋ \n失败原因=',str(e))
            

    # 取得开／收票总额
    def get_list_total(self):
        try:
            publicPage = PublicPage(self.driver)
            elem_loc = self.driver.find_element_by_xpath(
                list_base_elem + self.invoice_io + list_total_elem)
            publicPage.get_value(elem_loc)
        except Exception as e:
            print('[InvoiceListPage]get_list_total－－获取' +
                  page_name + '总额失败，失败原因是＝', str(e))

    # 点击记收／开票按钮
    def click_record_invoice_btn(self):
        try:
            publicPage = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(
                list_base_elem + self.invoice_io + record_invoice_btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print('[InvoiceListPage]click_record_invoice_btn－－点击 记' +
                  page_name + '按钮失败，失败原因是＝', str(e))
