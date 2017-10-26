import time,os,sys
import logging
from selenium import webdriver
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../'))
import xlrd
from openpyxl import load_workbook
from config import *
from .is_element_exit_util import IsElementExit
<<<<<<< HEAD
from selenium.webdriver.common.action_chains import ActionChains
=======
from public_page import PublicPage
>>>>>>> 735c391171023dac287ea94470d35b2205bcf030

#定义从登陆到进入账套
class EnterCompany(object):

    #environment [baseurl,accountCom]
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()
        # self.driver.get(environment[0])
        # self.login(environment[1])
       
    #accountCom [账户，密码，公司名]
    def login(self,accountCom):
        self.driver.find_element_by_id('mobile').clear()
        self.driver.find_element_by_id('mobile').send_keys(accountCom[0])
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(accountCom[1])
        self.driver.find_element_by_xpath('//*[@id="signupForm"]/div[2]/button').click()

        # self.driver.find_element_by_id('usernameInput').clear()
        # self.driver.find_element_by_id('usernameInput').send_keys(accountCom[0])
        # self.driver.find_element_by_id('passwordInput').clear()
        # self.driver.find_element_by_id('passwordInput').send_keys(accountCom[1])
        # self.driver.find_element_by_id('loginButton').click()
        
        isElementExit = IsElementExit(self.driver)
        time.sleep(3)
        if isElementExit.is_element_exit_by_xpath('//*[@id="content"]/div[2]/div[1]/alert/div'):
            print('=========================登陆失败===================================')
            exit()
        time.sleep(5)
            
        try:
            actionsLocator = self.driver.find_element_by_link_text(accountCom[2])
            actions = ActionChains(self.driver)
            actions.move_to_element(actionsLocator).perform()
            time.sleep(4)
            self.driver.find_element_by_link_text(accountCom[2]).click()
            time.sleep(5)
            actions.release()
            print('*******************************进入账套成功啦啦啦！！！*******************************')
        except Exception as e:
            print('===============================进入账套失败喽喽喽……==================================')
            logging.exception(e)

    def goToCompany(self):
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/../test_data/' + '创建公司.xlsx')
        loginSh = wb.sheet_by_name(u'登陆账号')
        loginData = loginSh.row_values(1)
        wb1 = load_workbook('写入数据.xlsx')
        sheet = wb1.get_sheet_by_name('已创建的公司')
        companyName = sheet['A2'].value
        loginData.append(companyName)
        self.driver.get(BaseUrl)
        self.login(loginData)




    
