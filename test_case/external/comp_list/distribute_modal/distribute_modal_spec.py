from selenium import webdriver
import unittest,time

from .distribute_modal_page import DistributeModalPage
from comp_info import CompInfo
from util.public_page import PublicPage
# from util.enter_comp_page import EnterCompPage
from ....login.login_page import LoginPage
from ..comp_list_page import CompListPage


class DistributeModalSpec(unittest.TestCase):
    user_info = ['huangcaiyan0714','13683139989',]

    @classmethod
    def setUpClass( self ):
        self.driver = webdriver.Chrome()
        global publicPage
        publicPage = PublicPage(self.driver)
        publicPage.max_window()
        self.driver.implicitly_wait(30)

        loginPage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginPage.login(CompInfo.LOGIN_DATA)

    @classmethod
    def tearDownClass( self ):
        self.driver.quit()

    def test_distribute_accounting( self ):
        compListPage = CompListPage(self.driver)
        page = DistributeModalPage(self.driver)
        compListPage.click_distribute_btn('北京第一村', '会计')
        time.sleep(5)

        page.get_name_list()

    def test_distribute_current_user_accounting( self ):
        compListPage = CompListPage(self.driver)
        page = DistributeModalPage(self.driver)
        compListPage.click_distribute_btn('北京第一村','会计')
        page.distribute_user()







if __name__ == '__main__':
    unittest.main()
