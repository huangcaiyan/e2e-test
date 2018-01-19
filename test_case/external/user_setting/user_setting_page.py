from selenium import webdriver
import os
import time
from .user_setting_elem import *
from util.public_page import PublicPage


class UserSettingPage:
    def __init__( self, driver ):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    def click_user_name( self ):
        click_loc = self.driver.find_element_by_xpath(user_setting_elem)
        publicPage = PublicPage(self.driver)
        publicPage.click_elem(click_loc)

    def go_to_setting_page( self, page_name ):
        publicPage = PublicPage(self.driver)
        link_loc = self.driver.find_element_by_link_text(page_name)
        publicPage.click_elem(link_loc)
