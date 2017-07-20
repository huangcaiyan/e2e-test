import unittest
import sys
import os
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../'))
from login.login_page import LoginPage
from .transaction_page import TransactionPage
import time


class RecordOutcomeSpec(unittest.TestCase):
    ''' 记支出测试 '''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.baseUrl = 'https://web-gyz-stage.guanplus.com'
        login_page = LoginPage(self.baseUrl, self.driver)
        login_page.login('18514509382', 'qq123456')
        transaction_page = TransactionPage(self.driver)
        transaction_page.goToCompany('羊呦呦有限公司')
        transaction_page.goToTransactionModule()
        transaction_page.goToTransactionPage('记支出')

    def test1(self):
        '''交易账户空校验'''

        self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[5]/div/span/button[2]').click()
        self.assertEquals('请填写交易账户！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[1]/alert/div').text[-8:])
        # print('aaaaa:' + self.driver.switch_to_alert().text)

    def test2(self):
        '''成功记一笔收支'''

        transaction_page = TransactionPage(self.driver)
        transaction = ['1','现金','内部代表']
        items = [['1','银行费用'],'119','羊啊']
        transaction_page.recordTransaction(transaction,items)
        self.assertEquals(self.baseUrl + '/app/transaction/list',self.driver.current_url)

    def tearDown(self):
        self.driver.quit()
        

