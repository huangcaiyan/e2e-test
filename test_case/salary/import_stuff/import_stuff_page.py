from selenium import webdriver
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
import time

# 导入员工
# 创建于2017-09-27-三
# caicai

class ImportStuffPage(object):

    def __init__(self,driver):
        # self.driver = webdriver.Chrome()        
        self.driver = driver