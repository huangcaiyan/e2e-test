import time
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from util.setDate_util import SetDate


class TransactionPage:

    def __init__(self, driver):
        self.driver = driver
        # 记一笔按钮
        self.record_buttton_xpath = '//*[@id="body"]/list/div/div[2]/div/ol/li[3]/button[2]'
        # 选择账户按钮
        self.account_button_xpath = '//*[@id="body"]/list/div/div[2]/div/ol/li[3]/div/button[1]'
        # 选择账户下拉菜单按钮
        self.account_dropdown_xpath = '//*[@id="body"]/list/div/div[2]/div/ol/li[3]/div/button[2]'
        # 交易账户按钮
        self.account_name_xpath = '//*[@id="body"]/detail/outcome/div/div[2]/form/div[2]/div/ng-select/div/div[2]/span'
        # 对方信息
        self.otherInfo_xpath = '//*[@id="body"]/detail/outcome/div/div[2]/form/div[3]/div/ng-select/div/div[2]/span'
        #类别下拉按钮
        self.category_xpath = '//*[@id="body"]/detail/outcome/div/div[3]/div/table/tbody[1]/tr/th/ng-select/div/div[2]/span'
        #保存按钮
        self.save_button_xpath = '//*[@id="body"]/detail/outcome/div/div[5]/div/span/button[2]'

    # 进入账套
    def goToCompany(self, companyName):
        self.driver.find_element_by_link_text(companyName).click()
        time.sleep(5)

    # 进入收支模块
    def goToTransactionModule(self):
        self.driver.get(
            'https://web-gyz-stage.guanplus.com/app/transaction/list')
        time.sleep(5)

    # 进入记收支模块
    def goToTransactionPage(self, transactionName):
        self.driver.find_element_by_xpath(self.record_buttton_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_link_text(transactionName).click()
        time.sleep(5)

    # 点击选择账户导入按钮
    def clickAccountButton(self):
        self.driver.find_element_by_xpath(self.account_button_xpath).click()

    # 设置交易账户
    def setAccount(self, accountName):
        self.driver.find_element_by_xpath(self.account_name_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_link_text(accountName).click()

    # 设置对方信息
    def setOtherInfo(self, otherInfo):
        self.driver.find_element_by_xpath(self.otherInfo_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_link_text(otherInfo).click()

    #设置类别
    def setCategory(self,first,second):
        self.driver.find_element_by_xpath(self.category_xpath).click()
        time.sleep(3)
        firstXpath = '//*[@id="body"]/detail/outcome/div/div[3]/div/table/tbody[1]/tr/th/ng-select/div/div[2]/ul/li[' + first + ']/div/div[1]'
        # self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[3]/div/table/tbody[1]/tr/th/ng-select/div/div[2]/ul/li[1]/div/div[1]').click()
        self.driver.find_element_by_xpath(firstXpath).click()
        time.sleep(3)
        self.driver.find_element_by_link_text(second).click()

    #设置金额
    def setMoney(self,money):
        self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[3]/div/table/tbody[1]/tr/td[1]/bp-input/input').clear()
        self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[3]/div/table/tbody[1]/tr/td[1]/bp-input/input').send_keys(money)

    #设置备注
    def setRemark(self,remark):
        self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[3]/div/table/tbody[1]/tr/td[2]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="body"]/detail/outcome/div/div[3]/div/table/tbody[1]/tr/td[2]/input').send_keys(remark)

    #记明细
    def recordTransactionItems(self,category,money,remark):
        self.setCategory(category[0],category[1])
        self.setMoney(money)
        self.setRemark(remark)

    # 记收支
    def recordTransaction(self,transaction,items):
        setDate = SetDate(self.driver)
        setDate.setDate(transaction[0])
        self.setAccount(transaction[1])
        self.setOtherInfo(transaction[2])
        self.recordTransactionItems(items[0],items[1],items[2])
        self.driver.find_element_by_xpath(self.save_button_xpath).click()
        time.sleep(5)