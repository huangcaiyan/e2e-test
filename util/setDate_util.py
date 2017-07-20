from selenium import webdriver
import time

class SetDate(object):
    def __init__(self,driver):
        self.driver = driver
        self.date_button_xpath = '//*[@id="body"]/detail/outcome/div/div[2]/form/div[1]/div/p-calendar/span/span[2]'

    def setDate(self,day):
        self.driver.find_element_by_xpath(self.date_button_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_link_text(day).click()
