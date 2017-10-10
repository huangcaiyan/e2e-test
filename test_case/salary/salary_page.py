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
        self.driver.get(CompInfo.BASE_URL + stuff_list_url)
        time.sleep(3)

    # 去添加员工页面
    def go_to_add_stuff_page(self):
        self.driver.get(CompInfo.BASE_URL + add_stuff_url)
        time.sleep(3)

    # 去导入员工页面
    def go_to_import_stuff_page(self):
        self.driver.get(CompInfo.BASE_URL + import_stuff_url)
        time.sleep(3)

    # 去工资表页面
    def go_to_salary_sheet_page(self):
        self.driver.get(CompInfo.BASE_URL + salary_sheet_url)
        time.sleep(3)

    # 去劳务表页面
    def go_to_labour_sheet_page(self):
        self.driver.get(CompInfo.BASE_URL + labour_sheet_url)
        time.sleep(3)

    # 去工资表导入页面
    def go_to_salary_import_page(self):
        self.driver.get(CompInfo.BASE_URL + salary_sheet_url)
        time.sleep(3)

    # 去劳务表导入页面
    def go_to_labour_import_page(self):
        self.driver.get(CompInfo.BASE_URL + labour_import_url)
        time.sleep(3)

    # 去工资发放记录页面
    def go_to_salary_record_page(self):
        self.driver.get(CompInfo.BASE_URL + salary_record_url)
        time.sleep(3)

    # 去劳务发放记录页面
    def go_to_labour_record_page(self):
        self.driver.get(CompInfo.BASE_URL + labour_record_url)
        time.sleep(3)
