from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait

from util.public_page import PublicPage
from .beginning_period_elem import *
from util.upload_file_page import UploadFilePage


# @Time :18/2/1 下午5:32
# @Author :huangcaiyan
# @File : beginning_period_page
# @Software : PyCharm


class BeginningPeriodPage:
    
    def __init__( self , driver ):
        self.driver = driver  # self.driver = webdriver.Chrome()
        
        # ------------------------------------------------------------------------------------------------------------------
    
    # 按钮
    def click_btn( self , btn_name ):
        """
        :param btn_name: 按钮名称，可选值（启用期初帐,编辑,导入)
        :return: 点击 '启用帐套''编辑'、'导入'按钮
        """
        publicPage = PublicPage( self.driver )
        if btn_name == '启用期初帐':
            btn_elem = start_btn_elem
        elif btn_name == '编辑':
            btn_elem = edit_btn_elem
        elif btn_name == '导入':
            btn_elem = import_btn_elem
        btn_loc = self.driver.find_element_by_xpath( btn_elem )
        publicPage.click_elem( btn_loc )
    
    def import_initial_account( self , file_path ):
        """
        :param file_path:
        :return:
        """
        self.click_btn( '导入' )
        # WebDriverWait( self.driver , 30 , 1 ).until_not(
        #     lambda x: self.driver.find_element_by_id( 'fileUploadBtn' ).is_displayed() )
        uploadFilePage = UploadFilePage( self.driver )
        uploadFilePage.upload_file( file_path )
