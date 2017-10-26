from selenium import webdriver
import time
from .salary_elem import *
from util.enter_comp_page import EnterCompPage
from comp_info import CompInfo

# 薪资导航
# 创建于2017-09-21-四
# caicai


class SalaryPage(object):

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 去员工管理页面
    def go_to_stuff_list_page(self):
        stuff_list_page_url = CompInfo.BASE_URL+stuff_list_url
        self.driver.get(stuff_list_page_url)
        time.sleep(3)
        if self.driver.current_url == stuff_list_page_url:
            print('员工管理页面：')
        else:
            print('[SalaryPage]＝＝＝＝＝＝去员工管理页面失败！＝＝＝＝＝＝')

    # 去添加员工页面
    def go_to_add_stuff_page(self):
        add_stuff_page_url = CompInfo.BASE_URL + add_stuff_url
        self.driver.get(add_stuff_page_url)
        time.sleep(3)
        if self.driver.current_url ==  add_stuff_page_url:
            print('添加员工页面：')
        else:
            print('[SalaryPage]＝＝＝＝＝＝去添加员工页面失败！＝＝＝＝＝＝')


    # 去导入员工页面
    def go_to_import_stuff_page(self):
        import_stuff_page_url = CompInfo.BASE_URL + import_stuff_url
        self.driver.get(import_stuff_page_url)
        time.sleep(3)
        if self.driver.current_url ==  import_stuff_page_url:
            print('导入员工页面：')
        else:
            print('[SalaryPage]＝＝＝＝＝＝去导入员工页面失败！＝＝＝＝＝＝')



    # 去工资表页面
    def go_to_salary_sheet_page(self):
        salary_sheet_page_url = CompInfo.BASE_URL + salary_sheet_url
        self.driver.get(salary_sheet_page_url)
        time.sleep(3)
        if self.driver.current_url ==  salary_sheet_page_url:
            print('工资表页面：')
        else:
            print('[SalaryPage]＝＝＝＝＝＝去工资表页面失败！＝＝＝＝＝＝')



    # 去劳务表页面
    def go_to_labour_sheet_page(self):
        labour_sheet_page_url = CompInfo.BASE_URL + labour_sheet_url
        self.driver.get(labour_sheet_page_url)
        time.sleep(3)
        if self.driver.current_url ==  labour_sheet_page_url:
            print('劳务表页面：')
        else:
            print('[SalaryPage]＝＝＝＝＝＝去劳务表页面失败！＝＝＝＝＝＝')


    # 去工资表导入页面
    def go_to_salary_import_page(self):
        salary_import_page_url = CompInfo.BASE_URL + salary_sheet_url
        self.driver.get(salary_import_page_url)
        time.sleep(3)
        if self.driver.current_url ==  salary_import_page_url:
            print('工资表导入页面：')
        else:
            print('[SalaryPage]＝＝＝＝＝＝去工资表导入页面失败！＝＝＝＝＝＝')



    # 去劳务表导入页面
    def go_to_labour_import_page(self):
        labour_import_page_url = CompInfo.BASE_URL + labour_import_url
        self.driver.get(labour_import_page_url)
        time.sleep(3)
        if self.driver.current_url ==  labour_import_page_url:
            print('劳务表导入页面：')
        else:
            print('[SalaryPage]＝＝＝＝＝＝去劳务表导入页面失败！＝＝＝＝＝＝')



    # 去工资发放记录页面
    def go_to_salary_record_page(self):
        salary_record_page_url = CompInfo.BASE_URL + salary_record_url
        self.driver.get(salary_record_page_url)
        time.sleep(3)
        if self.driver.current_url ==  salary_record_page_url:
            print('工资发放记录页面：')
        else:
            print('[SalaryPage]＝＝＝＝＝＝去工资发放记录页面失败！＝＝＝＝＝＝')


    # 去劳务发放记录页面
    def go_to_labour_record_page(self):
        labour_record_page_url = CompInfo.BASE_URL + labour_record_url
        self.driver.get(labour_record_page_url)
        time.sleep(3)
        if self.driver.current_url ==  labour_record_page_url:
            print('劳务发放记录页面：')
        else:
            print('[SalaryPage]＝＝＝＝＝＝去劳务发放记录页面失败！＝＝＝＝＝＝')

