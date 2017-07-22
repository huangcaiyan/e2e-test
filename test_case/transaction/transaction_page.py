import time
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from util.setDate_util import SetDate


class TransactionPage:
    itemsNumber = ''

    def setItemsNum(self,itemsNum):
        global itemsNumber 
        itemsNumber = itemsNum

    def __init__(self, driver,classify):
        self.driver = driver
        self.classify = classify
        # 记一笔按钮
        self.record_buttton_xpath = '//*[@id="body"]/list/div/div[2]/div/ol/li[3]/button[2]'
        # 选择账户按钮
        self.account_button_xpath = '//*[@id="body"]/list/div/div[2]/div/ol/li[3]/div/button[1]'
        # 选择账户下拉菜单按钮
        self.account_dropdown_xpath = '//*[@id="body"]/list/div/div[2]/div/ol/li[3]/div/button[2]'

    # 进入账套
    def goToCompany(self, companyName):
        self.driver.find_element_by_link_text(companyName).click()
        time.sleep(5)

    # 进入收支模块
    def goToTransactionModule(self,baseUrl):
        self.driver.get(baseUrl + '/app/transaction/list')
        time.sleep(5)

    # 进入记收支模块
    def goToTransactionPage(self, transactionName):
        self.driver.find_element_by_xpath(self.record_buttton_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_link_text(transactionName).click()
        time.sleep(5)

    #进入凭证列表页面
    def goToVoucherPage(self,baseUrl):
        self.driver.get(baseUrl + '/app/finance/voucher')
        time.sleep(5)

    # 点击选择账户导入按钮
    def clickAccountButton(self):
        self.driver.find_element_by_xpath(self.account_button_xpath).click()

    # 设置交易账户
    def setAccount(self, accountName):
        account_name_xpath = '//*[@id="body"]/detail/'+ self.classify + '/div/div[2]/form/div[2]/div/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(account_name_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_link_text(accountName).click()

    # 设置对方信息
    def setOtherInfo(self, otherInfo):
        otherInfo_xpath = '//*[@id="body"]/detail/'+ self.classify + '/div/div[2]/form/div[3]/div/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(otherInfo_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_link_text(otherInfo).click()

    #设置类别 【itemNum】 明细行号
    def setCategory(self,itemNum,category):
        global itemsNumber 
        itemsNumber = itemNum
        categoryButton = ''
        if int(itemNum) < 2:
            categoryButton = '//*[@id="body"]/detail/' + self.classify + '/div/div[3]/div/table/tbody[1]/tr/th/ng-select/div/div[2]/span'
        else:
            categoryButton = '//*[@id="body"]/detail/' + self.classify + '/div/div[3]/div/table/tbody[1]/tr[' + itemNum + ']/th/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(categoryButton).click()
        time.sleep(3) 
        firstXpath = '//*[@id="body"]/detail/' + self.classify + '/div/div[3]/div/table/tbody[1]/tr/th/ng-select/div/div[2]/ul/li[' + category[0] + ']/div/div[1]'
        self.driver.find_element_by_xpath(firstXpath).click()
        time.sleep(3)
        self.driver.find_element_by_link_text(category[1]).click()

    #设置金额
    def setMoney(self,money):
        if int(itemsNumber) < 2:
            moneyXpath = '//*[@id="body"]/detail/'+ self.classify + '/div/div[3]/div/table/tbody[1]/tr/td[1]/bp-input/input'
        else:
            moneyXpath = '//*[@id="body"]/detail/'+ self.classify + '/div/div[3]/div/table/tbody[1]/tr[' + itemsNumber + ']/td[1]/bp-input/input'
        self.driver.find_element_by_xpath(moneyXpath).clear()
        self.driver.find_element_by_xpath(moneyXpath).send_keys(money)

    #设置备注
    def setRemark(self,remark=None):
        if int(itemsNumber) < 2:
            remarkXpath = '//*[@id="body"]/detail/' + self.classify + '/div/div[3]/div/table/tbody[1]/tr/td[2]/input'
        else:
            remarkXpath = '//*[@id="body"]/detail/' + self.classify + '/div/div[3]/div/table/tbody[1]/tr[' + itemsNumber + ']/td[2]/input'
        self.driver.find_element_by_xpath(remarkXpath).clear()
        self.driver.find_element_by_xpath(remarkXpath).send_keys(remark)

    #点击新增明细按钮-新增一行
    def clickAddItems(self):
        addItemsXpath = '//*[@id="body"]/detail/'+ self.classify + '/div/div[4]/div[1]/a'
        self.driver.find_element_by_xpath(addItemsXpath).click()

    #点击保存按钮
    def clickSaveButton(self):
        saveButtonXpath = '//*[@id="body"]/detail/' + self.classify + '/div/div[5]/div/span/button[2]'
        self.driver.find_element_by_xpath(saveButtonXpath).click()
        time.sleep(5)

    #设置明细：类别，金额，备注 items 是一个list [类别，金额，备注]
    def setTransactionItems(self,items):
        category = items[1]
        self.setCategory(items[0],items[1])
        self.setMoney(items[2])
        self.setRemark(items[3])

    #设置收支的记账日期，交易账户，对方信息 publicTransaction 是一个list,[记账日期，交易账户，对方信息]
    def setPublicTransaction(self,publicTransaction):
        SetDate(self.driver,publicTransaction[0])
        self.setAccount(publicTransaction[1])
        self.setOtherInfo(publicTransaction[2])

    # 记收支
    def recordTransaction(self,publicTransaction,items):
        self.setPublicTransaction(publicTransaction)
        self.setTransactionItems(items)
        self.clickSaveButton()

    # 记多笔收支
    def recordTransactions(self,publicTransaction,items):
        self.setPublicTransaction(publicTransaction)
        self.setTransactionItems(items)
        self.clickSaveButton()