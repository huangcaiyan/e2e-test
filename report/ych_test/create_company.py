from selenium import webdriver
import time
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../'))
print(sys.path)
from util.is_element_exit_util import IsElementExit
from util.set_date_util import SetDate
from util.generate_random_util import GenerateRandom
from datetime import datetime
import xlrd


#创建公司
class CreateCompay(object):
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()

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
        time.sleep(8)
        print('#####################################################' + str(IsElementExit(self.driver).is_element_exit_by_xpath('//*[@id="createCompany"]/div[1]/alert/div')))
        if IsElementExit(self.driver).is_element_exit_by_xpath('//*[@id="createCompany"]/div[1]/alert/div'):
            print('========================================================' + str(IsElementExit(self.driver).is_element_exit_by_xpath('//*[@id="createCompany"]/div[1]/alert/div')))
            time.sleep(1)
            self.driver.get_screenshot_as_file('createCompanyerror.jpg')
        time.sleep(10)

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
            # print('***********************************************成功创建并进入账套啦啦啦*****************************************************************')
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
            self.driver.find_element_by_xpath(roleNameLocator).click()
            time.sleep(3)
            self.driver.find_elements_by_link_text(roleInfo)[1].click()
            time.sleep(2)
            self.driver.find_element_by_xpath(inviteButtonLocator).click()
            time.sleep(3)
        except Exception as e:
            print('====================================分配会计或助理失败===============================================')
            logging.exception(e)

# driver = webdriver.Chrome()
driver = webdriver.PhantomJS()
cc = CreateCompay(driver)

# driver.get('https://web-gyz-stage.guanplus.com')
driver.get('https://firms.guanplus.com')
wb = xlrd.open_workbook('F:\\autoTest_workspace\\python_code\\e2e-test\\test_data\\创建公司.xlsx')
loginSh = wb.sheet_by_name(u'登陆账号')
loginRow = loginSh.row_values(1)
print(loginRow)
roleSh = wb.sheet_by_name(u'设置角色')
roleRow = roleSh.row_values(1)
createCompanySh = wb.sheet_by_name(u'创建公司测试数据')
createCompanyRow = createCompanySh.row_values(1)
now = datetime.now()
createCompanyRow[0]=createCompanyRow[0]+now.strftime('%m%d%H%M')
createCompanyRow[7]=GenerateRandom().generateRandom()
print(createCompanyRow)
goToCompanyPara = [loginRow,createCompanyRow,roleRow]
print(goToCompanyPara)
cc.goToCompany(goToCompanyPara)
driver.quit()

