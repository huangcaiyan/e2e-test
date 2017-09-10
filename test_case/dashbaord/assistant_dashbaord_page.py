from selenium import webdriver
from time import sleep
import logging

class AssistantDashbaordPage(object):

    def __init__(self,driver):
        self.driver = driver

    #进入助理首页
    def goAssistanDashbaordPage(self,url):
        self.driver.get(url + '/app/home-page/assist')
        sleep(2)

    #点击导入开票按钮
    def clickImportOutputInvoiceButton(self):
        try:
            className = 'cub '
            importButtonLocator = self.driver.find_element_by_class_name(className).find_element_by_tag_name('button')
            importButtonLocator.click()
            sleep(4)
        except Exception as e:
            print('[ERROR:助理首页导入开票按钮]')
            logging.exception(e)
    
    #点击选择账户导入按钮
    def clickChooseAccountImport(self):
        chooseAccountImportButtonLocator = '//*[@id="body"]/app-assist-home-page/div/div/div[3]/div[3]/div[3]/div/div/button[1]'
        self.driver.find_element_by_xpath(chooseAccountImportButtonLocator).click()
        sleep(2)

    #点击导入员工按钮
    def clickImportStaffButton(self):
        importStaffButtonLocator = '//*[@id="body"]/app-assist-home-page/div/div/div[3]/div[5]/div[3]/button'
        self.driver.find_element_by_xpath(importStaffButtonLocator).click()
        sleep(1)