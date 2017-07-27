from selenium import webdriver
import logging

class IsElementExit(object):

    def __init__(self,driver):
        self.driver = driver

    def is_element_exit_by_xpath(self,locator):
        try:
            self.driver.find_element_by_xpath(locator)
            return True
        except Exception as e:
            logging.exception(e)
            return False