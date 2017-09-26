from selenium import webdriver
import unittest
import time
from .add_stuff_page import AddStuffPage
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo
from test_case.salary.salary_page import SalaryPage 
from test_data.cai.add_stuff_data import *

class AddStuffSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        enterCompPage = EnterCompPage(CompInfo.BASE_URL,self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO_YB)

    def test_name_empty(self):
        """添加员工－员工名称为空－红框警示，保存失败"""
        salaryPage = SalaryPage(self.driver)
        salaryPage.go_to_add_stuff_page()
        print('url=>',self.driver.current_url)
        page = AddStuffPage(self.driver)
        page.set_name(stuff_name)
        page.save()
        result = page.has_danger_is_show()
        # time.sleep(2)
        print('result=>',result)
        self.assertEqual(result,1)

    def tearDown(self):
        self.driver.quit()

if __name__ == '_main_':
    unittest.main()
        
        
        