import unittest
import sys
import os
from selenium import webdriver
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../'))
# from util.jsonToPython_util import JsonToPython
from login.login_page import LoginPage
from transaction_page import TransactionPage
import time


class RecordOutcomeSpec(unittest.TestCase):
    def setUp(self):
        # self.jsonData = JsonToPython(os.path.abspath(os.path.dirname(__file__) + '/' + '../..')+ '/test_data/record_transaction_data.json', 'r')
        # self.pythonData = self.jsonData.readJson()
        self.driver = webdriver.Chrome()
        self.baseUrl = 'https://web-gyz-stage.guanplus.com'
        login_page = LoginPage(self.baseUrl, self.driver)
        login_page.login('18514509382', 'qq123456')
        transaction_page = TransactionPage(self.driver)
        transaction_page.goToCompany('羊呦呦有限公司')
        transaction_page.goToTransactionModule()
        transaction_page.goToTransactionPage('记支出')

    #空校验
    def test1(self):
        self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[5]/div/span/button[2]').click()
        self.assertEquals('请填写交易账户！',self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[1]/alert/div').text[-8:])

    #成功记一笔收支
    def test2(self):
        transaction_page = TransactionPage(self.driver)
        transaction = ['1','现金','内部代表']
        items = [['1','银行费用'],'119','羊啊']
        transaction_page.recordTransaction(transaction,items)
        self.assertEquals(baseUrl + '/app/transaction/list',self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
