from selenium import webdriver
import unittest
import time

from util.public_page import PublicPage

# @Time :18/1/22 上午11:20
# @Author :huangcaiyan
# @File : topbar_elem
# @Software : PyCharm

# 登陆用户名字
account_company_name_elem = '//*[@id="wrapper"]/navbar/div/nav/div/div[2]/div/div/span'
# 登陆用户名字
login_user_name_elem = '//*[@id="wrapper"]/navbar/div/nav/div/div[3]/a/span'
# ----------------------------------------------------------------------------------------------------------------------
# 帐套名称xpaht
comp_name_elem = '//*[@id="CompanyDropdownMenu"]/a/i'
# 当前会计期间xpath
accounting_period_elem = '//*[@id="wrapper"]/navbar/div/nav/div/div[2]/div'
# ----------------------------------------------------------------------------------------------------------------------
# 操作按钮下拉xpath
operation_drop_elem = '//*[@id="wrapper"]/navbar/div/nav/div/div[3]/button[1]'
# 下拉可选值 class
operation_item_elem = '.dropdown-item'
