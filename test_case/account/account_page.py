import time
import sys
import os
import logging


class AccountPage():

    #元素定位器
    add_accountbutton_id = 'addAccountButton'
    input_accountName_id = 'input-accountName'
    input_bankName_id = 'input-bankName'
    input_subbranch_id = 'input-subbranch'
    input_accountNumber_id = 'input-accountNumber'
    input_description_id = 'input-description'
    saveButton_id = 'saveButton'
    
    # 微信账户名称元素定位
    add_weixin_xpath = '//*[@id="body"]/account/gpw-account-details-modal/div/div/div/div[2]/div/tabset/ul/li[2]/a/span'
    input_accountName_id_WeChat = 'input-accountName3'
    input_accountNumber_id_WeChat = 'input-accountNumber3'
    input_description_id_WeChat = 'input-description3'

    # 支付宝账户名称元素定位
    add_zhifubao_xpath = '//*[@id="body"]/account/gpw-account-details-modal/div/div/div/div[2]/div/tabset/ul/li[3]/a/span'
    input_accountName_id_zhifubao = 'input-accountName4'
    input_accountNumber_id_zhifubao = 'input-accountNumber4'
    input_description_id_zhifubao = 'input-description4'





    def __init__(self, driver):
        self.driver = driver
        
    
    # 进入账户列表
    def goToAccountModule(self, baseUrl):
        subUrl = '/app/account'
        self.driver.get(baseUrl + subUrl)

    # 打开添加账户窗口
    def openAddAcountPage(self):
        try:
            self.driver.find_element_by_id(self.add_accountbutton_id).click()
            time.sleep(5)
        except Exception as e:
            print ('===================打开添加账户窗口失败==================')
            logging.exception(e)

    # 跳转到添加微信窗口
    def gotoAddWeixinModule(self, parameter_list):
        self.driver.find_element_by_xpath(self.add_weixin_xpath).click()


    # 跳转到添加支付宝窗口
    def gotoAddWeixinModule(self, parameter_list):
        self.driver.find_element_by_xpath(self.add_zhifubao_xpath).click()


    
    # 输入银行账户名称
    def InputaccountName(self,InputaccountName):
        input_accountName = self.driver.find_element_by_id(self.input_accountName_id)
        input_accountName.send_keys(InputaccountName)

    # 输入开户银行名称
    def InputbankName(self, InputbankName):
        input_bankName = self.driver.find_element_by_id(self.input_bankName_id)
        input_bankName.send_keys(InputbankName)

    # 输入支行
    def Inputsubbranch(self, Inputsubbranch):
        input_subbranch = self.driver.find_element_by_id(self.input_subbranch_id)
        input_subbranch.send_keys(Inputsubbranch)

    # 输入账号
    def InputaccountNumber(self, InputaccountNumber):
        input_accountNumber = self.driver.find_element_by_id(self.input_accountNumber_id)
        input_accountNumber.send_keys(InputaccountNumber)

    
    # 输入银行备注
    def Inputdescription(self, Inputdescription):
        input_description = self.driver.find_element_by_id(self.input_description_id)
        input_description.send_keys(Inputdescription)


    # 输入微信账户名称
    def InputaccountNameWeixin(self, InputaccountNameWeChat):
        input_accountName_weixin = self.driver.find_element_by_id(self.input_accountName_id_WeChat)
        input_accountName_weixin.send_keys(InputaccountNameWeChat)

    # 输入微信账号
    def InputaccountNumberWeixin(self, InputaccountNumberWeChat):
        input_accountNumber = self.driver.find_element_by_id(self.input_accountNumber_id_WeChat)
        input_accountNumber.send_keys(InputaccountNumberWeChat)

    # 输入微信备注
    def InputdescriptionWweixin(self, InputdescriptionWeChat):
        input_description = self.driver.find_element_by_id(self.input_description_id_WeChat)
        input_description.send_keys(InputdescriptionWeChat)



    
    # 输入支付宝账户名称
    def InputaccountNameWeixin(self, InputaccountNameAlipay):
        input_accountName_weixin = self.driver.find_element_by_id(self.input_accountName_id_Alipay)
        input_accountName_weixin.send_keys(InputaccountNameAlipay)

    # 输入支付宝账号
    def InputaccountNumberWeixin(self, InputaccountNumberAlipay):
        input_accountNumber = self.driver.find_element_by_id(self.input_accountNumber_id_Alipay)
        input_accountNumber.send_keys(InputaccountNumberAlipay)

    # 输入支付宝备注
    def InputdescriptionWweixin(self, InputdescriptionAlipay):
        input_description = self.driver.find_element_by_id(self.input_description_id_Alipay)
        input_description.send_keys(InputdescriptionAlipay)


    # 点击保存按钮
    def SaveButton(self):
        save_Button = self.driver.find_element_by_id(self.saveButton_id)
        save_Button.click()


    # 添加银行账户
    def test_add_bank_account(self,account_data):
        # self.driver.get(page_url)
        self.InputaccountName(account_data[0])
        self.InputbankName(account_data[1])
        self.Inputsubbranch(account_data[2])
        self.InputaccountNumber(account_data[3])
        self.Inputdescription(account_data[4])
        self.SaveButton()

    
    # 添加微信账户
    def test_add_WeChat_account(self,account_data_1):
        # self.driver.get(page_url)
        self.InputaccountNameWeChat(account_data_1[0])
        self.InputaccountNumberWeChat(account_data_1[1])
        self.InputdescriptionWeChat(account_data_1[2])
        self.SaveButton()
    

    # 添加支付宝账户
    def test_add_Alipay_account(self, account_data_2):
        self.InputaccountNameAlipay(account_data_2[0])
        self.InputaccountNumberAlipay(account_data_2[1])
        self.InputdescriptionAlipay(account_data_2[2])
        self.SaveButton()