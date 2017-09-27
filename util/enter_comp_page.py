from selenium import webdriver
import time
from test_case.login.login_page import LoginPage
from .public_page import PublicPage
from .enter_comp_elem import *

class EnterCompPage:

    # location
    create_comp_xpath = '//*[@id="body"]/company-list/div[1]/div[3]/div[2]/button[1]'

    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    def get_comp_name(self, comp_name):
        current_comp_name_loc = self.driver.find_element_by_link_text(
            comp_name)
        return current_comp_name_loc.text

    # 进入公司
    # comp_name 公司名称
    def enter_comp(self, enter_comp_info):
        loginPage = LoginPage(self.url, self.driver)
        loginPage.login(enter_comp_info[0])
        comp_name_loc = self.driver.find_element_by_link_text(
            enter_comp_info[1])
        comp_name_loc.click()
        time.sleep(5)
        page_url = self.driver.current_url
        if 'home-page' in page_url :
            print('进入帐套成功！当前帐套名称为： ',self.get_comp_name(enter_comp_info[1]))
        else:
            print('————————————进入公司失败 ！————————————')
