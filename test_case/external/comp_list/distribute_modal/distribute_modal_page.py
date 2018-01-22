from selenium import webdriver
import time

from .distribute_modal_elem import *
from util.public_page import PublicPage
from ..comp_list_page import CompListPage


# @Time :18/1/19 上午11:46
# @Author :huangcaiyan
# @File : distribute_modal_page
# @Software : PyCharm
class DistributeModalPage(object):

    def __init__( self, driver ):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def distribute_current_user( self, user_info ):
        """
        :param user_info: 客户联系人／会计／助理信息（姓名）
        :return: 分配当前用户为会计／助理
        """
        if not self.driver.find_element_by_xpath(name_text_elem).is_displayed():
            self.click_add_more_link()
        # current_user_name =
        self.select_user(user_info[0])
        self.submit(user_info[2])

    def invite_new_user( self, user_info ):
        """
        :param user_info: 客户联系人／会计／助理信息（姓名、电话）
        :return: 填写客户联系人，邀请会计／助理
        """
        if not self.driver.find_element_by_xpath(name_text_elem).is_displayed():
            self.click_add_more_link()
        self.select_user('+新增用户')
        time.sleep(1)
        if self.driver.find_element_by_xpath(name_input_elem).is_displayed():
            self.set_name(user_info[0])
            self.set_phone(user_info[1])
            self.submit(user_info[2])

    def distribute_user( self, user_info ):
        # compListPage = CompListPage(self.driver)
        # compListPage.click_distribute_btn()
        if not self.driver.find_element_by_xpath(name_text_elem).is_displayed():
            self.click_add_more_link()
        if self.driver.find_element_by_xpath(name_text_elem) == '':
            self.select_user('+新增用户')
            self.set_name(user_info[0])
            self.set_phone(user_info[1])
        else:
            self.select_user(user_info[0])
        self.submit(user_info[2])

    # ------------------------------------------------------------------------------------------------------------------
    def select_user( self, name ):
        """
        :param name: 姓名;选择新增用户（name=+新增用户);
        :return:点击姓名下拉可选值
        """
        publicPage = PublicPage(self.driver)
        drop_loc = self.driver.find_element_by_xpath(name_drop_elem)
        publicPage.select_dropdown_item(drop_loc, name)

    def get_name_list( self ):
        publicPage = PublicPage(self.driver)
        # self.driver.find_element_by_xpath(name_text_elem).click()
        drop_loc = self.driver.find_element_by_xpath(name_drop_elem)
        publicPage.click_elem(drop_loc)
        name_locs = drop_loc.find_element_by_css_selector('.dropdown-menu').find_elements_by_tag_name('li')
        name_len = len(name_locs)
        print('name_len=', name_len)
        names = []
        for name_index in range(name_len):
            name_xpath = 'li[' + str(name_index) + ']/div/a/div/div'
            print('name_xpath=>',name_xpath)
            name_loc = self.driver.find_element_by_css_selector('.dropdown-menu').find_element_by_xpath(name_xpath)
            name = name_loc.text
            print('name=>', name)
            names.append(name)
            print('names1==', names)
        print('names=', names)
        return names

    def set_name( self, name ):
        """
        :param name: 姓名
        :return:输入姓名
        """
        publicPage = PublicPage(self.driver)
        input_loc = self.driver.find_element_by_xpath(name_input_elem)
        publicPage.set_value(input_loc, name)

    def set_phone( self, phone_num ):
        """
        :param phone_num: 手机号
        :return:输入手机号
        """
        publicPage = PublicPage(self.driver)
        input_loc = self.driver.find_element_by_xpath(phone_input_elem)
        publicPage.set_value(input_loc, phone_num)

    def click_add_more_link( self ):
        """
        :return: 点击继续添加
        """
        publicPage = PublicPage(self.driver)
        link_loc = self.driver.find_element_by_partial_link_text('继续添加')
        publicPage.click_elem(link_loc)

    def submit( self, btn_name ):
        """
        :param btn_name: 按钮名称，可选值(save,cancel)
        :return:点击保存、取消按钮
        """
        if btn_name == 'save':
            submit_elem = save_elem
        elif btn_name == 'cancel':
            submit_elem = cancel_elem
        publicPage = PublicPage(self.driver)
        btn_loc = self.driver.find_element_by_xpath(submit_elem)
        publicPage.click_elem(btn_loc)

# class Test(unittest.TestCase):
#     @classmethod
#     def setUpClass( self ):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(30)
#
#         loginPage = LoginPage()
#
#     @classmethod
#     def tearDownClass( self ):
#         self.driver.quit()
#
#     def test_get_name_list( self ):
#         page = DistributeModalPage(self.driver)
#         page
