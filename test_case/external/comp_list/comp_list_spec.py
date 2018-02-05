from selenium import webdriver
import unittest,time

from .comp_list_page import CompListPage
from util.public_page import PublicPage
from ...login.login_page import LoginPage
from comp_info import CompInfo


# @Time :18/1/19 上午11:46
# @Author :huangcaiyan
# @File : comp_list_page
# @Software : PyCharm
class CompListSpec( unittest.TestCase ):
    comp_info = [ None ]
    
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
    
    # def test_distribute_accounting( self ):
    #     page = CompListPage( self.driver )
    #     page.distribute_accounting( '固定yk' )
    #
    # name_list()
    
    def test_enter_comp( self ):
        page = CompListPage( self.driver )
        page.enter_comp()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
