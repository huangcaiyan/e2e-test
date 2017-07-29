import time
import logging
from selenium import webdriver
from .is_element_exit_util import IsElementExit

#定义从登陆到进入账套
class EnterCompany(object):

    #environment [baseurl,accountCom]
    def __init__(self,driver,environment):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(environment[0])
        self.login(environment[1])
       
    #accountCom [账户，密码，公司名]
    def login(self,accountCom):
        self.driver.find_element_by_id('usernameInput').clear()
        self.driver.find_element_by_id('usernameInput').send_keys(accountCom[0])
        self.driver.find_element_by_id('passwordInput').clear()
        self.driver.find_element_by_id('passwordInput').send_keys(accountCom[1])
        self.driver.find_element_by_id('loginButton').click()
        isElementExit = IsElementExit(self.driver)
        time.sleep(3)
        if isElementExit.is_element_exit_by_xpath('//*[@id="content"]/div[2]/div[1]/alert/div'):
            print('=========================登陆失败===================================')
            exit()
        time.sleep(20)
            
        try:
            self.driver.find_element_by_link_text(accountCom[2]).click()
            time.sleep(5)
            print('*******************************进入账套成功啦啦啦！！！*******************************')
        except Exception as e:
            print('===============================进入账套失败喽喽喽……==================================')
            logging.exception(e)



    
