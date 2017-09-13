from selenium import webdriver
from time import sleep
# import sys
# import os
# sys.path.append('F:\\autoTest_workspace\\python_code\\e2e-test\\test_case\\login')
# from login_page import LoginPage

class ImportOutputInvoiceFile(object):
    '''导入开票'''

    def __init__(self,driver):
        self.driver = driver
        self.importInputId = 'fileUploadBtn'

    def goToImportOutputInvoicePage(self,baseUrl):
        self.driver.get(baseUrl + '/app/invoice/import-output-invoice')
        sleep(5)

    def importOutputInvoiceFile(self,file):
        alertLocator = '//*[@id="body"]/invoice/import-output-invoice/div[1]/div[1]/alert/div'
        self.driver.find_element_by_id(self.importInputId).send_keys(file)
        sleep(20)
        # try:
        #     if '导入的文件不符合当前模板' == self.driver.find_element_by_xpath(alertLocator).text:
        #         print('[error: 导入的文件不符合当前模板]')
        #     else:
        #         print('============================导入开票失败=========================================')
        # except Exception as e:
        #     pass

# def test():
#     driver = webdriver.Chrome()
#     driver.get('https://firms.guanplus.com')
#     login = LoginPage('https://firms.guanplus.com',driver)
#     login.login(['18514509382','qq123456'])
#     sleep(5)
#     driver.find_element_by_xpath('//*[@id="company-table"]/tbody/tr[46]/td[1]/div/a').click()
#     sleep(5)
#     driver.get('https://firms.guanplus.com/app/invoice/import-output-invoice')
#     sleep(4)
#     im = ImportOutputInvoice(driver)
#     im.importOutputInvoiceFile('E:\\work\\产品文档\\一般纳税人\\一般纳税人开票导入.xlsx')
#     driver.quit()
#     print('ssssss')

# test()

