from selenium import webdriver
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
import unittest


# 导入员工
# 创建于2017-09-27-三
# caicai

class ImportStuffSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


if __name__ == '_main_':
    unittest.main()
