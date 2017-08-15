import unittest
import sys
import os
from selenium import webdriver
import time
import random
from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import logging
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from util.enter_company_util import EnterCompany
from util.generate_random_util import GenerateRandom
from util.category_map_util import CategoryMap
from util.create_company_util import CreateCompay
from util.decorator_util import exit_test
from config import *
import xlrd
from test_case.login.login_page import LoginPage
from test_case.transaction.transaction_page import TransactionPage
from test_case.invoice.invoice_page import InvoicePage
from test_case.fixedassets.fixedassets_page import FixedassetsPage
from test_case.call_api.call_account_token_api import CallAccountTokenApi
from test_case.call_api.call_accountbook_search_api import CallAccountBookSearchApi
from test_case.call_api.call_journalEntry_search_api import CallJournalEntrySearchApi

class PositiveFlowSpec(unittest.TestCase):
    ''' 业务流程测试 '''

    @classmethod
    def setUpClass(self):
        # try:
        #     self.driver = Driver
        #     #创建公司->分配角色->启用期初账->进入账套
        #     cc = CreateCompay(self.driver)
        #     cc.get(BaseUrl)
        #     wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '创建公司.xlsx')
        #     loginSh = wb.sheet_by_name(u'登陆账号')
        #     loginRow = loginSh.row_values(1)
        #     roleSh = wb.sheet_by_name(u'设置角色')
        #     roleRow = roleSh.row_values(1)
        #     createCompanySh = wb.sheet_by_name(u'创建公司测试数据')
        #     createCompanyRow = createCompanySh.row_values(1)
        #     now = datetime.now()
        #     createCompanyRow[0]=createCompanyRow[0]+now.strftime('%m%d%H%M')
        #     createCompanyRow[7]=GenerateRandom().generateRandom()
        #     goToCompanyPara = [loginRow,createCompanyRow,roleRow]
        #     cc.goToCompany(goToCompanyPara)
        #     #创建三个账户：招商银行，羊羊羊微信，羊羊羊支付宝
        #     cc.goToCreateAccountPage(BaseUrl)
        #     accountSh = wb.sheet_by_name(u'创建账户')
        #     for i in range(1,accountSh.nrows):
        #         accountRow = accountSh.row_values(i)
        #         cc.createAccount(accountRow[0],accountRow[1])
        #         cc.goToCreateAccountPage(BaseUrl)

        # except Exception as e:
        #     print('===========================初始化环境失败=========================================')
        #     self.skipTest(PositiveFlowSpec,'初始化环境失败')
        pass

    @classmethod
    def tearDownClass(self):
        # self.driver.quit()
        pass

    def test1(self):
        '''记所有类别的-收入'''

        transaction_page = TransactionPage(self.driver,'income')
        transaction_page.goToTransactionModule(BaseUrl)
        transaction_page.goToTransactionPage('记收入')
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '收支.xlsx')
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
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '收支.xlsx')
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
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '收支.xlsx')
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
       wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '发票.xlsx')
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
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '发票.xlsx')
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
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '发票.xlsx')
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
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '固定资产.xlsx')
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
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '固定资产.xlsx')
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
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '固定资产.xlsx')
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
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '固定资产.xlsx')
        sh = wb.sheet_by_name(u'记无形资产专票测试数据')
        invoiceNumList = GenerateRandom().invoiceNumList(sh.nrows-1)
        for i,invoiceNum in zip(range(1,sh.nrows),invoiceNumList):
            sourceRowList = sh.row_values(i)
            targetPara = [sourceRowList[:5],sourceRowList[5:]]
            fixedassets_page.recordFixedassetsSpec(targetPara,invoiceNum)

        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/intangible-list',self.driver.current_url)

    def test11(self):
        '''凭证校验'''

        #获取Authorization和company_id
        callAccountToken = CallAccountTokenApi()
        auComDataList = callAccountToken.getAuthorizationComid()
        #获取accountbook_id
        callAccountBookSearch = CallAccountBookSearchApi()
        accountBookDict = callAccountBookSearch.getAccountBook(auComDataList)
        accountBookId = accountBookDict['羊羊羊08121546']
        #获取凭证列表数据
        callJournalEntrySearch = CallJournalEntrySearchApi()
        journalList = callJournalEntrySearch.getJournalList([auComDataList[0],auComDataList[1],accountBookId[0]])
        #读取预期的凭证数据
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../../test_data/' + '收支.xlsx')
        sh = wb.sheet_by_name(u'收入记录凭证校验数据')
        for expect,actual in zip(range(1,sh.nrows),journalList):
            sourceRowList = sh.row_values(i)
            for i in sourceRowList:
                

