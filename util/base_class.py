<<<<<<< HEAD
import platform
=======
import unittest
>>>>>>> f0d2c843669e5d27aaaabf803bdbe17b8112a2b2
from selenium import webdriver

from util.public_page import PublicPage
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo

<<<<<<< HEAD
class BaseClass:
	def __init__(self,driver):
		self.driver = driver
	
	@staticmethod
	def get_system_name():
		running_system = platform.system()
		print("system=>", running_system)
		if running_system == 'Darwin':
			current_system_name = 'Mac'
		elif running_system == 'Windows':
			current_system_name = 'Windows'
		else:
			current_system_name = 'others'
			print('自动化测试程序在 非Mac 或 windows 机器上运行！')
		return current_system_name
		
	# 在windows上浏览器最大化
	def max_window(self):
		if self.get_system_name() == 'Windows':
			self.driver.maximize_window()
=======

class BaseClass(unittest.TestCase):
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        publicPage = PublicPage(self.driver)
        publicPage.max_window()

        self.driver.implicitly_wait(30)

        enterCompPage = EnterCompPage(self.driver)
        enterCompPage.enter_comp(CompInfo.ENTER_COMP_INFO)

    def tearDownClass(self):
        print('测试用例运行结束！')
        self.driver.quit()

>>>>>>> f0d2c843669e5d27aaaabf803bdbe17b8112a2b2
