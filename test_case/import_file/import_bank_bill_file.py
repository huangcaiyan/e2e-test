from selenium import webdriver
from time import sleep
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# sys.path.append('F:\\autoTest_workspace\\python_code\\e2e-test\\test_case\\login')
# from login_page import LoginPage


class ImportBankBillFile(object):
    def __init__(self,driver):
        self.driver = driver

    #进入账户列表页面
    def goToAccountListPage(self,url):
        self.driver.get(url + '/app/account')
        sleep(3)
 

    #进入银行账户的导入页面
    def goToBankAccountImportPage(self,url,accountName):
        self.goToAccountListPage(url)
        hrefAttri = self.driver.find_element_by_link_text(accountName).get_attribute('href')
        accountId = hrefAttri.split(';')[1]
        self.driver.get(url + '/app/reconcile/import;' + accountId + ';where=account')
        sleep(3)

    #导入文件
    def importBankBill(self,file):
        chooseFileButtonLocator = '//*[@id="uploadBtn"]'
        self.driver.find_element_by_xpath(chooseFileButtonLocator).send_keys(file)
        sleep(5)
        uploadButtonLocator = '//*[@id="body"]/setting/reconcile-import/div[1]/div[8]/upload/button'
        uploadBttonElement = WebDriverWait(self.driver,5,0.2).until(EC.presence_of_element_located((By.XPATH,uploadButtonLocator)))
        uploadBttonElement.click()
        sleep(8)

    #匹配对账单表头
    def mappingBankBillHeader(self):
        dateLocator = '//*[@id="body"]/setting/reconcile-match/div/form/div/div/tbody/tr[2]/td[3]/ng-select/div/div[2]/span'
        incomeLocator = '//*[@id="body"]/setting/reconcile-match/div/form/div/div/tbody/tr[6]/td[3]/ng-select/div/div[2]/span'
        outcomeLocator = '//*[@id="body"]/setting/reconcile-match/div/form/div/div/tbody/tr[7]/td[3]/ng-select/div/div[2]/span'
        saveButtonLocator = '//*[@id="body"]/setting/reconcile-match/div/form/div/div/div[1]/div[1]/button'
        locators = [dateLocator,incomeLocator,outcomeLocator]
        mappingValues = ['日期','收入','支出']
        for locator,value in zip(locators,mappingValues):
            self.driver.find_element_by_xpath(locator).click()
            sleep(1)
            self.driver.find_element_by_link_text(value).click()
            sleep(1)

        self.driver.find_element_by_xpath(saveButtonLocator).click()
        sleep(8)

    #同步为管有方记录
    def synchronizeBankBill(self):
        tableLocator = '//*[@id="body"]/setting/gpw-multi-sync/div[2]/div/div'
        saveButtonLocator = '//*[@id="body"]/setting/gpw-multi-sync/div[2]/div/div/div/button[1]'
        tableElementsList = self.driver.find_element_by_xpath(tableLocator).find_elements_by_tag_name('table')
        for tableElement in tableElementsList:
            tbodyTrsList = tableElement.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
            tdList = tbodyTrsList[1].find_elements_by_tag_name('td')
            tdList[3].click()
            sleep(1)
            self.setCategory(tdList[3])
        self.driver.find_element_by_xpath(saveButtonLocator).click()
        sleep(5)

    #设置类别 临时借入，临时借出
    def setCategory(self,locator):
        firstCategoryElementsList = locator.find_element_by_tag_name('ul').find_elements_by_tag_name('li')
        #设置一级类别
        firstCategoryElementsList[1].click()
        sleep(2)
        #设置二级类别
        self.driver.find_element_by_class_name('children-float').find_elements_by_tag_name('div')[0].click()
        sleep(1)

    #导入并匹配银行对账单
    def importMapping(self,file):
        self.importBankBill(file)
        self.mappingBankBillHeader()
        self.synchronizeBankBill()

# driver = webdriver.Chrome()
# url = 'https://firms.guanplus.com'
# login = LoginPage('https://firms.guanplus.com',driver)
# login.login(['18514509382','qq123456'])
# sleep(5)
# driver.find_element_by_xpath('//*[@id="company-table"]/tbody/tr[46]/td[1]/div/a').click()
# sleep(5)
# im = ImportBankBillFile(driver)
# im.goToBankAccountImportPage(url,'招商银行（账户类型：银行账户）')
# im.importBankBill('F:\\autoTest_workspace\\python_code\\e2e-test\\test_data\\导入招商银行对账单.xlsx')
# im.mappingBankBillHeader()
# im.synchronizeBankBill()
# driver.quit()