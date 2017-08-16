from selenium import webdriver
from time import sleep

class AssistantDashbaordPage(object):

    def __init__(self,driver):
        self.driver = driver

    #进入会计首页
    def goAssistanDashbaordPage(self,url):
        self.driver.get(url + '/app/home-page/assist')
        sleep(2)

    #点击导入开票按钮
    def clickImportOutputInvoiceButton(self):
        importButtonLocator = '//*[@id="body"]/app-assist-home-page/div/div/div[3]/div[1]/div[3]/span/a'
        self.driver.find_element_by_xpath(importButtonLocator).click()
        sleep(3)
    
    #点击选择账户导入按钮
    def clickChooseAccountImport(self):
        chooseAccountImportButtonLocator = '//*[@id="body"]/app-assist-home-page/div/div/div[3]/div[3]/div[3]/div/button[1]'
        self.driver.find_element_by_xpath(chooseAccountImportButtonLocator).click()
        sleep(2)

    #点击导入员工按钮
    def clickImportStaffButton(self):
        importStaffButtonLocator = '//*[@id="body"]/app-assist-home-page/div/div/div[3]/div[5]/div[3]'
        self.driver.find_element_by_xpath(importStaffButtonLocator).click()
        sleep(1)