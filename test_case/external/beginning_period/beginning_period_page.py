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
        :param btn_name: 按钮名称，可选值（start,edit,import)
        :return: 点击 '启用帐套''编辑'、'导入'按钮
        """
        publicPage = PublicPage( self.driver )
        if btn_name == 'start':
            btn_elem = start_btn_elem
        elif btn_name == 'edit':
            btn_elem = edit_btn_elem
        elif btn_name == 'import':
            btn_elem = import_btn_elem
        publicPage.click_elem( btn_elem )
    
    def import_initial_account( self , file_path ):
        """
        :param file_path:
        :return:
        """
        publicPage = PublicPage( self.driver )
        self.click_btn( 'edit' )
        WebDriverWait( self.driver , 30 , 1 ).until_not(
            lambda x: self.driver.find_element_by_id( 'fileUploadBtn' ).is_displayed() )
        uploadFilePage = UploadFilePage( self.driver , file_path )
        uploadFilePage.upload_file()
