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
	
	def __init__(self, driver):
		self.driver = driver  # self.driver = webdriver.Chrome()
	
	# ------------------------------------------------------------------------------------------------------------------
	
	# 按钮
	def click_btn(self, btn_name):
		"""
		:param btn_name: 按钮名称，可选值（start,edit,import)
		:return: 点击 '启用帐套''编辑'、'导入'按钮
		"""
		publicPage = PublicPage(self.driver)
		if btn_name == 'start':
			btn_elem = start_btn_elem
		elif btn_name == 'edit':
			btn_elem = edit_btn_elem
		elif btn_name == 'import':
			btn_elem = import_btn_elem
		publicPage.click_elem(btn_elem)
	
	def go_to_upload_initial_account_page(self, base_url):
		"""
		:param base_url: 环境url
		:return: 页面跳转至导入期初账页面；
		"""
		self.driver.get(base_url + '/app/finance/import')
	
	def import_initial_account(self, file_path):
		"""
		:param file_path:期初账导入文件地址
		:return:导入期初账
		"""
		WebDriverWait(self.driver, 30, 1).until_not(
			lambda x: self.driver.find_element_by_id('fileUploadBtn').is_displayed())
		uploadFilePage = UploadFilePage(self.driver, file_path)
		uploadFilePage.upload_file()
	
	def distribute_initial_account(self):
		"""
		:return:期初分配
		"""
