import time
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from util.setDate_util import SetDate


class InvoicePage:
    itemsNumber = ''
    invoiceType = ''

    def setItemsNum(self,itemsNum):
        global itemsNumber 
        itemsNumber = itemsNum

    def __init__(self, driver):
        self.driver = driver
        self.date_button_xpath = '//*[@id="datePiker"]/span/span[2]'

    # 进入账套
    def goToCompany(self, companyName):
        self.driver.find_element_by_link_text(companyName).click()
        time.sleep(5)

    # 进入记发票页面
    def goToInvoice(self,baseUrl,invoiceType):
        self.driver.get(baseUrl + '/app/invoice/tab/new-' + invoiceType + '-invoice')
        time.sleep(5)

    #进入凭证列表页面
    def goToVoucherPage(self,baseUrl):
        self.driver.get(baseUrl + '/app/finance/voucher')
        time.sleep(5)

    # 设置收票类型               
    def setIncomeInvoiceType(self, incomeInvoiceType):
        global invoiceType 
        invoiceType = incomeInvoiceType
        income_invoice_type_xpath = '//*[@id="body"]/tab/fgff/div/div[2]/ul/div[1]/div/label[2]/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(income_invoice_type_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_link_text(incomeInvoiceType).click()
        time.sleep(3)

    # 设置对方信息
    def setOtherInfo(self, otherInfo):
        otherInfo_xpath = '//*[@id="body"]/tab/fgff/div/div[2]/ul/div[1]/div/label[3]/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(otherInfo_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_link_text(otherInfo).click()

    #设置发票号码
    def setInvoiceNum(self,invoiceNum):
        self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/div[1]/div/label[4]/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/div[1]/div/label[4]/div/input').send_keys(invoiceNum)

    #设置类别 
    def setCategory(self,category):
        self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[1]/ng-select/div/div[2]/span').click()
        time.sleep(5) 
        firstXpath = '//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[1]/ng-select/div/div[2]/ul/li[' + category[0] + ']/div'
        self.driver.find_element_by_xpath(firstXpath).click()
        if 1 == int(category[1]):
            secondXpath = '//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[1]/ng-select/div/div[2]/div/div[1]/div/button/div'
        else:
            secondXpath = '//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[1]/ng-select/div/div[2]/div/div['+ category[1] + ']/div[2]/button/div'
        self.driver.find_element_by_xpath(secondXpath).click()

    #设置部门
    def setDepartment(self,departmentName):
        self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[2]/ng-select/div/div[2]/span').click()
        self.driver.find_element_by_link_text(departmentName).click()

    #设置税率
    def setRate(self,rate):
        self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[3]/ng-select/div/div[2]/span').click()
        self.driver.find_element_by_link_text(rate).click()

    #设置进项税类别
    def setInputTax(self,taxCategory):
        self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[4]/ng-select/div/div[2]/span').click()
        self.driver.find_element_by_link_text(taxCategory).click()

    #设置价税合计金额
    def setMoney(self,money):
        if '普票' == invoiceType:
            self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[4]/bp-input/input').clear()
            self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[4]/bp-input/input').send_keys(money)
        else:
            self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[5]/bp-input/input').clear()
            self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[5]/bp-input/input').send_keys(money)

    #设置备注
    def setRemark(self,remark=None):
        if '普票' == invoiceType:
            self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[5]/input').clear()
            self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[5]/input').send_keys(remark)
        else:
            self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[6]/input').clear()
            self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/table/tbody/tr[1]/td[6]/input').send_keys(remark)

    #点击保存按钮
    def clickSaveButton(self):
        self.driver.find_element_by_xpath('//*[@id="body"]/tab/fgff/div/div[2]/ul/div[3]/div/span/button[2]').click()
        time.sleep(5)

    #普票-设置明细：类别，部门性质，税率，价税合计金额，备注 items 是一个list [类别，部门性质，税率，价税合计金额，备注]
    def setCommonInvoiceItems(self,commonItems):
        self.setCategory(commonItems[0])
        self.setDepartment(commonItems[1])
        self.setRate(commonItems[2])
        self.setMoney(commonItems[3])
        self.setRemark(commonItems[4])

    #普票-设置收票的记账日期，发票类型，对方信息 publicInvoice 是一个list,[记账日期，发票类型，对方信息]
    def setCommonPublicInvoice(self,commonPublicInvoice):
        SetDate(self.driver,self.date_button_xpath,commonPublicInvoice[0])
        self.setIncomeInvoiceType(commonPublicInvoice[1])
        self.setOtherInfo(commonPublicInvoice[2])

    # 记收票-普票
    def recordCommonIncomeInvoice(self,commonPublicInvoice,commonItems):
        self.setCommonPublicInvoice(commonPublicInvoice)
        self.setCommonInvoiceItems(commonItems)
        self.clickSaveButton()

    #专票-设置明细：类别，部门性质，税率，进项税类别，价税合计金额，备注 items 是一个list [类别，部门性质，税率，进项税类别，价税合计金额，备注]
    def setSpecialInvoiceItems(self,specialItems):
        self.setCategory(specialItems[0])
        self.setDepartment(specialItems[1])
        self.setRate(specialItems[2])
        self.setInputTax(specialItems[3])
        self.setMoney(specialItems[4])
        self.setRemark(specialItems[5])

    #专票-设置收票的记账日期，发票类型，对方信息，发票号码 publicInvoice 是一个list,[记账日期，发票类型，对方信息，发票号码]
    def setSpecialPublicInvoice(self,publicInvoice,invoiceNum):
        SetDate(self.driver,self.date_button_xpath,publicInvoice[0])
        self.setIncomeInvoiceType(publicInvoice[1])
        self.setOtherInfo(publicInvoice[2])
        self.setInvoiceNum(invoiceNum)

    # 记收票-专票
    def recordSpecialIncomeInvoice(self,publicInvoice,invoiceNum,specialItems):
        self.setSpecialPublicInvoice(publicInvoice,invoiceNum)
        self.setSpecialInvoiceItems(specialItems)
        self.clickSaveButton()