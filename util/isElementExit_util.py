from selenium import webdriver

class IsElementExit(object):

    def __init__(self,driver):
        self.driver = driver

    def is_element_exit_by_xpath(self,locator):
        elementLocator = self.driver.driver.find_element_by_xpath(locator)
        if elementLocator == None:
            print('元素未找到！')