import platform
from selenium import webdriver


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
