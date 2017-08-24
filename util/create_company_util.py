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
        try:
            alertInfo = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/alert/div').text[8:]
            print('[LOGIN_ALERTINFO:' + alertInfo + ']')
            self.driver.get_screenshot_as_file('./report/images/login_error.jpg')
            self.driver.quit()
            sys.exit()
        except Exception as e:
            print('[SUCESS:登陆]')
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
        # self.setAddress(companyPara[3:6])
        SetDate(self.driver,'//*[@id="setupDate"]/span/span[2]',companyPara[6])
        self.driver.find_element_by_name('taxNumber').clear
        self.driver.find_element_by_name('taxNumber').send_keys(companyPara[7])
        try:
            industryLocator = '//*[@id="createCompany"]/div[4]/div/div[2]/table/tbody/tr/td[9]/div/ng-select/div/div[2]/span'
            companyNature = '//*[@id="createCompany"]/div[4]/div/div[2]/table/tbody/tr/td[10]/div/ng-select/div/div[2]/span'
            # industryLocator = '//*[@id="createCompany"]/div[4]/div/div/table/tbody/tr/td[9]/div/ng-select/div/div[2]/span'
            # companyNature = '//*[@id="createCompany"]/div[4]/div/div/table/tbody/tr/td[10]/div/ng-select/div/div[2]/span'
            for locator,selectValue in zip([industryLocator,companyNature],companyPara[8:10]):
                self.driver.find_element_by_xpath(locator).click()
                self.driver.find_element_by_link_text(selectValue).click()
        except Exception as e:
            print('[ERROR:设置公司行业或性质]')
            self.driver.get_screenshot_as_file('./report/images/setcompanyInduNat_error.jpg')
            self.driver.quit()
            logging.exception(e)
            sys.exit()

        startDateButtonLocator = '//*[@id="createCompany"]/div[4]/div/div[2]/table/tbody/tr/td[11]/div/datepicker/datepicker-inner/div/monthpicker/div[1]/span/span[2]'
        # startDateButtonLocator = '//*[@id="createCompany"]/div[4]/div/div/table/tbody/tr/td[11]/div/datepicker/datepicker-inner/div/monthpicker/div[1]/span/span[2]'
        self.driver.find_element_by_xpath(startDateButtonLocator).click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('month-button')[int(companyPara[10])-1].click()
        createCompanyLocator = '//*[@id="createCompany"]/div[7]/div/span/button[1]'
        self.driver.find_element_by_xpath(createCompanyLocator).click()
        try:
            alertElement = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="createCompany"]/div[1]/alert/div'))) 
            print('[CREATECOMPANY_ALERTINFO:' + alertElement.text[8:] + ']')
            self.driver.get_screenshot_as_file('./report/images/createCompany_error.jpg')
            self.driver.quit()
            sys.exit()
        except Exception as e:
            #将创建的公司名字写入到excel中
            wb = load_workbook('写入数据.xlsx')
            sheet = wb.get_sheet_by_name('已创建的公司')
            sheet['A2'] = companyPara[0]
            wb.save('写入数据.xlsx')

    #地址
    def setAddress(self,address):
        try:
            # provinceLocator = '//*[@id="createCompany"]/div[4]/div/div[2]/table/tbody/tr/td[4]/div/ng-select/div/div[2]/span'
            # cityLocator = '//*[@id="createCompany"]/div[4]/div/div[2]/table/tbody/tr/td[5]/div/ng-select/div/div[2]/span'
            # districtLocator = '//*[@id="createCompany"]/div[4]/div/div[2]/table/tbody/tr/td[6]/div/ng-select/div/div[2]/span'
            provinceLocator = '//*[@id="createCompany"]/div[4]/div/div/table/tbody/tr/td[4]/div/ng-select/div/div[2]/span'
            cityLocator = '//*[@id="createCompany"]/div[4]/div/div/table/tbody/tr/td[5]/div/ng-select/div/div[2]/span'
            districtLocator = '//*[@id="createCompany"]/div[4]/div/div/table/tbody/tr/td[6]/div/ng-select/div/div[2]/span'
            locators = [provinceLocator,cityLocator,districtLocator]
            for locator,address in zip(locators,address):
                self.driver.find_element_by_xpath(locator).click()
                time.sleep(2)
                self.driver.find_element_by_link_text(address).click()

        except Exception as e:
            print('[ERROR:设置公司地址]')
            self.driver.get_screenshot_as_file('./report/images/setAddress_error.jpg')
            self.driver.quit()
            logging.exception(e)
            sys.exit()

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
            #启用期初账
            startButtonLocator = '//*[@id="body"]/finance/div/beginning-period/div/div[3]/div[2]/div[2]/div[1]/button'
            WebDriverWait(self.driver,2,0.5).until(EC.presence_of_element_located((By.XPATH,startButtonLocator))).click()
            time.sleep(8)
            print('[SUCESS:启用期初账]')
        except Exception as e:
            print('[ERROR:启用账套]')
            self.driver.get_screenshot_as_file('./report/images/startCompany_error.jpg')
            self.driver.quit()
            logging.exception(e)
            sys.exit()

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
            print('[ERROR:设置客户联系人]')
            self.driver.get_screenshot_as_file('./report/images/setClient_error.jpg')
            self.driver.quit()
            logging.exception(e)
            sys.exit()
            

    #分配会计/助理
    def setRole(self,roleInfo):
        try:
            roleNameLocator = '//*[@id="name-sel"]/div/div[2]/span'
            inviteButtonLocator = '//*[@id="body"]/company-list/gpw-invite-user-new-modal/div/div/div/div[3]/div/button'
            self.driver.find_element_by_xpath(roleNameLocator).click()
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="name-sel"]/div/ul').find_element_by_link_text(roleInfo).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(inviteButtonLocator).click()
            time.sleep(2)
        except Exception as e:
            print('[ERROR:分配会计或助理]')
            self.driver.get_screenshot_as_file('./report/images/setRole_error.jpg')
            self.driver.quit()
            logging.exception(e)
            sys.exit()
            


    #进入创建账户页面
    def goToCreateAccountPage(self,baseUrl):
        self.driver.get(baseUrl + '/app/account' )
        time.sleep(3)
        accountListAlertLocator = ".//*[@id='body']/account/div[1]/alert/div"
        try:
            accountListAlert = WebDriverWait(self.driver,3,0.2).until(EC.presence_of_element_located((By.XPATH,accountListAlertLocator)))
            print('[ACCOUNTLIST_ALERTINFO:' + accountListAlert.text[8:] + ']')
            self.driver.get_screenshot_as_file('./report/images/accountList_error.jpg')
        except Exception as e:
            # print('[SUCESS:进入创建账户页面]')
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
            alertInfo = WebDriverWait(self.driver,2,0.2).until(EC.presence_of_element_located((By.XPATH,addAccountPageAlertLocator)))
            # print('================================================创建'+ accountName + '账户失败=============================================================')
            # self.driver.get_screenshot_as_file('F:\\autoTest_workspace\\python_code\\e2e-test\\report\\images\\addAccountError.jpg')
            print(accountName + '[CREATEACCOUNT_ALERTINFO:'+ alertInfo.text[8:] + ']')
            self.driver.get_screenshot_as_file('./report/images/createAccount_error.jpg')
        except Exception as e:
            print('[SUCESS:创建' + accountName + '账户]')       
        
# def test():
#     driver = webdriver.Chrome()
#     # driver.get('https://firms.guanplus.com')
#     driver.get('http://guanplus-app-accountingfirm-web-dev-1.cn-north-1.eb.amazonaws.com.cn')
#     cc = CreateCompay(driver)
#     cc.login(['18514509382','qq123456'])
#     driver.find_element_by_xpath('//*[@id="company-table"]/tbody/tr[153]/td[4]/div').click()
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="name-sel"]/div/div[2]/span').click()
#     time.sleep(2)
#     driver.find_element_by_link_text('杨春红')
#     # cc.goToCreateAccountPage('https://firms.guanplus.com')
#     # time.sleep(3)
#     # cc.createAccount('添加微信','添加微信1')
#     # cc.goToCreateAccountPage('https://firms.guanplus.com')
#     # cc.createAccount('添加银行账户','招商招商1')
#     # cc.goToCreateAccountPage('https://firms.guanplus.com')
#     # cc.createAccount('添加支付宝','宝宝1')
#     driver.quit()

# test()

