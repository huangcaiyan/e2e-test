import unittest
import sys
import os
from selenium import webdriver
import time
from collections import Iterator
from HTMLTestRunner import HTMLTestRunner
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from test_case.login.login_page import LoginPage
from .transaction_page import TransactionPage
from test_data.record_outcome_data import *
from util.enter_company_util import EnterCompany
from config import *
from util.category_map_util import CategoryMap
from util.driver_util import Driver
import xlrd


class RecordOutcomeSpec(unittest.TestCase):
    ''' 记支出测试 '''

    def setUp(self):
        self.driver = Driver().get_driver()
        enterCompany = EnterCompany(self.driver)
        enterCompany.goToCompany()
        self.transaction_page = TransactionPage(self.driver,'outcome')
        self.transaction_page.goToTransactionModule(BaseUrl)
        self.transaction_page.goToTransactionPage('记支出')

    def test1(self):
        '''全空校验'''

        self.transaction_page.clickSaveButton()
        self.assertEqual('请填写交易账户！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[1]/alert/div').text[-8:])

    def test2(self):
        '''交易账户-空校验'''

        self.transaction_page.setCategory(['1','1'])  
        self.transaction_page.setMoney('123')
        self.transaction_page.clickSaveButton()
        self.assertEqual('请填写交易账户！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[1]/alert/div').text[-8:])

    def test3(self):
        '''类别-空校验'''

        self.transaction_page.setAccount('现金')
        self.transaction_page.setMoney('111')  
        self.transaction_page.clickSaveButton()
        self.assertEqual('请填写完整！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[1]/alert/div').text[-6:])

    def test4(self):
        '''金额-空校验'''

        self.transaction_page.setCategory(['1','1'])  
        self.transaction_page.setAccount('现金')
        self.transaction_page.clickSaveButton()
        self.assertEqual('金额不能为0！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[1]/alert/div').text[-7:])

    def test5(self):
        '''金额为0测试'''

        self.transaction_page.setCategory(['1','1'])  
        self.transaction_page.setAccount('现金')
        self.transaction_page.setMoney('0')
        self.transaction_page.clickSaveButton()
        self.assertEqual('金额不能为0！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[1]/alert/div').text[-7:])

    def test6(self):
        '''成功记一笔支出测试'''

        transaction = ['1','现金','(个)内部代表']
        items1 = [['1','1'],'111','行政支出']
        self.transaction_page.recordTransaction(transaction,items1)
        self.assertEqual('保存成功',self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[1]/alert/div').text[-4:])

    def test7(self):
        '''成功记两笔明细支出测试'''

        publicTransaction = ['1','现金','内部代表']   
        items1 = [['1','1'],'111','行政支出']
        items2 = [['2','1'],'211','资金往来']     
        self.transaction_page.setPublicTransaction(publicTransaction)
        self.transaction_page.setTransactionItems(items1)
        self.transaction_page.clickAddItems()
        self.transaction_page.setItemsNumber('2')
        self.transaction_page.setTransactionItems(items2)
        self.transaction_page.clickSaveButton()
        self.assertEqual(BaseUrl + '/app/transaction/list',self.driver.current_url)

    def test8(self):
        '''成功记所有类别支出测试'''
    
        transaction_page = TransactionPage(self.driver,'outcome')
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/' + '../../test_data/' + '收支.xlsx')
        sh = wb.sheet_by_name(u'记支出测试数据')
        for i in range(1,sh.nrows):
            sourceRowList = sh.row_values(i)
            targetList = CategoryMap().outcomeCategeoryMapList(sourceRowList)
            transaction_page.recordTransaction(targetList[:3],targetList[3:])
        transaction_page.goToTransactionModule(BaseUrl)
        self.assertEqual(BaseUrl + '/app/transaction/list',self.driver.current_url)

    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()

