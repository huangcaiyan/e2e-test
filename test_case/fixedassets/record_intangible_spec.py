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
import xlrd

class RecordIntangibleSpec(unittest.TestCase):
    ''' 记无形资产测试 '''

    def setUp(self):
        self.driver = webdriver.Chrome()
        EnterCompany(self.driver,Environment)
        fixedassets_page = FixedassetsPage(self.driver,'intangible')
        fixedassets_page.goToRecordFixedassetsPage(BaseUrl)

    def test1(self):
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

    def test2(self):
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

