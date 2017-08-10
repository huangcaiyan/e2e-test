from selenium import webdriver
import time
import logging
from .is_element_exit_util import IsElementExit
from .set_date_util import SetDate
from util.generate_random_util import GenerateRandom
from datetime import datetime
import xlrd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#创建公司
class CreateCompay(object):
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()

    def get(self,baseUrl):
        self.driver.get(baseUrl)

     #登陆
    def login(self,account):
        idlocators = ['usernameInput','passwordInput']
        for idlocator,textValue in zip(idlocators,account):
            self.driver.find_element_by_id(idlocator).clear()
            self.driver.find_element_by_id(idlocator).send_keys(textValue)
        self.driver.find_element_by_id('loginButton').click()
        isElementExit = IsElementExit(self.driver)
        time.sleep(3)
        if isElementExit.is_element_exit_by_xpath('//*[@id="content"]/div[2]/div[1]/alert/div'):
            print('=========================登陆失败===================================')
            exit()
        time.sleep(10)

    #创建公司-手动
    def createCompany(self,companyPara):
        createCompanyLocater = '//*[@id="body"]/company-list/div[1]/div[3]/div[2]/button[1]'
        self.driver.find_element_by_xpath(createCompanyLocater).click()
        time.sleep(3)
        manualCreateLocator = '//*[@id="manual-link"]'
        self.driver.find_element_by_xpath(manualCreateLocator).click()
        time.sleep(3)
        nameLocators = ['companyName','legalPersonName','registeredCapital']
        for namelocator,textValue in zip(nameLocators,companyPara[0:3]):
            self.driver.find_element_by_name(namelocator).clear()
            self.driver.find_element_by_name(namelocator).send_keys(textValue)
        self.setAddress(companyPara[3:6])
        SetDate(self.driver,'//*[@id="setupDate"]/span/span[2]',companyPara[6])
        self.driver.find_element_by_name('taxNumber').clear
        self.driver.find_element_by_name('taxNumber').send_keys(companyPara[7])
        industryLocator = '//*[@id="createCompany"]/div[4]/div/div[2]/table/tbody/tr/td[9]/div/ng-select/div/div[2]/span'
        companyNature = '//*[@id="createCompany"]/div[4]/div/div[2]/table/tbody/tr/td[10]/div/ng-select/div/div[2]/span'
        for locator,selectValue in zip([industryLocator,companyNature],companyPara[8:10]):
            self.driver.find_element_by_xpath(locator).click()
            self.driver.find_element_by_link_text(selectValue).click()
        startDateButtonLocator = '//*[@id="createCompany"]/div[4]/div/div[2]/table/tbody/tr/td[11]/div/datepicker/datepicker-inner/div/monthpicker/div[1]/span/span[2]'
        self.driver.find_element_by_xpath(startDateButtonLocator).click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('month-button')[int(companyPara[10])-1].click()
        createCompanyLocator = '//*[@id="createCompany"]/div[7]/div/span/button[1]'
        self.driver.find_element_by_xpath(createCompanyLocator).click()
        try:
            alertElement = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="createCompany"]/div[1]/alert/div'))) 
            print('======================================失败创建账套==========================================')
            self.driver.get_screenshot_as_file('createCompanyerror.jpg')
        except Exception as e:
            print('*************************************成功创建账套********************************')
            # logging.exception(e)

    #地址
    def setAddress(self,address):
        try:
            provinceLocator = '//*[@id="createCompany"]/div[4]/div/div[2]/table/tbody/tr/td[4]/div/ng-select/div/div[2]/span'
            cityLocator = '//*[@id="createCompany"]/div[4]/div/div[2]/table/tbody/tr/td[5]/div/ng-select/div/div[2]/span'
            districtLocator = '//*[@id="createCompany"]/div[4]/div/div[2]/table/tbody/tr/td[6]/div/ng-select/div/div[2]/span'
            locators = [provinceLocator,cityLocator,districtLocator]
            for locator,address in zip(locators,address):
                self.driver.find_element_by_xpath(locator).click()
                time.sleep(2)
                self.driver.find_element_by_link_text(address).click()

        except Exception as e:
            print('====================================设置公司地址失败===============================================')
            logging.exception(e)


    #进入账套
    def goToCompany(self,goToCompanyPara):
        try:
            self.login(goToCompanyPara[0])
            self.createCompany(goToCompanyPara[1])
            self.driver.find_element_by_link_text(goToCompanyPara[1][0]).find_element_by_xpath('../../..').find_elements_by_tag_name('td')[3].click()
            time.sleep(2)
            self.setClient(goToCompanyPara[2][0:2])
            for role,locator in zip(goToCompanyPara[2][2:],[4,5]):
                self.driver.find_element_by_link_text(goToCompanyPara[1][0]).find_element_by_xpath('../../..').find_elements_by_tag_name('td')[locator].click()
                time.sleep(2)
                self.setRole(role)
            self.driver.find_element_by_link_text(goToCompanyPara[1][0]).click()
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/beginning-period/div/div[3]/div[2]/div[2]/div[1]/button').click()
            time.sleep(8)
            print('***********************************************成功创建并进入账套啦啦啦*****************************************************************')
        except Exception as e:
            print('====================================失败进入账套===============================================')
            logging.exception(e)

    #设置客户联系人
    def setClient(self,clientInfo):
        try:
            clientNameLocator = '//*[@id="name"]'
            clientPhoneLocator = 'phoneNumber'
            saveButtonLocator = '//*[@id="body"]/company-list/gpw-invite-customer-modal/div[2]/div/div/div[3]/button[1]'
            self.driver.find_element_by_xpath(clientNameLocator).clear()
            self.driver.find_element_by_xpath(clientNameLocator).send_keys(clientInfo[0])
            self.driver.find_elements_by_id(clientPhoneLocator)[1].clear()
            self.driver.find_elements_by_id(clientPhoneLocator)[1].send_keys(clientInfo[1])
            self.driver.find_element_by_xpath(saveButtonLocator).click()
            time.sleep(3)
        except Exception as e:
            print('====================================填写客户联系人失败===============================================')
            logging.exception(e)

    #分配会计/助理
    def setRole(self,roleInfo):
        try:
            roleNameLocator = '//*[@id="name-sel"]/div/div[2]/span'
            inviteButtonLocator = '//*[@id="body"]/company-list/gpw-invite-user-new-modal/div/div/div/div[3]/div/button'
            WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,roleNameLocator))).click() 
            # self.driver.find_element_by_xpath(roleNameLocator).click()
            # time.sleep(3)
            WebDriverWait(self.driver,3,0.5).until(EC.presence_of_all_elements_located((By.LINK_TEXT,roleInfo)))[1].click()
            # self.driver.find_elements_by_link_text(roleInfo)[1].click()
            # time.sleep(2)
            self.driver.find_element_by_xpath(inviteButtonLocator).click()
            time.sleep(3)
        except Exception as e:
            print('====================================分配会计或助理失败===============================================')
            # logging.exception(e)


    #进入创建账户页面
    def goToCreateAccountPage(self,baseUrl):
        self.driver.get(baseUrl + '/app/account' )
        time.sleep(3)
        addButtouLocator = '//*[@id="addAccountButton"]'
        self.driver.find_element_by_xpath(addButtouLocator).click()
        time.sleep(2)

    #创建账户
    def createAccount(self,accountType,accountName):
        if '添加银行账户' == accountType:
            accountNameLocator = './/*[@id="input-accountName"]'
        else:
            accountNameLocator = ".//*[@id='input-accountNumber3']"

        self.driver.find_element_by_xpath(accountNameLocator).clear()
        self.driver.find_element_by_xpath(accountNameLocator).send_keys(accountName)
        saveButtonLocator = ".//*[@id='saveButton']"
        self.driver.find_element_by_xpath(saveButtonLocator).click()
        alertLocator = ".//*[@id='body']/account/div[1]/alert/div"
        try:
             WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,alertLocator)))
        except Exception as e:
            print('======================================创建账户失败======================================================')
        
        

