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

class GenerateVoucherSpec(unittest.TestCase):
    '''生成凭证测试'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        # createComoany = CreateCompay(self.driver)
        # createComoany.goToCompany(Environment2)
        EnterCompany(self.driver,Environment)

    def test1(self):
        '''记一笔收入-凭证测试'''
        
        # recordIncome = TransactionPage(self.driver,'income')
        # recordIncome.goToTransactionModule(BaseUrl)
        # recordIncome.goToTransactionPage('记收入')
        # recordIncomePublicData = ['1','现金','内部代表']
        # recordIncomeItemsData = ['1',['1','1'],'111','现金-内部代表-利息收入-利息收入 111']
        # recordIncome.recordTransaction(recordIncomePublicData,recordIncomeItemsData)
        # time.sleep(3)
        # recordIncome.goToVoucherPage(BaseUrl)
        # firstLines = ['2017年2月现金收款','100101—RMB','111.00']
        # firstRows = ['3','4','5']
        # for firstLine,firsrRow in zip(firstLines,firstRows):
        #     firstRowLocator = '//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table/tbody/tr[1]/td['+ firsrRow +']'
        #     self.assertEqual(firstLine,self.driver.find_element_by_xpath(firstRowLocator).text)
        # secondLines = ['现金-内部代表-利息收入-利息收入 111','560301—利息费用','-111.00']
        # secondRows = ['1','2','3']
        # for secondLine,secondRow in zip(secondLines,secondRows):
        #     secondRowLocator = '//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table/tbody/tr[2]/td['+ secondRow +']'
        #     self.assertEqual(secondLine,self.driver.find_element_by_xpath(secondRowLocator).text)

        recordIncome = TransactionPage(self.driver,'income')
        # recordIncome.goToTransactionModule(BaseUrl)
        # recordIncome.goToTransactionPage('记收入')
        # for recordIncomePublicData,recordIncomeItemsData in zip(RecordIncomePublicData,RecordIncomeItemsData):
        #     recordIncome.recordTransaction(recordIncomePublicData,recordIncomeItemsData)
        recordIncome.goToVoucherPage(BaseUrl)
        voucherSumList = self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table').find_elements_by_tag_name('tbody')
        print('voucherSumList:' + str(len(voucherSumList)))
        for tbody,incomeVoucherData in zip(range(0,len(voucherSumList)),IncomeVoucherData):
            trsVoucher = voucherSumList[tbody].find_elements_by_tag_name('tr')
            print('trsVoucher:' + str(len(trsVoucher)))
            for tr,incomeVoucherLine in zip(range(0,len(trsVoucher)),range(0,len(incomeVoucherData))):
                tdsVoucher = trsVoucher[tr].find_elements_by_tag_name('td')
                if 9 == len(tdsVoucher):
                    for td1,voucherCheck1 in zip(range(2,6),range(0,len(incomeVoucherLine))):
                        self.assertEqual(incomeVoucherLine[voucherCheck1],tdsVoucher[td1].text)
                elif 4 == len(tdsVoucher):
                    for  td2,voucherCheck2 in zip(range(0,4),range(0,len(incomeVoucherLine))):
                        self.assertEqual(incomeVoucherLine[voucherCheck2],tdsVoucher[td2])

                elif 5 == len(tdsVoucher):
                    for td3,voucherCheck3 in zip(range(2,4),range(0,len(incomeVoucherLine))):
                        self.assertEqual(incomeVoucherLine[voucherCheck3],tdsVoucher[td3])
            # for tr in range(0,len(trsVoucher)):
            #     tdsVoucher = trsVoucher[tr].find_elements_by_tag_name('td')
            #     print('tdsVoucher:' + str(len(tdsVoucher)))
            #     for td,voucherCheck in zip(range(0,len(tdsVoucher))[2:6],[0,1,2,3]):
            #         self.assertEqual(voucherCheck,tdsVoucher[td].text)
            
        

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