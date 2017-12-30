from selenium import webdriver
import sys
import os
import time
from util.public_page import PublicPage
from .comp_list_elem import *

class CompListPage(object):

    def __init__(self,driver):
        self.driver = driver

    # 点击创建帐套按钮
    def click_create_comp_btn(self):
        try:
            public_page = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(create_comp_btn_elem)
            public_page.click_elem(btn_loc)
        except Exception as e:
            print('[CompListPage]点击创建帐套按钮失败=>',str(e))

    # 进入帐套
    def enter_comp(self, comp_name):
        try:
            public_page = PublicPage(self.driver)
            comp_loc = self.driver.find_element_by_link_text(comp_name)
            public_page.click_elem(comp_loc)
        except Exception as e:
            print('[CompListPage]enter_comp：进入帐套失败，失败原因=>',str(e))











    
            
            
        

