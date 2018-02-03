from selenium import webdriver
from .create_ways_elem import *
from util.public_page import PublicPage


class CreateWaysPage:
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    def set_comp_name(self, comp_name):
        """
        :param comp_name:帐套名称
        """
        publicPage = PublicPage(self.driver)
        if comp_name == '':
            name = comp_name
        else:
            name = publicPage.random_num(10000) + comp_name
        comp_name_input_loc = self.driver.find_element_by_xpath(comp_name_input_elem)
        publicPage.set_value(comp_name_input_loc, name)

    def confirm_enter(self):
        """
        :return:点击回车
        """
        publicPage = PublicPage(self.driver)
        comp_name_input_loc = self.driver.find_element_by_xpath(comp_name_input_elem)
        publicPage.keys_enter(comp_name_input_loc)
        if not publicPage.wait_until_loader_disapeared():
            print('页面跳转成功！')
        else:
            print('页面跳转失败！')

    def back_to_comp_list_page(self):
        """
        :return:点击返回到帐套列表页面
        """
        publicPage = PublicPage(self.driver)
        link_loc = self.driver.find_element_by_link_text('帐套')
        publicPage.click_elem(link_loc)
