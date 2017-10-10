import unittest
import sys
import os
from selenium import webdriver
import time
import random
from HTMLTestRunner import HTMLTestRunner
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from .fixedassets_page import FixedassetsPage
from util.enter_company_util import EnterCompany
from config import *
from util.category_map_util import CategoryMap
from util.driver_util import Driver
import xlrd
import threading

class RecordFixedSpec(unittest.TestCase):
    ''' 记固定资产测试 '''

    def setUp(self):
        self.driver = Driver().get_driver()
        enterCompany = EnterCompany(self.driver)
        enterCompany.goToCompany()
        fixedassets_page = FixedassetsPage(self.driver,'fixed')
        fixedassets_page.goToRecordFixedassetsPage(BaseUrl)
    
    def tearDown(self):
        self.driver.quit()
    # @classmethod
    # def setUpClass(self):
    #     # self.driver = Driver
    #     self.driver = webdriver.Chrome()
    #     EnterCompany(self.driver,Environment)
    #     fixedassets_page = FixedassetsPage(self.driver,'fixed')
    #     fixedassets_page.goToRecordFixedassetsPage(BaseUrl)

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()
    def test1(self):
        '''成功记一笔固定资产-普票'''

        fixedassets_page = FixedassetsPage(self.driver,'fixed')
        fixedParaPublic = ['1','普票','管理部门','(个)内部代表']
        fixedParaItems = ['iphoneX','电子设备','1','6888','固定-普票-管理部门-内部代表-电子设备']
        fixedassets_page.recordFixedassetsComm([fixedParaPublic,fixedParaItems])
        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/list',self.driver.current_url)

    def test2(self):
        '''成功记一笔固定资产-专票'''
        
        fixedassets_page = FixedassetsPage(self.driver,'fixed')
        fixedParaPublic = ['1','专票','管理部门','(个)内部代表','17%','固定资产']
        fixedParaItems = ['iphone8','电子设备','1','6800','固定-普票-管理部门-内部代表-电子设备']
        fixedassets_page.recordFixedassetsSpec([fixedParaPublic,fixedParaItems],self.invoiceNum())
        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/list',self.driver.current_url)


    def test3(self):
        '''成功记录多笔固定资产-普票记录测试'''

        fixedassets_page = FixedassetsPage(self.driver,'fixed')
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/' + '../../test_data/' + '固定资产.xlsx')
        sh = wb.sheet_by_name(u'记固定资产普票测试数据')
        for i in range(1,sh.nrows):
            sourceRowList = sh.row_values(i)
            targetPara = [sourceRowList[:4],sourceRowList[4:]]
            fixedassets_page.recordFixedassetsComm(targetPara)

        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/list',self.driver.current_url)

    def test4(self):
        '''成功记录多笔固定资产-专票记录测试'''
        
        fixedassets_page = FixedassetsPage(self.driver,'fixed')
        fixedassets_page.goToRecordFixedassetsPage(BaseUrl)
        invoiceNumList = []
        for i in range(0,10):
            invoiceNumList.append(self.invoiceNum())

        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/' + '../../test_data/' + '固定资产.xlsx')
        sh = wb.sheet_by_name(u'记固定资产专票测试数据')
        for i,invoiceNum in zip(range(1,sh.nrows),invoiceNumList):
            sourceRowList = sh.row_values(i)
            targetPara = [sourceRowList[:5],sourceRowList[5:]]
            fixedassets_page.recordFixedassetsSpec(targetPara,invoiceNum)

        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/list',self.driver.current_url)

    #生成8位随机整数
    def invoiceNum(self):
        invoiceNum = ''
        for i in range(0,8) :
            invoiceNum = invoiceNum + str(random.randint(0,9))
        return invoiceNum



if __name__ == '__main__':
    unittest.main()

