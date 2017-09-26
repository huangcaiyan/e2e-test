from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class AccountDashbaordPage(object):

    def __init__(self,driver):
        self.driver = driver

    #进入会计首页
    def goAssistanDashbaordPage(self,url):
        self.driver.get(url + '/app/home-page/accounting')
        sleep(2)

    #点击操作按钮
    def clickOperationButton(self):
        operationButtonLocator = '//*[@id="body"]/accounting-home-page/div[3]/div/div[2]/div[2]/button'
        operationButton = self.driver.find_element_by_xpath('//*[@id="body"]/accounting-home-page/div[2]/div[1]/div')
        actions = ActionChains(self.driver)
        actions.move_to_element(operationButton).perform()
        self.driver.find_element_by_xpath(operationButtonLocator).click()
        sleep(2)

    #结转成功-点击知道了按钮
    def clickIKnowButton(self):
        buttonLocaotr = '//*[@id="body"]/accounting-home-page/carry-forward-modal/div/div/div/div[2]/button[2]'
        self.driver.find_element_by_xpath(buttonLocaotr).click()
        sleep(2)
        
    #过账弹出-点击过账按钮
    def clickPostButton(self):
        buttonLocator = '//*[@id="body"]/accounting-home-page/posting-modal/div/div/div/div[2]/button[1]'
        self.driver.find_element_by_xpath(buttonLocator).click()
        sleep(3)

    #点击 结转/过账/反过账/驳回审核 按钮
    def clickDropDown(self,index):
        self.clickOperationButton()
        self.driver.find_element_by_class_name('dropdown-menu').find_elements_by_tag_name('button')[index].click()
        sleep(3)