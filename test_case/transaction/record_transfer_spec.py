import unittest
import sys
import os
from selenium import webdriver
import time
from collections import Iterator
from HTMLTestRunner import HTMLTestRunner
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from .transaction_page import TransactionPage
from test_data.record_transfer_data import *
from util.enter_company_util import EnterCompany
from config import *

#前提条件：有一个【招商银行】账户
class RecordTransterSpec(unittest.TestCase):
    ''' 记账户互转测试 '''

    def setUp(self):
        self.driver = webdriver.Chrome()
        EnterCompany(self.driver,Environment)
        self.transaction_page = TransactionPage(self.driver,'accounttransfers')
        self.transaction_page.goToTransactionModule(BaseUrl)
        self.transaction_page.goToTransactionPage('记账户互转')

    def test1(self):
        '''全空校验'''

        self.transaction_page.transferClickSaveButton()
        self.assertEqual('账户不能为空',self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[1]/alert/div').text[-6:])

    def test2(self):
        '''记账日期空校验'''

        self.transaction_page.setFundFlow('现金','招商银行')
        self.transaction_page.setTransferMoney('111')
        self.transaction_page.deleteDate()
        self.transaction_page.transferClickSaveButton()
        self.assertEqual('请填写记账日期！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[1]/alert/div').text[-8:])

    def test3(self):
        '''转出账户-空校验'''

        self.transaction_page.setTransferIn('招商银行')
        self.transaction_page.setTransferMoney('123')
        self.transaction_page.transferClickSaveButton()
        self.assertEqual('账户不能为空',self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[1]/alert/div').text[-6:])
        
    def test4(self):
        '''转入账户-空校验'''

        self.transaction_page.setTransferOut('招商银行')
        self.transaction_page.setTransferMoney('123')
        self.transaction_page.transferClickSaveButton()
        self.assertEqual('账户不能为空',self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[1]/alert/div').text[-6:])

    def test5(self):
        '''资金流向账户不能相同测试'''
        self.transaction_page.setFundFlow('现金','现金')
        self.transaction_page.setTransferMoney('123')
        self.transaction_page.transferClickSaveButton()
        self.assertEqual('账户不能相同',self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[1]/alert/div').text[-6:])

    def test6(self):
        '''金额-空校验'''

        self.transaction_page.setFundFlow('招商银行','现金')
        self.transaction_page.transferClickSaveButton()
        self.assertEqual('金额不能为0！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[1]/alert/div').text[-7:])

    def test7(self):
        '''成功记一笔账户互转测试'''

        transferPara = ['1','现金','招商银行','1','现金-招商银行1']
        self.transaction_page.recordTransfer(transferPara)
        self.assertEqual('保存成功',self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[1]/alert/div').text[-4:])

    # def test8(self):
    #     '''成功记所有类别支出测试'''
    
    #     transaction = ['1','现金','内部代表']
    #     transaction_page = TransactionPage(self.driver,'outcome')
    #     for outcome in RecordOutcomeData:
    #         transaction_page.recordTransaction(transaction,outcome)
    #     transaction_page.goToTransactionModule(BaseUrl)
    #     self.assertEqual(BaseUrl + '/app/transaction/list',self.driver.current_url)

    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()

