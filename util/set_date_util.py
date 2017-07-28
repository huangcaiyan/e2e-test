from selenium import webdriver
import time

class SetDate(object):
    def __init__(self,driver,elementLocator,day):
        self.driver = driver    
        self.driver.find_element_by_xpath(elementLocator).click()
        time.sleep(3)
        self.driver.find_element_by_link_text(day).click()
        time.sleep(2)


