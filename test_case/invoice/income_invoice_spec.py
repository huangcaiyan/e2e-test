import unittest
import sys
import os
from selenium import webdriver
import time
import random
from collections import Iterator
from HTMLTestRunner import HTMLTestRunner
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from test_case.login.login_page import LoginPage
from invoice_page import InvoicePage
from test_data.record_income_invoice_data import *


#前置条件：新账套
class RecordIncomeInvoiceSpec(unittest.TestCase):
    ''' 记收票测试 '''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.baseUrl = 'http://guanplus-app-accountingfirm-web-dev-1.cn-north-1.eb.amazonaws.com.cn'
        login_page = LoginPage(self.baseUrl, self.driver)
        login_page.login('18514509382', 'qq123456')
        self.invoice_page = InvoicePage(self.driver)
        self.invoice_page.goToCompany('2206一般纳税人')
        self.invoice_page.goToInvoice(self.baseUrl,'input')

    # def test1(self):
    #     '''记录所有类别的收票-普票'''

    #     commonPublicInvoice = ['1','普票','内部代表']
    #     for commonItems in commonIncomeInvoiceCategory:
    #         self.invoice_page.recordCommonIncomeInvoice(commonPublicInvoice,commonItems)
    #         self.invoice_page.goToInvoice(self.baseUrl,'input')

    def test2(self):
        '''记所有类别的收票-专票'''

        specialPublicInvoice = ['1','专票','内部代表']
        invoiceNumList = []
        for i in range(0,33):
            invoiceNumList.append(self.invoiceNum())

        for specialItems,invoiceNum in zip(specialIncomeInvoiceCategory,invoiceNumList):
             self.invoice_page.recordSpecialIncomeInvoice(specialPublicInvoice,invoiceNum,specialItems)
             self.invoice_page.goToInvoice(self.baseUrl,'input')

    #生成8位随机正数
    def invoiceNum(self):
        invoiceNum = ''
        for i in range(0,8) :
            invoiceNum = invoiceNum + str(random.randint(0,9))
        return invoiceNum

    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()

