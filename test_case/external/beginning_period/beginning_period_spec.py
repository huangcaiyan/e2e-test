from selenium import webdriver
import unittest
import time
import sys
import os

from util.public_page import PublicPage
from ...login.login_page import LoginPage
from comp_info import CompInfo
from ..comp_list.comp_list_page import CompListPage
from ..comp_list.distribute_modal.distribute_modal_page import DistributeModalPage
from .beginning_period_page import BeginningPeriodPage


# @Time :18/2/1 下午5:32
# @Author :huangcaiyan
# @File : beginning_period_spec
# @Software : PyCharm


class BeginningPeriodSpec( unittest.TestCase ):
    # ｛角色，帐套名称，会计名称，会计手机号｝
    user_info = [ '会计' , None , 'current_user' , '' ]
    initial_account_import_data_path ='/Users/huangcaiyan/work/e2e-test/test_data/cai/external/导入期初帐.xlsx'
    
    @classmethod
    def setUpClass( self ):
        self.driver = webdriver.Chrome()
        publicPage = PublicPage( self.driver )
        publicPage.max_window()
        self.driver.implicitly_wait( 30 )
        
        loginPage = LoginPage( CompInfo.BASE_URL , self.driver )
        loginPage.login( CompInfo.LOGIN_DATA )
    
    @classmethod
    def tearDownClass( self ):
        self.driver.quit()
    
    def test_import_initial_account( self ):
        """测试 导入期初帐"""
        compListPage = CompListPage( self.driver )
        distributePage = DistributeModalPage( self.driver )
        page = BeginningPeriodPage( self.driver )
        distributePage.invite_user( self.user_info )
        time.sleep( 2 )
        compListPage.enter_comp()
        page.import_initial_account( self.initial_account_import_data_path )
        time.sleep(8)


if __name__ == '__main__':
    unittest.main()
