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
from util.category_map_util import CategoryMap
import xlrd

class RecordInputInvoiceSpec(unittest.TestCase):
    ''' 记收票测试 '''

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = Driver
        EnterCompany(self.driver,Environment)
        invoice_page = InvoicePage(self.driver,'input')
        invoice_page.goToInvoice(BaseUrl)

    def test1(self):
        '''记录所有类别的收票-普票'''

        invoice_page = InvoicePage(self.driver,'input')
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/' + '../../test_data/' + '发票.xlsx')
        sh = wb.sheet_by_name(u'记收普票测试数据')
        for i in range(1,sh.nrows):
            sourceRowList = sh.row_values(i)
            targetList = CategoryMap().inputInvoiceCategeoryCommMapList(sourceRowList)
            invoice_page.recordCommonIncomeInvoice(targetList[:3],targetList[3:])

        invoice_page.goToInvoiceList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/invoice/input-invoice',self.driver.current_url)

    def test2(self):
        '''记所有类别的收票-专票'''

        invoice_page = InvoicePage(self.driver,'input')
        invoiceNumList = []
        for i in range(0,68):
            invoiceNumList.append(self.invoiceNum())

        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/' + '../../test_data/' + '发票.xlsx')
        sh = wb.sheet_by_name(u'记收专票测试数据')
        for i,invoiceNum in zip(range(1,sh.nrows),invoiceNumList):
            sourceRowList = sh.row_values(i)
            targetList = CategoryMap().inputInvoiceCategeorySpecMapList(sourceRowList)
            invoice_page.recordSpecialIncomeInvoice(targetList[:3],invoiceNum,targetList[3:])
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

