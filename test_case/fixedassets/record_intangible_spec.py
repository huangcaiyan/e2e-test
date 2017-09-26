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

class RecordIntangibleSpec(unittest.TestCase):
    ''' 记无形资产测试 '''

    def setUp(self):
        self.driver = Driver().get_driver()
        enterCompany = EnterCompany(self.driver)
        enterCompany.goToCompany()
        fixedassets_page = FixedassetsPage(self.driver,'intangible')
        fixedassets_page.goToRecordFixedassetsPage(BaseUrl)

    def test1(self):
        '''成功记一笔无形资产-普票'''

        fixedassets_page = FixedassetsPage(self.driver,'intangible')
        fixedParaPublic = ['1','普票','管理部门','(个)内部代表']
        fixedParaItems = ['管有账','软件','1','888','无形-普票-管理部门-内部代表-软件']
        fixedassets_page.recordFixedassetsComm([fixedParaPublic,fixedParaItems])
        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/intangible-list',self.driver.current_url)

    def test2(self):
        '''成功记一笔无形资产-专票'''
        
        fixedassets_page = FixedassetsPage(self.driver,'intangible')
        fixedParaPublic = ['1','专票','管理部门','(个)内部代表','17%','无形资产']
        fixedParaItems = ['智商','知识产权(IP)','1','88','无形-专票-管理部门-内部代表-知识产权(IP)']
        fixedassets_page.recordFixedassetsSpec([fixedParaPublic,fixedParaItems],self.invoiceNum())
        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/intangible-list',self.driver.current_url)


    def test3(self):
        '''成功记录多笔无形资产-普票记录测试'''

        fixedassets_page = FixedassetsPage(self.driver,'intangible')
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/' + '../../test_data/' + '固定资产.xlsx')
        sh = wb.sheet_by_name(u'记无形资产普票测试数据')
        for i in range(1,sh.nrows):
            sourceRowList = sh.row_values(i)
            targetPara = [sourceRowList[:4],sourceRowList[4:]]
            fixedassets_page.recordFixedassetsComm(targetPara)

        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/intangible-list',self.driver.current_url)

    def test4(self):
        '''成功记录多笔无形资产-专票记录测试'''

        fixedassets_page = FixedassetsPage(self.driver,'intangible')
        invoiceNumList = []
        for i in range(0,10):
            invoiceNumList.append(self.invoiceNum())

        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/' + '../../test_data/' + '固定资产.xlsx')
        sh = wb.sheet_by_name(u'记无形资产专票测试数据')
        for i,invoiceNum in zip(range(1,sh.nrows),invoiceNumList):
            sourceRowList = sh.row_values(i)
            targetPara = [sourceRowList[:5],sourceRowList[5:]]
            fixedassets_page.recordFixedassetsSpec(targetPara,invoiceNum)

        fixedassets_page.goToFixedassetsList(BaseUrl)
        self.assertEqual(BaseUrl + '/app/fixed-assets/intangible-list',self.driver.current_url)

    #生成8位随机整数
    def invoiceNum(self):
        invoiceNum = ''
        for i in range(0,8) :
            invoiceNum = invoiceNum + str(random.randint(0,9))
        return invoiceNum

    def tearDown(self):
        self.driver.quit()        

if __name__ == '__main__':
    unittest.main()

