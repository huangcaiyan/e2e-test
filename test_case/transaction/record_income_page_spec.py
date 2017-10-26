import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from selenium import webdriver
from time import sleep
from util.driver_util import Driver
from util.enter_company_util import EnterCompany
from .transaction_page import TransactionPage
from config import *

class RecordIncomePageSpec(unittest.TestCase):
    '''记收入页面测试'''

    @classmethod
    def setUpClass(self):
        self.driver = Driver().get_driver()
        enterCompany = EnterCompany(self.driver)
        enterCompany.goToCompany()
        self.transaction_page = TransactionPage(self.driver,'income')
        self.transaction_page.recordIncomeUrl(BaseUrl)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        
    def test1(self):
        '''不填写信息点-击保存并更新按钮'''
        self.transaction_page.clickSaveAndAddButton()
        alertInfo = self.driver.find_element_by_xpath('//*[@id="body"]/detail/income/div/div[1]/alert/div').text[-8:]
        self.assertEqual('请填写交易账户！',alertInfo)

    def test2(self):
        '''不填写信息-点击保存按钮'''
        self.transaction_page.clickSaveButton()
        alertInfo = self.driver.find_element_by_xpath('//*[@id="body"]/detail/income/div/div[1]/alert/div').text[-8:]
        self.assertEqual('请填写交易账户！',alertInfo)

    def test3(self):
        '''填写交易账户-点击保存按钮'''
        self.transaction_page.setAccount('现金')
        self.transaction_page.clickSaveButton()
        sleep(2)
        alertInfo = self.driver.find_element_by_xpath('//*[@id="body"]/detail/income/div/div[1]/alert/div').text[-7:]
        self.assertEqual('金额不能为0！',alertInfo)

    def test4(self):
        '''填写类别-点击保存按钮'''
        self.transaction_page.setCategory(['1','1'])
        self.transaction_page.clickSaveButton()
        alertInfo = self.driver.find_element_by_xpath('//*[@id="body"]/detail/income/div/div[1]/alert/div').text[-7:]
        self.assertEqual('金额不能为0！',alertInfo)

    def test5(self):
        '''填写金额为0-点击保存按钮'''
        self.transaction_page.setMoney('0')
        self.transaction_page.clickSaveButton()
        sleep(2)
        alertInfo = self.driver.find_element_by_xpath('//*[@id="body"]/detail/income/div/div[1]/alert/div').text[-7:]
        self.assertEqual('金额不能为0！',alertInfo)

    def test6(self):
        '''填写备注-点击保存按钮'''
        pass

    
