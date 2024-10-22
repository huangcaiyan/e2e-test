import time
from selenium.common.exceptions import NoSuchElementException
import traceback,logging

from util.public_page import PublicPage
from .record_invoice_elem import *


# 记发票测试
# 创建于2017-10-17-周三
# caicai


class RecordInvoicePage:
	"""记发票测试"""
	def __init__(self, driver, base_url, invoice_io):
		"""
		:param driver:
		:param base_url: 主页地址
		:param invoice_io: 页面类型，可选值（input，output）
		"""
		# self.driver = webdriver.Chrome()
		self.driver = driver
		self.base_url = base_url
		self.invoice_io = invoice_io
	
	def go_to_record_invoice_page(self):
		if self.invoice_io == 'input':
			page_name = '记收票页面'
		elif self.invoice_io == 'output':
			page_name = '记开票页面'
		else:
			return 'error'
		page_url = self.base_url + '/app/invoice/detail/new-' + self.invoice_io + '-invoice'
		time.sleep(3)
		self.driver.get(page_url)
		page_url = self.driver.current_url
		if self.invoice_io in page_url:
			print('[RecordInvoicePage]－－－－－－成功进入' +
				  page_name + '－－－－－－\n当前url是=>', page_url)
		else:
			print('[RecordInvoicePage]－－－－－－去' + page_name + ' 失败－－－－－－')
			self.driver.quit()
	
	def select_invoice_type(self, invoice_type):
		"""
		:param invoice_type: 可选值（专票、普票、无票）
		"""
		global invoice_type_define
		invoice_type_define = invoice_type
		try:
			public_page = PublicPage(self.driver)
			is_disapeared = public_page.wait_until_loader_disapeared()
			if not is_disapeared:
				drop_loc = self.driver.find_element_by_xpath(
					record_invoice_base_xpath + self.invoice_io + invoice_type_drop_elem)
				public_page.select_dropdown_item(drop_loc, invoice_type)
				time.sleep(1)
		except NoSuchElementException as e:
			logging.error('查找的页面元素不存在，异常堆栈信息：'+str(traceback.format_exc()))
		
		except Exception as e:
			print('[RecordInvoicePage] －－选择发票类型失败－－失败原因是->', str(e))
			self.driver.quit()
	
	def select_invoice_status(self, invoice_status):
		"""
		:param invoice_status: 选择发票状态，可选值(税控自开，税务代开)
		"""
		try:
			publicPage = PublicPage(self.driver)
			drop_loc = self.driver.find_element_by_xpath(
				record_invoice_base_xpath + self.invoice_io + invoice_status_drop_elem)
			publicPage.select_dropdown_item(drop_loc, invoice_status)
		except Exception as e:
			print('[RecordInvoicePage]－－选择发票状态失败－－失败原因是->', str(e))
			self.driver.quit()
	
	def select_contact(self, contact):
		"""
		:param contact: 对方信息名
		"""
		try:
			if self.invoice_io == 'input':
				contact_drop_elem = input_contact_drop_elem
			elif self.invoice_io == 'output':
				contact_drop_elem = output_contact_drop_elem
			publicPage = PublicPage(self.driver)
			drop_loc = self.driver.find_element_by_xpath(
				record_invoice_base_xpath + self.invoice_io + contact_drop_elem)
			publicPage.select_dropdown_item(drop_loc, contact)
		except Exception as e:
			print('[RecordInvoicePage]－－选择对方信息失败－－失败原因是->', str(e))
			self.driver.quit()
	
	def set_invoice_num(self, invoice_num):
		"""
		:param invoice_num: 发票号
		"""
		try:
			if self.invoice_io == 'input':
				invice_num_elem = input_invoice_num_elem
			elif self.invoice_io == 'output':
				invice_num_elem = output_invoice_num_elem
			publicPage = PublicPage(self.driver)
			input_loc = self.driver.find_element_by_xpath(
				record_invoice_base_xpath + self.invoice_io + invice_num_elem)
			publicPage.set_value(input_loc, invoice_num)
		except Exception as e:
			print('[RecordInvoicePage]－－填写发票号失败－－失败原因是->', str(e))
			self.driver.quit()
	
	def select_category(self, category):
		"""
		:param category: 发票类别名
		"""
		try:
			publicPage = PublicPage(self.driver)
			print(self.category_index(category))
			p_index = self.category_index(category)[0]
			c_index = self.category_index(category)[1]
			
			drop_loc = self.driver.find_element_by_xpath(
				record_invoice_base_xpath + self.invoice_io + category_drop_elem)
			publicPage.click_elem(drop_loc)
			
			parent_loc = self.driver.find_elements_by_css_selector(parent_elem)[
				p_index]
			publicPage.click_elem(parent_loc)
			
			child_loc = self.driver.find_elements_by_css_selector(child_elem)[
				c_index]
			return publicPage.click_elem(child_loc)
		except Exception as e:
			print('[RecordInvoicePage]－－选择类别失败－－失败原因是->', str(e))
			self.driver.quit()
	
	def select_department(self, department):
		"""
		:param department: 部门名
		"""
		try:
			publicPage = PublicPage(self.driver)
			drop_loc = self.driver.find_element_by_xpath(
				record_invoice_base_xpath + self.invoice_io + department_drop_elem)
			publicPage.select_dropdown_item(drop_loc, department)
		except Exception as e:
			print('[RecordInvoicePage]－－选择部门名称失败－－失败原因是->', str(e))
	
	def select_tax_rate(self, tax_rate):
		"""
		:param tax_rate: 税率
		"""
		try:
			publicPage = PublicPage(self.driver)
			drop_loc = self.driver.find_element_by_xpath(
				record_invoice_base_xpath + self.invoice_io + tax_rate_drop_elem)
			publicPage.select_dropdown_item(drop_loc, tax_rate)
		except Exception as e:
			print('[RecordInvoicePage]－－选择税率失败－－失败原因是->', str(e))
			self.driver.quit()
	
	def select_input_tax_category(self, input_tax_category):
		"""
		:param input_tax_category: 进项税类别
		"""
		try:
			publicPage = PublicPage(self.driver)
			drop_loc = self.driver.find_element_by_xpath(
				record_invoice_base_xpath + self.invoice_io + input_tax_category_drop_elem)
			publicPage.select_dropdown_item(drop_loc, input_tax_category)
		except Exception as e:
			print('[RecordInvoicePage]－－选择进项税类别失败－－失败原因是->', str(e))
			self.driver.quit()
	
	def set_total(self, total):
		"""
		:param total: 价税合计
		"""
		try:
			if self.invoice_io == 'input' and invoice_type_define == '专票':
				total_elem = special_total_elem
			else:
				total_elem = general_total_elem
			publicPage = PublicPage(self.driver)
			input_loc = self.driver.find_element_by_xpath(
				record_invoice_base_xpath + self.invoice_io + total_elem)
			publicPage.set_value(input_loc, total)
		except Exception as e:
			print('[RecordInvoicePage]－－设置价税合计失败－－失败原因是->', str(e))
			self.driver.quit()
	
	def set_attachment(self, attachment):
		"""
		:param attachment: 备注
		"""
		try:
			if self.invoice_io == 'input' and invoice_type_define == '专票':
				attachment_elem = special_attachment_elem
			else:
				attachment_elem = general_attachment_elem
			publicPage = PublicPage(self.driver)
			input_loc = self.driver.find_element_by_xpath(
				record_invoice_base_xpath + self.invoice_io + attachment_elem)
			publicPage.set_value(input_loc, attachment)
		except Exception as e:
			print('[RecordInvoicePage]－－设置备注失败－－失败原因是->', str(e))
			self.driver.quit()
	
	def submit(self, btn_name):
		"""
		:param btn_name: 按钮名，可选值（save_and_new，save，cancel）
		:return: 保存并新增，保存，取消
		"""
		try:
			if btn_name == 'save_and_new':
				btn_elem = save_and_new_btn_elem
				submit_name = '保存并新增'
			elif btn_name == 'save':
				btn_elem = save_btn_elem
				submit_name = '保存'
			elif btn_name == 'cancel':
				btn_elem = cancel_btn_elem
				submit_name = '取消'
			publicPage = PublicPage(self.driver)
			btn_loc = self.driver.find_element_by_xpath(
				record_invoice_base_xpath + self.invoice_io + btn_elem)
			publicPage.click_elem(btn_loc)
		except Exception as e:
			print('[RecordInvoicePage]－－' +
				  submit_name + '失败－－失败原因是->', str(e))
			self.driver.quit()
	
	def record_invoice(self, invoice_data):
		if self.invoice_io == 'input':
			self.record_input_invoice(invoice_data)
		elif self.invoice_io == 'output':
			self.record_output_invoice(invoice_data)
		else:
			print('invoice_io=>', self.invoice_io)
			print('[RecordInvoicePage]－－函数调用失败－－')
			self.driver.quit()
	
	def record_input_invoice(self, invoice_data):
		"""
		:param invoice_data: 记收票信息
		"""
		publicPage = PublicPage(self.driver)
		invoice_num = str(publicPage.eight_random_nums())
		self.select_invoice_type(invoice_data[0])
		self.select_contact(invoice_data[1])
		if invoice_type_define == '专票':
			self.set_invoice_num(invoice_data[2] + invoice_num)
		self.select_category(invoice_data[3])
		self.select_department(invoice_data[4])
		self.select_tax_rate(invoice_data[5])
		if invoice_type_define == '专票':
			self.select_input_tax_category(invoice_data[6])
		self.set_total(invoice_data[7])
		self.set_attachment(invoice_data[8])
	
	def record_output_invoice(self, invoice_data):
		"""
		:param invoice_data: 记开票信息（只适用于一般纳税人）
		"""
		publicPage = PublicPage(self.driver)
		invoice_num = str(publicPage.eight_random_nums())
		self.select_invoice_type(invoice_data[0])
		self.select_invoice_status(invoice_data[1])
		self.select_contact(invoice_data[2])
		if invoice_data[0] == '专票' or invoice_type_define == '普票':
			self.set_invoice_num(invoice_data[3] + invoice_num)
		self.select_category(invoice_data[4])
		self.select_department(invoice_data[5])
		self.select_tax_rate(invoice_data[6])
		self.set_total(invoice_data[7])
		self.set_attachment(invoice_data[8])

	def record_output_invoice_xgm( self, invoice_data ):
		"""
		:param invoice_data: 记开票信息(只适用于小规模）
		"""
		self.select_invoice_type(invoice_data[0])
		self.select_invoice_status(invoice_data[1])
		self.select_contact(invoice_data[2])
		self.select_category(invoice_data[3])
		self.select_department(invoice_data[4])
		self.select_tax_rate(invoice_data[5])
		self.set_total(invoice_data[6])
		self.set_attachment(invoice_data[7])


	def category_index(self, category):
		"""
		类别转义
		:param category: 类别名称
		"""
		try:
			if self.invoice_io == 'input':
				if category == '福利费':
					p_c_arr = [0, 0]
					return p_c_arr
				elif category == '劳务费':
					p_c_arr = [0, 1]
					return p_c_arr
				elif category == '招待费':
					p_c_arr = [1, 0]
					return p_c_arr
				elif category == '办公费':
					p_c_arr = [1, 1]
					return p_c_arr
				elif category == '快递费':
					p_c_arr = [1, 2]
					return p_c_arr
				elif category == '通讯费':
					p_c_arr = [1, 3]
					return p_c_arr
				elif category == '维修费':
					p_c_arr = [1, 4]
					return p_c_arr
				elif category == '财产保险费':
					p_c_arr = [1, 5]
					return p_c_arr
				elif category == '设备租赁费':
					p_c_arr = [1, 6]
					return p_c_arr
				elif category == '银行费用':
					p_c_arr = [1, 7]
					return p_c_arr
				elif category == '差旅费':
					p_c_arr = [2, 0]
					return p_c_arr
				elif category == '交通费':
					p_c_arr = [2, 1]
					return p_c_arr
				elif category == '汽油费':
					p_c_arr = [2, 2]
					return p_c_arr
				elif category == '路桥费':
					p_c_arr = [2, 3]
					return p_c_arr
				elif category == '汽车维修费':
					p_c_arr = [2, 4]
					return p_c_arr
				elif category == '汽车保险费':
					p_c_arr = [2, 5]
					return p_c_arr
				elif category == '物流费':
					p_c_arr = [2, 6]
					return p_c_arr
				elif category == '房租费':
					p_c_arr = [3, 0]
					return p_c_arr
				elif category == '物业费':
					p_c_arr = [3, 1]
					return p_c_arr
				elif category == '水费':
					p_c_arr = [3, 2]
					return p_c_arr
				elif category == '电费':
					p_c_arr = [3, 3]
					return p_c_arr
				elif category == '仓储费':
					p_c_arr = [3, 4]
					return p_c_arr
				elif category == '装修费':
					p_c_arr = [3, 5]
					return p_c_arr
				elif category == '广告费':
					p_c_arr = [4, 0]
					return p_c_arr
				elif category == '宣传费':
					p_c_arr = [4, 1]
					return p_c_arr
				elif category == '研发费':
					p_c_arr = [4, 2]
					return p_c_arr
				elif category == '会议费':
					p_c_arr = [4, 3]
					return p_c_arr
				elif category == '服务费':
					p_c_arr = [4, 4]
					return p_c_arr
				elif category == '咨询费':
					p_c_arr = [4, 5]
					return p_c_arr
				elif category == '认证费':
					p_c_arr = [4, 6]
					return p_c_arr
				elif category == '专利费':
					p_c_arr = [4, 7]
					return p_c_arr
				elif category == '工会经费':
					p_c_arr = [4, 8]
					return p_c_arr
				elif category == '其他':
					p_c_arr = [4, 9]
					return p_c_arr
				elif invoice_type_define == '普票':
					if category == '行政罚款':
						p_c_arr = [5, 0]
						return p_c_arr
					elif category == '税务滞纳金':
						p_c_arr = [5, 1]
						return p_c_arr
					elif category == '印花税':
						p_c_arr = [6, 0]
						return p_c_arr
					elif category == '残保金':
						p_c_arr = [6, 1]
						return p_c_arr
					elif category == '减免税款':
						p_c_arr = [6, 2]
						return p_c_arr
					elif category == '原材料':
						p_c_arr = [7, 0]
						return p_c_arr
					elif category == '商品产品':
						p_c_arr = [7, 1]
						return p_c_arr
				elif invoice_type_define == '专票':
					if category == '原材料':
						p_c_arr = [5, 0]
						return p_c_arr
					elif category == '商品产品':
						p_c_arr = [5, 1]
						return p_c_arr
			elif self.invoice_io == 'output':
				if category == '商品销售':
					p_c_arr = [0, 0]
					return p_c_arr
				elif category == '服务收入':
					p_c_arr = [1, 0]
					return p_c_arr
			else:
				return 'Error'
		except Exception as e:
			print('[RecordInvoicePage]－－－发票类别转义失败－－－失败原因是->', str(e))
