from selenium import webdriver
import sys
import os
import time

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
import unittest

from .import_stuff_page import ImportStuffPage
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo


# 导入员工
# 创建于2017-09-27-三
# caicai

class ImportStuffSpec(unittest.TestCase):
	print("path=", os.path.abspath(os.path.dirname(__file__)))
	stuff_file_path = '/Users/doghome/Test/e2e-test/test_data/cai/salary/导入员工－yb.xlsx'
	
	def setUp(self):
		self.driver = webdriver.Chrome()
		# self.driver = webdriver.PhantomJS()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		
		enterCompPage = EnterCompPage(self.driver)
		enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)
	
	def tearDown(self):
		self.driver.quit()
	
	def test_upload_file(self):
		"""测试 导入员工"""
		page = ImportStuffPage(self.driver)
		page.go_to_stuff_import_page(CompInfo.BASE_URL)
		time.sleep(2)
		page.upload_stuff_file(self.stuff_file_path)
		time.sleep(10)


if __name__ == '_main_':
	unittest.main()
