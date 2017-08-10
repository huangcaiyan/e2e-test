import unittest
import sys
import os
from selenium import webdriver
import time
import random
from HTMLTestRunner import HTMLTestRunner
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../../'))
from util.enter_company_util import EnterCompany
from util.generate_random_util import GenerateRandom
from util.category_map_util import CategoryMap
from util.create_company_util import CreateCompay
from config import *
import xlrd
from test_case.transaction.transaction_page import TransactionPage
from test_case.invoice.invoice_page import InvoicePage
from test_case.fixedassets.fixedassets_page import FixedassetsPage


class RecordBusinessSpec(unittest.TestCase):
    ''' 记业务单测试 '''

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.PhantomJS()
        EnterCompany(self.driver,Environment)
    
    def test1(self):
        '''记所有类别的-收入'''

        transaction_page = TransactionPage(self.driver,'income')
        transaction_page.goToTransactionModule(BaseUrl)
        transaction_page.goToTransactionPage('记收入')
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../../test_data/' + '收支.xlsx')
        sh = wb.sheet_by_name(u'记收入测试数据')
        for i in range(1,sh.nrows):
            sourceRowList = sh.row_values(i)
            targetList = CategoryMap().incomeCategoryMapList(sourceRowList)
            transaction_page.recordTransaction(targetList[:3],targetList[3:])
        
        transaction_page.goToTransactionModule(BaseUrl)
        self.assertEqual(BaseUrl + '/app/transaction/list',self.driver.current_url)
       
    def test2(self):
        '''记所有类别的-支出'''

        transaction_page = TransactionPage(self.driver,'outcome')
        transaction_page.goToTransactionModule(BaseUrl)
        transaction_page.goToTransactionPage('记支出')
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../../test_data/' + '收支.xlsx')
        sh = wb.sheet_by_name(u'记支出测试数据')
        for i in range(1,sh.nrows):
            sourceRowList = sh.row_values(i)
            targetList = CategoryMap().outcomeCategeoryMapList(sourceRowList)
            transaction_page.recordTransaction(targetList[:3],targetList[3:])
        transaction_page.goToTransactionModule(BaseUrl)
        self.assertEqual(BaseUrl + '/app/transaction/list',self.driver.current_url)
    
    def test3(self):
        '''记四个类型-账户互转[招商银行，现金，羊羊羊微信，羊羊羊支付宝]'''
        
        transaction_page = TransactionPage(self.driver,'accounttransfers')
        transaction_page.goToTransactionModule(BaseUrl)
        transaction_page.goToTransactionPage('记账户互转')
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../../test_data/' + '收支.xlsx')
        sh = wb.sheet_by_name(u'记账户互转测试数据')
        for i in range(1,sh.nrows):
            sourceRowList = sh.row_values(i)
            transaction_page.recordTransfer(sourceRowList)
        transaction_page.goToTransactionModule(BaseUrl)
        self.assertEqual(BaseUrl + '/app/transaction/list',self.driver.current_url)

    def test4(self):
       '''记收票-专票'''

       invoice_page = InvoicePage(self.driver,'input')
       invoice_page.goToInvoice(BaseUrl)
       wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../../test_data/' + '发票.xlsx')
       sh = wb.sheet_by_name(u'记收专票测试数据')
       invoiceNumList = GenerateRandom().invoiceNumList(sh.nrows-1)
       for i,invoiceNum in zip(range(1,sh.nrows),invoiceNumList):
                sourceRowList = sh.row_values(i)
                targetList = CategoryMap().inputInvoiceCategeorySpecMapList(sourceRowList)
                invoice_page.recordSpecialIncomeInvoice(targetList[:3],invoiceNum,targetList[3:])
       invoice_page.goToInvoiceList(BaseUrl)
       self.assertEqual(BaseUrl + '/app/invoice/input-invoice',self.driver.current_url)   


    def test5(self):
        '''记收票-普票'''

        invoice_page = InvoicePage(self.driver,'input')
        invoice_page.goToInvoice(BaseUrl)
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../../test_data/' + '发票.xlsx')
        sh = wb.sheet_by_name(u'记收普票测试数据')
        for i in range(1,sh.nrows):
            sourceRowList = sh.row_values(i)
            targetList = CategoryMap().inputInvoiceCategeoryCommMapList(sourceRowList)
            invoice_page.recordCommonIncomeInvoice(targetList[:3],targetList[3:])

        invoice_page.goToInvoiceList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/invoice/input-invoice',self.driver.current_url)

    def test6(self):
        '''记开票'''

        invoice_page = InvoicePage(self.driver,'output')
        invoice_page.goToInvoice(BaseUrl)
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../../test_data/' + '发票.xlsx')
        sh = wb.sheet_by_name(u'记开票测试数据')
        invoiceNumList = GenerateRandom().invoiceNumList(sh.nrows-1)
        for i,invoiceNum in zip(range(1,sh.nrows),invoiceNumList):
            sourceRowList = sh.row_values(i)
            targetList = CategoryMap().outputInvoiceCategeoryMapList(sourceRowList)
            invoice_page.recordOutputInvoice(targetList[:4],invoiceNum,targetList[4:])

        invoice_page.goToInvoiceList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/invoice/output-invoice',self.driver.current_url)
    
    def test7(self):
        '''记固定资产-普票'''

        fixedassets_page = FixedassetsPage(self.driver,'fixed')
        fixedassets_page.goToRecordFixedassetsPage(BaseUrl)
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../../test_data/' + '固定资产.xlsx')
        sh = wb.sheet_by_name(u'记固定资产普票测试数据')
        for i in range(1,sh.nrows):
            sourceRowList = sh.row_values(i)
            targetPara = [sourceRowList[:4],sourceRowList[4:]]
            fixedassets_page.recordFixedassetsComm(targetPara)

        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/list',self.driver.current_url)

    def test8(self):
        '''记固定资产-专票'''

        fixedassets_page = FixedassetsPage(self.driver,'fixed')
        fixedassets_page.goToRecordFixedassetsPage(BaseUrl)
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../../test_data/' + '固定资产.xlsx')
        sh = wb.sheet_by_name(u'记固定资产专票测试数据')
        invoiceNumList = GenerateRandom().invoiceNumList(sh.nrows-1)
        for i,invoiceNum in zip(range(1,sh.nrows),invoiceNumList):
            sourceRowList = sh.row_values(i)
            targetPara = [sourceRowList[:5],sourceRowList[5:]]
            fixedassets_page.recordFixedassetsSpec(targetPara,invoiceNum)

        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/list',self.driver.current_url)

    def test9(self):
        '''记无形资产-普票'''

        fixedassets_page = FixedassetsPage(self.driver,'intangible')
        fixedassets_page.goToRecordFixedassetsPage(BaseUrl)
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../../test_data/' + '固定资产.xlsx')
        sh = wb.sheet_by_name(u'记无形资产普票测试数据')
        for i in range(1,sh.nrows):
            sourceRowList = sh.row_values(i)
            targetPara = [sourceRowList[:4],sourceRowList[4:]]
            fixedassets_page.recordFixedassetsComm(targetPara)

        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/intangible-list',self.driver.current_url)

    def test10(self):
        '''记无形资产-专票'''

        fixedassets_page = FixedassetsPage(self.driver,'intangible')
        fixedassets_page.goToRecordFixedassetsPage(BaseUrl)
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../../test_data/' + '固定资产.xlsx')
        sh = wb.sheet_by_name(u'记无形资产专票测试数据')
        invoiceNumList = GenerateRandom().invoiceNumList(sh.nrows-1)
        for i,invoiceNum in zip(range(1,sh.nrows),invoiceNumList):
            sourceRowList = sh.row_values(i)
            targetPara = [sourceRowList[:5],sourceRowList[5:]]
            fixedassets_page.recordFixedassetsSpec(targetPara,invoiceNum)

        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/intangible-list',self.driver.current_url)

    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()

