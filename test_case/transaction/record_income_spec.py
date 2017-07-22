import unittest
import sys
import os
from selenium import webdriver
import time
from collections import Iterator
from HTMLTestRunner import HTMLTestRunner
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from test_case.login.login_page import LoginPage
from transaction_page import TransactionPage
from test_data.record_outcome_data import *


#前置条件：新账套
class RecordIncomeSpec(unittest.TestCase):
    ''' 记收入测试 '''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.baseUrl = 'https://web-gyz-stage.guanplus.com'
        login_page = LoginPage(self.baseUrl, self.driver)
        login_page.login('18514509382', 'qq123456')
        transaction_page = TransactionPage(self.driver,'income')
        transaction_page.goToCompany('testau1')
        transaction_page.goToTransactionModule(self.baseUrl)
        transaction_page.goToTransactionPage('记收入')

    def test1(self):
        '''全空校验'''

        transaction_page = TransactionPage(self.driver,'income')
        transaction_page.clickSaveButton()                                   
        self.assertEqual('请填写交易账户！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/income/div/div[1]/alert/div').text[-8:])

    def test2(self):
        '''交易账户-空校验'''

        transaction_page = TransactionPage(self.driver,'income')
        transaction_page.setCategory('1',['1','利息收入'])  
        transaction_page.setMoney('123')
        transaction_page.clickSaveButton()
        self.assertEqual('请填写交易账户！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/income/div/div[1]/alert/div').text[-8:])

    def test3(self):
        '''类别-空校验'''

        transaction_page = TransactionPage(self.driver,'income')
        transaction_page.setItemsNum('1')
        transaction_page.setAccount('现金')
        transaction_page.setMoney('111')  
        transaction_page.clickSaveButton()
        self.assertEqual('请填写完整！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/income/div/div[1]/alert/div').text[-6:])

    def test4(self):
        '''金额-空校验'''

        transaction_page = TransactionPage(self.driver,'income')
        transaction_page.setCategory('1',['1','利息收入'])  
        transaction_page.setAccount('现金')
        transaction_page.clickSaveButton()
        self.assertEqual('金额不能为0！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/income/div/div[1]/alert/div').text[-7:])

    def test5(self):
        '''金额为0测试'''

        transaction_page = TransactionPage(self.driver,'income')
        transaction_page.setCategory('1',['1','利息收入'])  
        transaction_page.setAccount('现金')
        transaction_page.setMoney('0')
        transaction_page.clickSaveButton()
        self.assertEqual('金额不能为0！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/income/div/div[1]/alert/div').text[-7:])

    def test6(self):
        '''成功记一笔收入测试'''

        transaction_page = TransactionPage(self.driver,'income')
        transaction = ['1','现金','内部代表']
        items1 = ['1',['1','利息收入'],'111','利息收入']
        transaction_page.recordTransaction(transaction,items1)
        self.assertEqual(self.baseUrl + '/app/transaction/list',self.driver.current_url)

    def test7(self):
        '''成功记两笔明细支出测试'''

        transaction_page = TransactionPage(self.driver,'income')
        publicTransaction = ['1','现金','内部代表']   
        items1 = ['1',['1','利息收入'],'111','利息收入']
        items2 = ['2',['2','回收借出资金(收入)'],'121','资金往来']     
        transaction_page.setPublicTransaction(publicTransaction)
        transaction_page.setTransactionItems(items1)
        transaction_page.clickAddItems()
        transaction_page.setTransactionItems(items2)
        transaction_page.clickSaveButton()
        self.assertEqual(self.baseUrl + '/app/transaction/list',self.driver.current_url)

    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()

