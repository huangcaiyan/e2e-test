import sys
import os
from selenium import webdriver
import unittest

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from .login_page import LoginPage
from comp_info import CompInfo
from util.danger_page import DangerPage
from util.read_excel import ReadExcel
from util.public_page import PublicPage

"""
登录测试
修改于2017-12-8-五
caicai
"""

base_dir = os.path.abspath(os.path.dirname(__file__) + '/../..')


class LoginSpec(unittest.TestCase):
	login_test_data_dir = base_dir + '/test_data/cai/login/login_test_data.xlsx'
	
	@classmethod
	def setUpClass(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		PublicPage(self.driver).max_window()
	
	@classmethod
	def tearDownClass(self):
		self.driver.quit()
	
	def test_verify_login(self):
		"""登录管有帐"""
		login_page = LoginPage(CompInfo.BASE_URL, self.driver)
		if 'dev' in CompInfo.BASE_URL:
			sheet_name = 'dev'
		elif 'stage' in CompInfo.BASE_URL:
			sheet_name = 'stage'
		elif 'firms' in CompInfo.BASE_URL:
			sheet_name = 'pro'
		
		read_excel = ReadExcel(self.login_test_data_dir)
		login_test_data = read_excel.get_value_by_row(sheet_name, 1)
		print('login_test_data=>', login_test_data)
		login_page.login(login_test_data)
		
		page_url = self.driver.current_url
		print('page_url=>', page_url)
		self.assertIn('/app/company-list', page_url, msg='登录验证失败！')
	
	def test_unexit_username(self):
		""" 登录测试－用户不存在 """
		login_page = LoginPage(CompInfo.BASE_URL, self.driver)
		danger_page = DangerPage(self.driver)
		read_excel = ReadExcel(self.login_test_data_dir)
		if 'dev' in CompInfo.BASE_URL:
			sheet_name = 0
		elif 'stage' in CompInfo.BASE_URL:
			sheet_name = 1
		elif 'firms' in CompInfo.BASE_URL:
			sheet_name = 2
		login_test_data = read_excel.get_value_by_row(sheet_name, 2)
		login_page.login(login_test_data)
		
		error_msg = danger_page.get_error_msg()
		self.assertEqual(error_msg, login_test_data[3], msg='登录测试－用户不存在，失败！')
	
	def test_wrong_password(self):
		""" 登录测试－密码不正确 """
		login_page = LoginPage(CompInfo.BASE_URL, self.driver)
		danger_page = DangerPage(self.driver)
		read_excel = ReadExcel(self.login_test_data_dir)
		if 'dev' in CompInfo.BASE_URL:
			sheet_name = 0
		elif 'stage' in CompInfo.BASE_URL:
			sheet_name = 1
		elif 'firms' in CompInfo.BASE_URL:
			sheet_name = 2
		login_test_data = read_excel.get_value_by_row(sheet_name, 3)
		login_page.login(login_test_data)
		
		error_msg = danger_page.get_error_msg()
		self.assertEqual(error_msg, login_test_data[3], msg='登录测试－密码不正确，失败！')
	
	def test_empty_username(self):
		""" 登录测试－用户名为空 """
		login_page = LoginPage(CompInfo.BASE_URL, self.driver)
		danger_page = DangerPage(self.driver)
		read_excel = ReadExcel(self.login_test_data_dir)
		if 'dev' in CompInfo.BASE_URL:
			sheet_name = 0
		elif 'stage' in CompInfo.BASE_URL:
			sheet_name = 1
		elif 'firms' in CompInfo.BASE_URL:
			sheet_name = 2
		login_test_data = read_excel.get_value_by_row(sheet_name, 4)
		login_page.login(login_test_data)
		
		input_alert_msg = danger_page.get_input_alert_msg()
		self.assertEqual(input_alert_msg, login_test_data[3], msg='登录测试－用户名为空,失败！')
	
	def test_empty_password(self):
		""" 登录测试－密码为空 """
		login_page = LoginPage(CompInfo.BASE_URL, self.driver)
		read_excel = ReadExcel(self.login_test_data_dir)
		if 'dev' in CompInfo.BASE_URL:
			sheet_name = 0
		elif 'stage' in CompInfo.BASE_URL:
			sheet_name = 1
		elif 'firms' in CompInfo.BASE_URL:
			sheet_name = 2
		login_test_data = read_excel.get_value_by_row(sheet_name, 5)
		login_page.login(login_test_data)
		
		input_alert_msg = login_page.get_input_error('password')
		self.assertEqual(input_alert_msg, login_test_data[3], msg='登录测试－密码为空,失败！')
	
	def test_typeerror_username(self):
		""" 登录测试－手机号码格式错误 """
		login_page = LoginPage(CompInfo.BASE_URL, self.driver)
		danger_page = DangerPage(self.driver)
		read_excel = ReadExcel(self.login_test_data_dir)
		if 'dev' in CompInfo.BASE_URL:
			sheet_name = 0
		elif 'stage' in CompInfo.BASE_URL:
			sheet_name = 1
		elif 'firms' in CompInfo.BASE_URL:
			sheet_name = 2
		login_test_data = read_excel.get_value_by_row(sheet_name, 6)
		login_page.login(login_test_data)
		
		input_alert_msg = danger_page.get_input_alert_msg()
		self.assertEqual(input_alert_msg, login_test_data[3], msg='登录测试－手机号码格式错误,失败！')


if __name__ == '__main__':
	unittest.main()
# login_test_data_dir = '../test_data/cai/login_test_data.xlsx'
# testCase = unittest.TestLoader().loadTestsFromTestCase(LoginSpec)
# suite = unittest.TestSuite()
# unittest.TextTestRunner(verbosity=2).run(suite)
