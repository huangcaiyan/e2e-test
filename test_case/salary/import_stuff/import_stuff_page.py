from selenium import webdriver
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
import time
from util.upload_file_page import UploadFilePage


# 导入员工
# 创建于2017-09-27-三
# caicai

class ImportStuffPage(object):
	
	def __init__(self, driver):
		# self.driver = webdriver.Chrome()
		self.driver = driver
	
	def go_to_stuff_import_page(self, base_url):
		self.driver.get(base_url + '/app/salary/stuff-import')
	
	def upload_stuff_file(self, stuff_file_path):
		uploadFilePage = UploadFilePage(self.driver, stuff_file_path)
		uploadFilePage.upload_file()
