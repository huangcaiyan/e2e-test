import time
import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from util.set_date_util import SetDate
from util.is_element_exit_util import IsElementExit


class TransactionPage:
    itemsNumber = ''

    def setItemsNum(self,itemsNum):
        global itemsNumber 
        itemsNumber = itemsNum

    def __init__(self, driver,transactionType):
        self.driver = driver
        self.transactionType = transactionType

    # 进入收支列表
    def goToTransactionModule(self,baseUrl):
        self.driver.get(baseUrl + '/app/transaction/list')
        time.sleep(5)

    # 进入记收支页面
    def goToTransactionPage(self, transactionName):
        try:
            self.driver.find_element_by_xpath('//*[@id="body"]/list/div/div[2]/div/ol/li[3]/button[2]').click()
            time.sleep(5)
            self.driver.find_element_by_link_text(transactionName).click()
            time.sleep(5)
        except Exception as e:
            print('====================================进入记收支页面失败……==============================')
            logging.exception(e)


    #进入凭证列表页面
    def goToVoucherPage(self,baseUrl):
        self.driver.get(baseUrl + '/app/finance/voucher')
        time.sleep(5)

    # 设置交易账户
    def setAccount(self, accountName):
        account_name_xpath = '//*[@id="body"]/detail/'+ self.transactionType + '/div/div[2]/form/div[2]/div/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(account_name_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_link_text(accountName).click()

    # 设置对方信息
    def setOtherInfo(self, otherInfo):
        otherInfo_xpath = '//*[@id="body"]/detail/'+ self.transactionType + '/div/div[2]/form/div[3]/div/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(otherInfo_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_link_text(otherInfo).click()

    #设置类别 【itemNum】 明细行号
    def setCategory(self,category,itemNum=1):
        global itemsNumber 
        itemsNumber = itemNum
        categoryButton = ''
        if int(itemNum) < 2:
            categoryButton = '//*[@id="body"]/detail/' + self.transactionType  + '/div/div[3]/div/table/tbody[1]/tr/th/ng-select/div/div[2]/span'
        else:
            categoryButton = '//*[@id="body"]/detail/' + self.transactionType + '/div/div[3]/div/table/tbody[1]/tr[' + itemNum + ']/th/ng-select/div/div[2]/span'
        self.driver.find_element_by_xpath(categoryButton).click()
        time.sleep(3) 
        firstXpath = '//*[@id="body"]/detail/' + self.transactionType + '/div/div[3]/div/table/tbody[1]/tr/th/ng-select/div/div[2]/ul/li[' + category[0] + ']/div/div[1]'
        self.driver.find_element_by_xpath(firstXpath).click()
        time.sleep(3)
        if int(category[1]) == 1:
            secondXpath = '//*[@id="body"]/detail/'+ self.transactionType + '/div/div[3]/div/table/tbody[1]/tr/th/ng-select/div/div[2]/div/div[1]/div/button/div'
        else:
            secondXpath = '//*[@id="body"]/detail/'+ self.transactionType + '/div/div[3]/div/table/tbody[1]/tr/th/ng-select/div/div[2]/div/div['+ category[1] +']/div[2]/button/div'      
        self.driver.find_element_by_xpath(secondXpath).click()

    #设置金额
    def setMoney(self,money):
        if int(itemsNumber) < 2:
            moneyXpath = '//*[@id="body"]/detail/'+ self.transactionType + '/div/div[3]/div/table/tbody[1]/tr/td[1]/bp-input/input'
        else:
            moneyXpath = '//*[@id="body"]/detail/'+ self.transactionType + '/div/div[3]/div/table/tbody[1]/tr[' + itemsNumber + ']/td[1]/bp-input/input'
        self.driver.find_element_by_xpath(moneyXpath).clear()
        self.driver.find_element_by_xpath(moneyXpath).send_keys(money)

    #设置备注
    def setRemark(self,remark=None):
        if int(itemsNumber) < 2:
            remarkXpath = '//*[@id="body"]/detail/' + self.transactionType + '/div/div[3]/div/table/tbody[1]/tr/td[2]/input'
        else:
            remarkXpath = '//*[@id="body"]/detail/' + self.transactionType + '/div/div[3]/div/table/tbody[1]/tr[' + itemsNumber + ']/td[2]/input'
        self.driver.find_element_by_xpath(remarkXpath).clear()
        self.driver.find_element_by_xpath(remarkXpath).send_keys(remark)

    #点击新增明细按钮-新增一行
    def clickAddItems(self):
        addItemsXpath = '//*[@id="body"]/detail/'+ self.transactionType + '/div/div[4]/div[1]/a'
        self.driver.find_element_by_xpath(addItemsXpath).click()

    #点击保存按钮
    def clickSaveButton(self):
        saveButtonXpath = '//*[@id="body"]/detail/' + self.transactionType + '/div/div[5]/div/span/button[2]'
        self.driver.find_element_by_xpath(saveButtonXpath).click()
        time.sleep(5)

    #点击保存并新增按钮
    def clickSaveAndAddButton(self):
        saveAndButtonXpath = '//*[@id="body"]/detail/' + self.transactionType + '/div/div[5]/div/span/button[1]'
        self.driver.find_element_by_xpath(saveAndButtonXpath).click()
        time.sleep(3)
        
    #设置明细：类别，金额，备注 items 是一个list [类别，金额，备注]
    def setTransactionItems(self,items):
        category = items[0]
        self.setCategory(items[0])
        self.setMoney(items[1])
        self.setRemark(items[2])

    #设置收支的记账日期，交易账户，对方信息 publicTransaction 是一个list,[记账日期，交易账户，对方信息]
    def setPublicTransaction(self,publicTransaction):
        date_button_xpath = '//*[@id="body"]/detail/'+ self.transactionType +'/div/div[2]/form/div[1]/div/p-calendar/span/span[2]'
        SetDate(self.driver,date_button_xpath,publicTransaction[0])
        self.setAccount(publicTransaction[1])
        self.setOtherInfo(publicTransaction[2])

    # 记收支-> 点击保存并新增按钮记收支
    def recordTransaction(self,publicTransaction,items):
        self.setPublicTransaction(publicTransaction)
        self.setTransactionItems(items)
        self.clickSaveAndAddButton()

    #####################################################账户互转##############################################################################
    # 设置转出账户
    def setTransferOut(self,accountOutName):
        isEelementExit = IsElementExit(self.driver)
        if isEelementExit.is_element_exit_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[2]/div/form/div[2]/ng-select[1]/div/div[2]/span'):
            self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[2]/div/form/div[2]/ng-select[1]/div/div[2]/span').click()
            time.sleep(2)
            self.driver.find_element_by_link_text(accountOutName).click() 
        else:
            print('====================================转出账户可能不存在==============================================')        

    #设置转入账户
    def setTransferIn(self,accountInName):
        isEelementExit = IsElementExit(self.driver)
        if isEelementExit.is_element_exit_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[2]/div/form/div[2]/ng-select[2]/div/div[2]/span'):
            self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[2]/div/form/div[2]/ng-select[2]/div/div[2]/span').click()
            time.sleep(2)
            self.driver.find_element_by_link_text(accountInName).click()    
        else:
            print('====================================转入账户可能不存在==============================================')  
            
    #设置资金流向  accountNames[转出账户，转入账户]
    def setFundFlow(self,accountOutName,accountInName):
        self.setTransferOut(accountOutName)
        self.setTransferIn(accountInName)
        
    #账户互转-设置金额
    def setTransferMoney(self,money):
        self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[2]/div/form/div[3]/bp-input/input').clear()
        self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[2]/div/form/div[3]/bp-input/input').send_keys(money)

    #账户互转-设置备注
    def setTransferRemark(self,remark=None):
        self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[2]/div/form/div[4]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[2]/div/form/div[4]/input').send_keys(remark)

    #账户互转-点击保存按钮
    def transferClickSaveButton(self):
        self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[3]/div/span/button[2]').click()
        time.sleep(5)
    
    #账户互转-点击保存并新增按钮
    def transferClickSaveAndAddButton(self):
        self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[3]/div/span/button[1]').click()
        time.sleep(2)

    #记账户互转-点击保存并新增 transferPara [记账日期，转出账户，转入账户，金额，备注]
    def recordTransfer(self,transferPara):
        dateButtonXPath = '//*[@id="body"]/detail/accounttransfers/div/div[2]/div/form/div[1]/p-calendar/span/span[2]'
        SetDate(self.driver,dateButtonXPath,transferPara[0])
        self.setFundFlow(transferPara[1],transferPara[2])
        self.setTransferMoney(transferPara[3])
        self.setTransferRemark(transferPara[4])
        self.transferClickSaveAndAddButton()

    #删除记账日期
    def deleteDate(self):
        self.driver.find_element_by_xpath('//*[@id="body"]/detail/accounttransfers/div/div[2]/div/form/div[1]/p-calendar/span/span[1]').click()
        time.sleep(1)