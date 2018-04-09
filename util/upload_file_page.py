from selenium import webdriver
import time
import unittest
from util.public_page import PublicPage


class UploadFilePage(object):
	def __init__(self, driver, file_dir):
		# self.driver = webdriver.Chrome()
		# self.driver = driver
		self.file_dir = file_dir
	
	def upload_file(self):
		publicPage = PublicPage(self.driver)
		upload_btn_loc = self.driver.find_element_by_id('fileUploadBtn')
		publicPage.is_element_present(upload_btn_loc)
		upload_btn_loc.send_keys(self.file_dir)
	# time.sleep(5)
