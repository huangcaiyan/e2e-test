from selenium import webdriver
import sys
import os
import time
from util.public_page import PublicPage
from .add_stuff_elem import *

class AddStuffPage(object):

    def __init__(self,driver):
        self.driver = webdriver.Chrome()
        # self.driver = driver

   
    
    # 竟是框是否出现
    def has_danger_is_show(self):
        publicPage = PublicPage(self.driver)
        ui_loc = self.driver.find_element_by_css_selector(has_danger_elem)
        publicPage.is_element_present(ui_loc)

    # 设置编号
    # num：编号
    def set_nun(self,num):
        publicPage = PublicPage(self.driver)
        input_loc = self.driver.find_element_by_xpath(nun_elem)
        