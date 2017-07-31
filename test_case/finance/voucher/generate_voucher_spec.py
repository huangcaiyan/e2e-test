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
        '''记一笔收入-凭证测试'''
        
        recordIncome = TransactionPage(self.driver,'income')
        # recordIncome.goToTransactionModule(BaseUrl)
        # recordIncome.goToTransactionPage('记收入')
        # recordIncomePublicData = ['1','现金','内部代表']
        # recordIncomeItemsData = ['1',['1','1'],'111','现金-内部代表-利息收入-利息收入 111']
        # recordIncome.recordTransaction(recordIncomePublicData,recordIncomeItemsData)
        # time.sleep(3)
        # recordIncome.goToVoucherPage(BaseUrl)
        recordIncome.goToVoucherPage(BaseUrl)

        #运行通过的                                           
        # tbodyLists = self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table').find_elements_by_tag_name('tbody')
        # for tbody,voucherData in zip(tbodyLists,IncomeVoucherData):
        #     trLists = tbody.find_elements_by_tag_name('tr')
        #     for tr,lineVoucherData in zip(trLists,voucherData):
        #        tdLists = tr.find_elements_by_tag_name('td') 
        #        if 9 == len(tdLists):  
        #             for td,voucherFieldData in zip(tdLists[2:6],lineVoucherData):
        #                 self.assertEqual(voucherFieldData,td.text)
        #        if 4 == len(tdLists):
        #             for td,voucherFieldData in zip(tdLists,lineVoucherData):
        #                 self.assertEqual(voucherFieldData,td.text)
        #        if 5 == len(tdLists):
        #             for td,voucherFieldData in zip(tdLists[2:4],lineVoucherData):
        #                 self.assertEqual(voucherFieldData,td.text)
        vc = VoucherCheck(self.driver)
        vc.voucherCheck(IncomeVoucherData)

    def test2(self):
        '''记一笔支出-凭证测试'''

        recordOutput = TransactionPage(self.driver,'output')
        recordOutput.goToTransactionModule(BaseUrl)
        recordOutput.goToTransactionPage('记支出')
        recordOutput.recordTransaction(RecordOutcomePublicData,RecordOutputItemsData)
        time.sleep(3)
        recordOutput.goToVoucherPage(BaseUrl)
        self.assertEqual('560302—手续费用',self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table/tbody[2]/tr[1]/td[4]').text)
        self.assertEqual('211.00',self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table/tbody[2]/tr[1]/td[5]').text)
        self.assertEqual('100101—RMB',self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table/tbody[2]/tr[2]/td[2]').text)
        self.assertEqual('211.00',self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table/tbody[2]/tr[2]/td[4]').text)

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