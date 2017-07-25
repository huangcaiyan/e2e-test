import unittest
import sys
import os
from selenium import webdriver
import time
from HTMLTestRunner import HTMLTestRunner
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from test_case.login.login_page import LoginPage
from transaction_page import TransactionPage
from test_data.record_outcome_data import *


#前置条件：新账套
class TransactionVoucherSpec(unittest.TestCase):
    ''' 记支出测试 '''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.baseUrl = 'http://guanplus-app-accountingfirm-web-test.cn-north-1.eb.amazonaws.com.cn'
        login_page = LoginPage(self.baseUrl, self.driver)
        login_page.login('18514509382', 'qq123456')
        transaction_page = TransactionPage(self.driver,'outcome')
        transaction_page.goToCompany('2206一般纳税人')
        transaction_page.goToTransactionModule(self.baseUrl)
        transaction_page.goToTransactionPage('记支出')

    def test1(self):
        '''记支出-生成凭证测试'''

        n = 0
        m = 0
        transaction = ['1','现金','内部代表']
        transaction_page = TransactionPage(self.driver,'outcome')
        for outcome,vocherFirst in zip(recordOutcomeData,outcomeVoucherFirst):
            n = n + 1
            m = m + 1
            transaction_page.recordTransaction(transaction,outcome)
            transaction_page.goToVoucherPage(self.baseUrl)
            if m >= 11:
                self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[2]/div/pagination/ul/li[4]/a').click()
                time.sleep(3)
            voucherFirstXpath = '//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table/tbody[' + str(n) + ']/tr[1]/td[4]'
            self.assertEqual(vocherFirst[0],self.driver.find_element_by_xpath(voucherFirstXpath).text)
            transaction_page.goToTransactionModule(self.baseUrl)
            transaction_page.goToTransactionPage('记支出')
            if 10 == n:
                n = 0
            
        transaction_page.goToTransactionModule(self.baseUrl)
        self.assertEqual('支出合计： 4,359.00',self.driver.find_element_by_xpath('//*[@id="body"]/list/div/div[5]/div[2]/span').text)

    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()

