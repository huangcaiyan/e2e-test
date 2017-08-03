import time
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from util.set_date_util import SetDate

#固定资产模块
class FixedassetsPage(object):

    def __init__(self,driver,fixedassetsType):
        self.driver = driver
        self.fixedassetsType = fixedassetsType

    #进入固定资产列表页面
    def goToFixedassetsList(self,baseUrl):
        if 'fixed' == self.fixedassetsType:
            subUrl = '/app/fixed-assets/list'
        else:
            subUrl = '/app/fixed-assets/intangible-list'
        self.driver.get(baseUrl + subUrl)
        time.sleep(5)

    #进入记固定资产页面
    def goToRecordFixedassetsPage(self,baseUrl):
        self.driver.get(baseUrl + '/app/fixed-assets/detail/' + self.fixedassetsType )
        time.sleep(5)


    #设置固定资产-普票：记账日期，发票类别，部门性质，对方信息 publicPara [记账日期，发票类别，部门性质，对方信息]
    def setFixedassetsPublicComm(self,publicPara):
        dateButtounLocator = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[1]/div[1]/div/p-calendar/span/span'
        SetDate(self.driver,dateButtounLocator,publicPara[0])
        invoiceType = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[1]/div[2]/div/ng-select/div/div[2]/span'
        departmentLocator = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[1]/div[3]/div/ng-select/div/div[2]/span'
        otherInfoLocator = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[1]/div[4]/div/ng-select/div/div[2]/span'
        for locator,paraValue in zip([invoiceType,departmentLocator,otherInfoLocator],publicPara[1:]):
            self.driver.find_element_by_xpath(locator).click()
            time.sleep(1)
            self.driver.find_element_by_link_text(paraValue).click()

    #设置固定资产-专票：记账日期，发票类别，部门性质，对方信息，税率，进项税类别 publicPara [记账日期，发票类别，部门性质，对方信息，税率，进项税类别]
    def setFixedassetsPublicSpec(self,publicPara,invoiceNum):
        dateButtounLocator = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[1]/div[1]/div/p-calendar/span/span'
        SetDate(self.driver,dateButtounLocator,publicPara[0])
        invoiceType = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[1]/div[2]/div/ng-select/div/div[2]/span'
        departmentLocator = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[1]/div[3]/div/ng-select/div/div[2]/span'
        otherInfoLocator = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[1]/div[4]/div/ng-select/div/div[2]/span'
        rateLocator = '//*[@id="body"]/app-assets-tab/app-' + self.fixedassetsType + '/div/div[2]/div[2]/div[2]/div/ng-select/div/div[2]/span'
        locatorList = [invoiceType,departmentLocator,otherInfoLocator,rateLocator]
        for locator,paraValue in zip(locatorList,publicPara[1:]):
            self.driver.find_element_by_xpath(locator).click()
            time.sleep(1)
            self.driver.find_element_by_link_text(paraValue).click()

        self.driver.find_element_by_xpath('//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[2]/div[1]/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[2]/div[1]/div/input').send_keys(invoiceNum)

    #设置固定资产明细：名称，分类，数量，总额，备注 itemsPara [名称，分类，数量，总额，备注]
    def setFixedassetsItems(self,itemsPara):
        if 'fixed' == self.fixedassetsType:
            fixedNameLocator = '//*[@id="body"]/app-assets-tab/app-fixed/div/div[2]/div[3]/div/table/tbody/tr/td[1]/div/input'
        else:
            fixedNameLocator = '//*[@id="body"]/app-assets-tab/app-intangible/div/div[2]/div[3]/div/table/tbody/tr/td[1]/input'
        self.driver.find_element_by_xpath(fixedNameLocator).clear()
        self.driver.find_element_by_xpath(fixedNameLocator).send_keys(itemsPara[0])
        classifyLocator = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[3]/div/table/tbody/tr/td[2]/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(classifyLocator).click()
        time.sleep(2)
        self.driver.find_element_by_link_text(itemsPara[1]).click()
        amountLocator = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType  +'/div/div[2]/div[3]/div/table/tbody/tr/td[3]/input'
        sumLocator = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType + '/div/div[2]/div[3]/div/table/tbody/tr/td[4]/bp-input/input'
        remarkLocator = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[3]/div/table/tbody/tr/td[5]/input'
        for locator,paraValue in zip([amountLocator,sumLocator,remarkLocator],itemsPara[2:]):
            self.driver.find_element_by_xpath(locator).clear()
            self.driver.find_element_by_xpath(locator).send_keys(paraValue)

    #点击保存并新增按钮
    def clickSaveAndAdd(self):
        saveAndAddLocator = '//*[@id="body"]/app-assets-tab/app-'+ self.fixedassetsType +'/div/div[2]/div[8]/div/span/button[1]'
        self.driver.find_element_by_xpath(saveAndAddLocator).click()
        time.sleep(3)

    #记固定资产-普票
    def recordFixedassetsComm(self,fixedassetsPara):
        self.setFixedassetsPublicComm(fixedassetsPara[0])
        self.setFixedassetsItems(fixedassetsPara[1])
        self.clickSaveAndAdd()

    #记固定资产-专票
    def recordFixedassetsSpec(self,fixedassetsPara,invoiceNum):
        self.setFixedassetsPublicSpec(fixedassetsPara[0],invoiceNum)
        self.setFixedassetsItems(fixedassetsPara[1])
        self.clickSaveAndAdd()