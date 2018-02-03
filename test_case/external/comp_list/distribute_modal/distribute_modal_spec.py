from selenium import webdriver
import unittest , time

from .distribute_modal_page import DistributeModalPage
from comp_info import CompInfo
from util.public_page import PublicPage
# from util.enter_comp_page import EnterCompPage
from ....login.login_page import LoginPage
from ..comp_list_page import CompListPage
from ...navigation.topbar.topbar_page import TopBarPage


# @Time :18/1/19 上午11:46
# @Author :huangcaiyan
# @File : distribute_modal_spec
# @Software : PyCharm
class DistributeModalSpec( unittest.TestCase ):
    user_info = [ '小芳' , '13683139980' , ]
    
    @classmethod
    def setUpClass( self ):
        self.driver = webdriver.Chrome()
        global publicPage
        publicPage = PublicPage( self.driver )
        publicPage.max_window()
        self.driver.implicitly_wait( 30 )
        
        loginPage = LoginPage( CompInfo.BASE_URL , self.driver )
        loginPage.login( CompInfo.LOGIN_DATA )
    
    @classmethod
    def tearDownClass( self ):
        self.driver.quit()
    
    #
    def test_distribute_accounting( self ):
        compListPage = CompListPage( self.driver )
        page = DistributeModalPage( self.driver )
        compListPage.click_distribute_btn(  '会计','北京第一村'  )
        page.invite_user( self.user_info )
        time.sleep( 5 )
    
    
    #     page.get_name_list()
    #
    # def test_distribute_current_user_accounting( self ):
    #     compListPage = CompListPage(self.driver)
    #     page = DistributeModalPage(self.driver)
    #     compListPage.click_distribute_btn('北京第一村', '会计')
    #     topBarPage = TopBarPage(self.driver)
    #     current_user_name = topBarPage.get_login_user_name()
    #
    #     page.select_user(current_user_name)
    #     page.submit('save')
    #     time.sleep(2)
    #
    # def test_get_user_list( self ):
    #     compListPage = CompListPage(self.driver)
    #     page = DistributeModalPage(self.driver)
    #     compListPage.click_distribute_btn('北京第一村', '会计')
    #     page.get_name_list()
    
    # def test_get_phone_list( self ):
    #     compListPage = CompListPage( self.driver )
    #     page = DistributeModalPage( self.driver )
    #     compListPage.click_distribute_btn( '北京第一村' , '会计' )
    #     page.get_phone_list()
    
    #
    
    # def test_write_excel( self ):  #     """测试"""  #     file_name = 'data.xlsx'  #     topBarPage = TopBarPage(self.driver)  #     current_user_name = topBarPage.get_login_user_name()  #     topBarPage.write_data(current_user_name, file_name)


if __name__ == '__main__':
    unittest.main()
