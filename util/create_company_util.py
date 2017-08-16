from selenium import webdriver
import time,os,sys
import logging
from .is_element_exit_util import IsElementExit
from .set_date_util import SetDate
from .generate_random_util import GenerateRandom
from datetime import datetime
import xlrd
from openpyxl import load_workbook
from openpyxl import Workbook
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
            #将创建的公司名字写入到excel中
            wb = load_workbook('写入数据.xlsx')
            sheet = wb.get_sheet_by_name('已创建的公司')
            sheet['A2'] = companyPara[0]
            wb.save('写入数据.xlsx')

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
            self.driver.find_element_by_link_text(goToCompanyPara[1][0]).find_element_by_xpath('../../..').find_elements_by_tag_name('td')[2].click()
            time.sleep(2)
            self.setClient(goToCompanyPara[2][0:2])
            for role,locator in zip(goToCompanyPara[2][2:],[3,4]):
                self.driver.find_element_by_link_text(goToCompanyPara[1][0]).find_element_by_xpath('../../..').find_elements_by_tag_name('td')[locator].click()
                time.sleep(2)
                self.setRole(role)
            self.driver.find_element_by_link_text(goToCompanyPara[1][0]).click()
            time.sleep(10)
            startButtonLocator = '//*[@id="body"]/finance/div/beginning-period/div/div[3]/div[2]/div[2]/div[1]/button'
            WebDriverWait(self.driver,2,0.5).until(EC.presence_of_element_located((By.XPATH,startButtonLocator))).click()
            time.sleep(8)
        except Exception as e:
            print('====================================失败进入账套===============================================')
            logging.exception(e)

    #设置客户联系人
    def setClient(self,clientInfo):
        try:
            clientNameLocator = '//*[@id="name"]'
            clientPhoneLocator = 'phoneNumber'
            saveButtonLocator = '//*[@id="body"]/company-list/gpw-invite-customer-modal/div[2]/div/div/div[3]/button[1]'
            clientnameInput = WebDriverWait(self.driver,3,0.5).until(EC.presence_of_element_located((By.XPATH,clientNameLocator))) 
            clientnameInput.clear()
            clientnameInput.send_keys(clientInfo[0])
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
            self.driver.find_element_by_xpath(roleNameLocator).click()
            time.sleep(3)
            self.driver.find_element_by_link_text(roleInfo).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(inviteButtonLocator).click()
            time.sleep(3)
        except Exception as e:
            print('====================================分配会计或助理失败===============================================')
            logging.exception(e)


    #进入创建账户页面
    def goToCreateAccountPage(self,baseUrl):
        self.driver.get(baseUrl + '/app/account' )
        time.sleep(3)
        accountListAlertLocator = ".//*[@id='body']/account/div[1]/alert/div"
        try:
            accountListAlert = WebDriverWait(self.driver,3,0.2).until(EC.presence_of_element_located((By.XPATH,accountListAlertLocator)))
            if '服务器生病了，请再试一下' == accountListAlert.text:
                print('================================================账户列表页面服务器生病了=============================================================')
                self.driver.get_screenshot_as_file('F:\\autoTest_workspace\\python_code\\e2e-test\\report\\images\\accountListServerError.jpg')
        except Exception as e:
            pass

        addButtouLocator = '//*[@id="addAccountButton"]'
        self.driver.find_element_by_xpath(addButtouLocator).click()
        time.sleep(2)

    #创建账户 accountType 添加的账户类型 如：添加银行账户，添加微信，添加支付宝  accountName 账户名称
    def createAccount(self,accountType,accountName):
        if '添加银行账户' == accountType:
            accountNameInput = self.driver.find_element_by_id('input-accountName')
        elif '添加微信' == accountType:
            accountNameLocator = '//*[@id="body"]/account/gpw-account-details-modal/div/div/div/div[2]/div/tabset/div/tab[2]'
            accountNameInput = self.driver.find_element_by_xpath(accountNameLocator).find_elements_by_tag_name('div')[0].find_element_by_tag_name('form').find_elements_by_tag_name('div')[0].find_element_by_tag_name('input')
        elif '添加支付宝' == accountType:
            accountNameLocator = '//*[@id="body"]/account/gpw-account-details-modal/div/div/div/div[2]/div/tabset/div/tab[3]'
            accountNameInput = self.driver.find_element_by_xpath(accountNameLocator).find_elements_by_tag_name('div')[0].find_element_by_tag_name('form').find_elements_by_tag_name('div')[0].find_element_by_tag_name('input')
            
        self.driver.find_element_by_link_text(accountType).click()
        accountNameInput.clear()
        accountNameInput.send_keys(accountName)
        saveButtonLocator = ".//*[@id='saveButton']"
        self.driver.find_element_by_xpath(saveButtonLocator).click()
        addAccountPageAlertLocator = '//*[@id="body"]/account/gpw-account-details-modal/div/div/div/div[2]/div[1]/alert/div'
        try:
            WebDriverWait(self.driver,2,0.2).until(EC.presence_of_element_located((By.XPATH,addAccountPageAlertLocator)))
            print('================================================创建账户失败=============================================================')
            self.driver.get_screenshot_as_file('F:\\autoTest_workspace\\python_code\\e2e-test\\report\\images\\addAccountError.jpg')
        except Exception as e:
            pass       
        
# def test():
#     driver = webdriver.Chrome()
#     driver.get('https://firms.guanplus.com')
#     cc = CreateCompay(driver)
#     cc.login(['18514509382','qq123456'])
#     driver.find_element_by_link_text('一般纳税人08042054').click()
#     time.sleep(5)
#     cc.goToCreateAccountPage('https://firms.guanplus.com')
#     time.sleep(3)
#     cc.createAccount('添加微信','添加微信1')
#     cc.goToCreateAccountPage('https://firms.guanplus.com')
#     cc.createAccount('添加银行账户','招商招商1')
#     cc.goToCreateAccountPage('https://firms.guanplus.com')
#     cc.createAccount('添加支付宝','宝宝1')
#     driver.quit()

# test()

