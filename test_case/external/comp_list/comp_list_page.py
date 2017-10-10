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
            publicPage = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(create_comp_btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print('[CompListPage] There was an exception when click_create_comp_btn=>',str(e))

    # 进入帐套
    def enter_comp(self,comp_name):
        try:
            publicPage = PublicPage(self.driver)
            comp_loc = = self.driver.find_element_by_link_text(comp_name)
            publicPage.click_elem(comp_loc)
        except Exception as e:
            print('[CompListPage] There was an exception when enter_comp=>',str(e))

    
            
            
        

