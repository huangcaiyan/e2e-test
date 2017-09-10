import time
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from util.set_date_util import SetDate


class InvoicePage(object):
    itemsNumber = ''
    invoiceClassfiy = ''

    def setItemsNum(self,itemsNum):
        global itemsNumber 
        itemsNumber = itemsNum

    def __init__(self, driver,invoiceType):
        self.driver = driver
        self.invoiceType = invoiceType

    # 进入记发票页面
    def goToInvoice(self,baseUrl):
        self.driver.get(baseUrl + '/app/invoice/tab/new-' + self.invoiceType + '-invoice')
        time.sleep(5)

    #进入发票列表页面
    def goToInvoiceList(self,baseUrl):
        self.driver.get(baseUrl + '/app/invoice/' + self.invoiceType + '-invoice')
        time.sleep(5)

    # 设置发票类型               
    def setInvoiceType(self, invoiceClass):
        global invoiceClassfiy
        invoiceClassfiy = invoiceClass
        invoice_type_xpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/div[1]/div/label[2]/ng-select/div/div[2]/span/span'
        self.driver.find_element_by_xpath(invoice_type_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_link_text(invoiceClass).click()
        time.sleep(3)

    # 设置对方信息
    def setOtherInfo(self, otherInfo):
        if 'input' == self.invoiceType:
            otherInfo_xpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/div[1]/div/label[3]/ng-select/div/div[2]/span'
        elif 'output' == self.invoiceType:
            otherInfo_xpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/div[1]/div/label[4]/ng-select/div/div[2]/span'
        else:
            print('========================================发票类型【invoiceType】错误============================================')
        self.driver.find_element_by_xpath(otherInfo_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_link_text(otherInfo).click()
        time.sleep(2)

    #设置发票状态
    def setInvoiceStatus(self,invoiceStatus):
        invoiceStatusXpath = '//*[@id="body"]/tab/new-output-invoice/div/div[2]/ul/div[1]/div/label[3]/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(invoiceStatusXpath).click()
        time.sleep(2)
        self.driver.find_element_by_link_text(invoiceStatus).click()
        time.sleep(2)
        
    #设置发票号码
    def setInvoiceNum(self,invoiceNum):
        if 'input' == self.invoiceType:
            invoiceNumXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/div[1]/div/label[4]/div/input'
        elif 'output' == self.invoiceType:
            invoiceNumXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/div[1]/div/label[5]/div/input'
        self.driver.find_element_by_xpath(invoiceNumXpath).clear()
        self.driver.find_element_by_xpath(invoiceNumXpath).send_keys(invoiceNum)

    #设置类别 
    def setCategory(self,category):
        categoryButtonXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/table/tbody/tr[1]/td[1]/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(categoryButtonXpath).click()
        time.sleep(5) 
        firstXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/table/tbody/tr[1]/td[1]/ng-select/div/div[2]/ul/li[' + category[0] + ']/div'
        self.driver.find_element_by_xpath(firstXpath).click()
        if 1 == int(category[1]):
            secondXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/table/tbody/tr[1]/td[1]/ng-select/div/div[2]/div/div[1]/div/button/div'
        else:
            secondXpath = '//*[@id="body"]/tab/new-' + self.invoiceType + '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[1]/ng-select/div/div[2]/div/div['+ category[1] + ']/div[2]/button/div'
        self.driver.find_element_by_xpath(secondXpath).click()

    #设置部门性质
    def setDepartment(self,departmentName):
        departmentXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/table/tbody/tr[1]/td[2]/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(departmentXpath).click()
        self.driver.find_element_by_link_text(departmentName).click()

    #设置税率
    def setRate(self,rate):
        rateXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/table/tbody/tr[1]/td[3]/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(rateXpath).click()
        self.driver.find_element_by_link_text(rate).click()

    #设置进项税类别
    def setInputTax(self,taxCategory):
        self.driver.find_element_by_xpath('//*[@id="body"]/tab/new-input-invoice/div/div[2]/ul/table/tbody/tr[1]/td[4]/ng-select/div/div[2]/span').click()
        self.driver.find_element_by_link_text(taxCategory).click()

    #设置价税合计金额
    def setMoney(self,money):
        
        if 'input' == self.invoiceType:
            if '普票' == invoiceClassfiy:
                 moneyXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/table/tbody/tr[1]/td[4]/bp-input/input'
            elif '专票' == invoiceClassfiy:
                 moneyXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/table/tbody/tr[1]/td[5]/bp-input/input'
            else:
                print('====================================发票类别【invoiceClassfiy】设置错误==============================================')
        elif 'output' == self.invoiceType:
            moneyXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/table/tbody/tr[1]/td[4]/bp-input/input'
        else:
            print('=============================================发票类别【invoiceType】设置错误============================================================')
        # if '普票' == invoiceClassfiy:
        #          moneyXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/table/tbody/tr[1]/td[4]/bp-input/input'
        # elif '专票' == invoiceClassfiy:
        #     moneyXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/table/tbody/tr[1]/td[5]/bp-input/input'
        # else:
        #     print('====================================发票类别【invoiceClassfiy】设置错误======================================================')
        self.driver.find_element_by_xpath(moneyXpath).clear()
        self.driver.find_element_by_xpath(moneyXpath).send_keys(money)

    #设置备注
    def setRemark(self,remark=None):
        if 'input' == self.invoiceType:
            if '普票' == invoiceClassfiy:
                remarkElement = self.driver.find_element_by_class_name("content-body ").find_element_by_tag_name('table').find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[4].find_element_by_tag_name('input')
            elif '专票' == invoiceClassfiy:
                remarkElement = self.driver.find_element_by_class_name("content-body ").find_element_by_tag_name('table').find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[5].find_element_by_tag_name('input')
            else:
                print('====================================发票类别【invoiceClassfiy】设置错误==============================================')
        elif 'output' == self.invoiceType:
            remarkElement = self.driver.find_element_by_class_name("content-body ").find_element_by_tag_name('table').find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td')[4].find_element_by_tag_name('input')
        else:
            print('=============================================发票类别【invoiceType】设置错误============================================================')
        # self.driver.find_element_by_xpath(remarkElement).clear()
        # self.driver.find_element_by_xpath(remarkElement).send_keys(remark)
        remarkElement.clear()
        remarkElement.send_keys(remark)
                                            
    #点击保存按钮                             
    def clickSaveButton(self): 
        saveButtonXpath = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/div[3]/div/span/button[2]'
        self.driver.find_element_by_xpath(saveButtonXpath).click()
        time.sleep(5)

    #点击保存并新增按钮
    def clickSaveAndAdd(self):
        saveAndAdd = '//*[@id="body"]/tab/new-'+ self.invoiceType +'-invoice/div/div[2]/ul/div[3]/div/span/button[1]'
        self.driver.find_element_by_xpath(saveAndAdd).click()
        time.sleep(3)

    #普票-设置明细：类别，部门性质，税率，价税合计金额，备注 items 是一个list [类别，部门性质，税率，价税合计金额，备注]
    def setCommonInvoiceItems(self,commonItems):
        self.setCategory(commonItems[0])
        self.setDepartment(commonItems[1])
        self.setRate(commonItems[2])
        self.setMoney(commonItems[3])
        self.setRemark(commonItems[4])

    #普票-设置收票的记账日期，发票类型，对方信息 publicInvoice 是一个list,[记账日期，发票类型，对方信息]
    def setCommonPublicInvoice(self,commonPublicInvoice):
        # date_button_xpath = '//*[@id="datePiker"]/span/span[2]'
        # SetDate(self.driver,date_button_xpath,commonPublicInvoice[0])
        dateButtonLocator = self.driver.find_elements_by_class_name("col-md-3")[0].find_element_by_tag_name('p-calendar')
        dateButtonLocator.click()
        time.sleep(2)
        self.driver.find_element_by_link_text(commonPublicInvoice[0]).click()
        time.sleep(2)
        self.setInvoiceType(commonPublicInvoice[1])
        self.setOtherInfo(commonPublicInvoice[2])

    # 记收票-普票 通过点击保存并新增按钮
    def recordCommonIncomeInvoice(self,commonPublicInvoice,commonItems):
        self.setCommonPublicInvoice(commonPublicInvoice)
        self.setCommonInvoiceItems(commonItems)
        self.clickSaveAndAdd()

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
        # date_button_xpath = '//*[@id="datePiker"]/span/span[2]'
        # SetDate(self.driver,date_button_xpath,publicInvoice[0])
        dateButtonLocator = self.driver.find_elements_by_class_name("col-md-3")[0].find_element_by_tag_name('p-calendar')
        dateButtonLocator.click()
        time.sleep(2)
        self.driver.find_element_by_link_text(publicInvoice[0]).click()
        time.sleep(2)
        self.setInvoiceType(publicInvoice[1])
        self.setOtherInfo(publicInvoice[2])
        self.setInvoiceNum(invoiceNum)

    # 记收票-专票 通过点击保存并新增按钮
    def recordSpecialIncomeInvoice(self,publicInvoice,invoiceNum,specialItems):
        self.setSpecialPublicInvoice(publicInvoice,invoiceNum)
        self.setSpecialInvoiceItems(specialItems)
        self.clickSaveAndAdd()

    #设置开票-记账日期，发票类别，发票状态，对方信息，发票号码  outputPublic [记账日期，发票类别，发票状态，对方信息] outputInvoiceNum 发票号码
    def setOutputInvoicePublic(self,outputPublic,outputInvoiceNum):
        # SetDate(self.driver,'//*[@id="datePiker"]/span/span[2]',outputPublic[0])
        dateButtonLocator = self.driver.find_elements_by_class_name("col-md-3")[0].find_element_by_tag_name('p-calendar')
        dateButtonLocator.click()
        time.sleep(2)
        self.driver.find_element_by_link_text(outputPublic[0]).click()
        time.sleep(2)
        self.setInvoiceType(outputPublic[1])
        self.setInvoiceStatus(outputPublic[2])
        self.setOtherInfo(outputPublic[3])
        self.setInvoiceNum(outputInvoiceNum)

    #设置开票明细-类别，部门性质，税率，价税合计金额，备注 outputItems [类别，部门性质，税率，价税合计金额，备注]
    def setOutputInvoiceItems(self,outputItems):
        self.setCategory(outputItems[0])
        self.setDepartment(outputItems[1])
        self.setRate(outputItems[2])
        self.setMoney(outputItems[3])
        self.setRemark(outputItems[4])

    # 记开票 通过点击保存并新增按钮
    def recordOutputInvoice(self,outputPublic,outputInvoiceNum,outputItems):
        self.setOutputInvoicePublic(outputPublic,outputInvoiceNum)
        self.setOutputInvoiceItems(outputItems)
        self.clickSaveAndAdd()