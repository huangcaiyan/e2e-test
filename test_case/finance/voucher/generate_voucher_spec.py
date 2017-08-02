import unittest
import sys
import os
from selenium import webdriver
import time
from HTMLTestRunner import HTMLTestRunner
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from util.create_company_util import CreateCompay
from config import *
from transaction.transaction_page import TransactionPage
from test_data.generate_voucher_data import *
from util.enter_company_util import EnterCompany
from util.voucher_check_util import VoucherCheck

class GenerateVoucherSpec(unittest.TestCase):
    '''生成凭证测试'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        # createComoany = CreateCompay(self.driver)
        # createComoany.goToCompany(Environment2)
        EnterCompany(self.driver,Environment)

    def test1(self):
        '''记所有收入类别-凭证测试'''
        
        recordIncome = TransactionPage(self.driver,'income')
        recordIncome.goToTransactionModule(BaseUrl)
        recordIncome.goToTransactionPage('记收入')
        for recordIncomePublicData,recordIncomeItemsData in zip(RecordIncomePublicData,RecordIncomeItemsData):
            recordIncome.recordTransaction(recordIncomePublicData,recordIncomeItemsData)

        recordOutput = TransactionPage(self.driver,'outcome')
        recordOutput.goToTransactionModule(BaseUrl)
        recordOutput.goToTransactionPage('记支出')
        for recordOutcomePublicData,recordOutcomeItemsData in zip(RecordOutcomePublicData,RecordOutputItemsData):
            recordOutput.recordTransaction(recordOutcomePublicData,recordOutcomeItemsData)

        recordTransfer = TransactionPage(self.driver,'accounttransfers')
        recordTransfer.goToTransactionModule(BaseUrl)
        recordTransfer.goToTransactionPage('记账户互转')
        for recordTransferData in RecordTransferData:
            recordTransfer.recordTransfer(recordTransferData)

            
        # recordIncome.goToVoucherPage(BaseUrl)
        # vc = VoucherCheck(self.driver)
        # vc.voucherCheck(IncomeVoucherData)

    def test2(self):
        '''记所有支出类别-凭证测试'''

        recordOutput = TransactionPage(self.driver,'outcome')
        recordOutput.goToTransactionModule(BaseUrl)
        recordOutput.goToTransactionPage('记支出')
        for recordOutcomePublicData,recordOutcomeItemsData in zip(RecordOutcomePublicData,RecordOutputItemsData):
            recordOutput.recordTransaction(recordOutcomePublicData,recordOutcomeItemsData)
        recordOutput.goToVoucherPage(BaseUrl)
        vc = VoucherCheck(self.driver)
        vc.voucherCheck(OutcomeVoucherData)

    # def test3(self):
    #     '''记一笔账户互转-凭证测试'''

    #     recordTransfer = TransactionPage(self.driver,'accounttransfers')
    #     recordTransfer.goToTransactionModule(BaseUrl)
    #     recordTransfer.goToTransactionPage('记账户互转')
    #     recordTransfer.recordTransfer(RecordOutcomePublicData,RecordOutputItemsData)
    #     time.sleep(3)
    #     recordTransfer.goToVoucherPage(BaseUrl)
    #     self.assertEqual('100101—RMB',self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table/tbody[3]/tr[1]/td[4]').text)
    #     self.assertEqual('711.00',self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table/tbody[3]/tr[1]/td[5]').text)
    #     self.assertEqual('100201—银行',self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table/tbody[3]/tr[2]/td[2]').text)
    #     self.assertEqual('711.00',self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table/tbody[3]/tr[2]/td[4]').text)

    # def test4(self):
    #     '''记一笔收票-普票-凭证测试'''
    #     pass

    def tearDown(self):
        self.driver.quit()