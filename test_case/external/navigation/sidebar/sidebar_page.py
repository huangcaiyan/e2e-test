from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from util.public_page import PublicPage
from .sidebar_elem import *

class SidebarPage:

    def __init__(self,driver):
        # self.driver = webdriver.Chrome()        
        self.driver = driver

    def get_account_status(self):
        try:
            text_loc = self.driver.find_element_by_css_selector(account_status_elem)
            base_value = text_loc.text
            value = base_value.split(' ')+'\n'
            return value
        except Exception as e:
            print('[SidebarPage]－－获取当前会计期间失败－－失败原因是＝>',str(e))

        
