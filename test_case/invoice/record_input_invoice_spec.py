import unittest
import sys
import os
from selenium import webdriver
import time
import random
from collections import Iterator
from HTMLTestRunner import HTMLTestRunner
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from .invoice_page import InvoicePage
from test_data.record_input_invoice_data import *
from util.enter_company_util import EnterCompany
from config import *


class RecordInputInvoiceSpec(unittest.TestCase):
    ''' 记收票测试 '''

    def setUp(self):
        self.driver = webdriver.Chrome()
        EnterCompany(self.driver,Environment)
        invoice_page = InvoicePage(self.driver,'input')
        invoice_page.goToInvoice(BaseUrl)

    def test1(self):
        '''记录所有类别的收票-普票'''

        invoice_page = InvoicePage(self.driver,'input')
        commonPublicInvoice = ['1','普票','内部代表']
        for commonItems in RecordCommonInputInvoiceData:
            invoice_page.recordCommonIncomeInvoice(commonPublicInvoice,commonItems)
        invoice_page.goToInvoiceList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/invoice/input-invoice',self.driver.current_url)

    def test2(self):
        '''记所有类别的收票-专票'''

        invoice_page = InvoicePage(self.driver,'input')
        specialPublicInvoice = ['1','专票','内部代表']
        invoiceNumList = []
        for i in range(0,33):
            invoiceNumList.append(self.invoiceNum())

        for specialItems,invoiceNum in zip(RecordSpecialInputInvoiceData,invoiceNumList):
             invoice_page.recordSpecialIncomeInvoice(specialPublicInvoice,invoiceNum,specialItems)
        invoice_page.goToInvoiceList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/invoice/input-invoice',self.driver.current_url)   

    #生成8位随机整数
    def invoiceNum(self):
        invoiceNum = ''
        for i in range(0,8) :
            invoiceNum = invoiceNum + str(random.randint(0,9))
        return invoiceNum

    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()

