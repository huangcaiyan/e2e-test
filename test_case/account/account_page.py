import time
import sys
import os
import logging
from test_case.account.account_elem import *

# 更新于2017-10-10
class AccountPage():

    def __init__(self, driver):
        self.driver = driver
        
    
    # 进入账户列表
    def goToAccountModule(self, baseUrl):
        subUrl = '/app/account'
        self.driver.get(baseUrl + subUrl)

    # 打开添加账户窗口
    def openAddAcountPage(self):
        try:
            self.driver.find_element_by_id(add_accountbutton_id).click()
            time.sleep(5)
        except Exception as e:
            print ('===================打开添加账户窗口失败==================')
            logging.exception(e)


    # 跳转到添加微信窗口
    def gotoAddWeChatModule(self, parameter_list):
        self.driver.find_element_by_xpath(add_WeChat_xpath).click()


    # 跳转到添加支付宝窗口
    def gotoAddAlipayModule(self, parameter_list):
        self.driver.find_element_by_xpath(add_Alipay_xpath).click()

    
    # 输入银行账户名称
    def InputaccountName(self,InputaccountName):
        input_accountName = self.driver.find_element_by_id(input_accountName_id)
        input_accountName.send_keys(InputaccountName)

    # 输入开户银行名称
    def InputbankName(self, InputbankName):
        input_bankName = self.driver.find_element_by_id(input_bankName_id)
        input_bankName.send_keys(InputbankName)

    # 输入支行
    def Inputsubbranch(self, Inputsubbranch):
        input_subbranch = self.driver.find_element_by_id(input_subbranch_id)
        input_subbranch.send_keys(Inputsubbranch)

    # 输入账号
    def InputaccountNumber(self, InputaccountNumber):
        input_accountNumber = self.driver.find_element_by_id(input_accountNumber_id)
        input_accountNumber.send_keys(InputaccountNumber)

    
    # 输入银行备注
    def Inputdescription(self, Inputdescription):
        input_description = self.driver.find_element_by_id(input_description_id)
        input_description.send_keys(Inputdescription)


    # 输入微信账户名称
    def InputaccountNameWeChat(self, InputaccountNameWeChat):
        input_accountName_WeChat = self.driver.find_element_by_id(input_accountName_id_WeChat)
        input_accountName_WeChat.send_keys(InputaccountNameWeChat)

    # 输入微信账号
    def InputaccountNumberWeChat(self, InputaccountNumberWeChat):
        input_accountNumber = self.driver.find_element_by_id(input_accountNumber_id_WeChat)
        input_accountNumber.send_keys(InputaccountNumberWeChat)

    # 输入微信备注
    def InputdescriptionWeChat(self, InputdescriptionWeChat):
        input_description = self.driver.find_element_by_id(input_description_id_WeChat)
        input_description.send_keys(InputdescriptionWeChat)



    
    # 输入支付宝账户名称
    def InputaccountNameAlipay(self, InputaccountNameAlipay):
        input_accountName_Alipay = self.driver.find_element_by_id(input_accountName_id_Alipay)
        input_accountName_Alipay.send_keys(InputaccountNameAlipay)

    # 输入支付宝账号
    def InputaccountNumberAlipay(self, InputaccountNumberAlipay):
        input_accountNumber = self.driver.find_element_by_id(input_accountNumber_id_Alipay)
        input_accountNumber.send_keys(InputaccountNumberAlipay)

    # 输入支付宝备注
    def InputdescriptionAlipay(self, InputdescriptionAlipay):
        input_description = self.driver.find_element_by_id(input_description_id_Alipay)
        input_description.send_keys(InputdescriptionAlipay)


    # 点击保存按钮
    def SaveButton(self):
        save_Button = self.driver.find_element_by_id(saveButton_id)
        save_Button.click()


    # 添加银行账户
    def test_add_bank_account(self,account_data):
        # self.driver.get(page_url)
        # self.driver.switch_to_active_element()
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
    