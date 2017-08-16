from selenium import webdriver
from time import sleep
import sys
import os
# sys.path.append('F:\\autoTest_workspace\\python_code\\e2e-test\\test_case\\login')
# from login_page import LoginPage

class ImportStaffFile(object):
    '''导入员工'''
    def __init__(self,driver):
        self.driver = driver

    #进入员工导入页面
    def goToImportStaffPage(self,url):
        self.driver.get(url + '/app/salary/stuff-import')
        sleep(2)

    #导入员工文件
    def importStaffFile(self,file):
        uploadInputLocator = 'fileUploadBtn'
        self.driver.find_element_by_id(uploadInputLocator).send_keys(file)
        sleep(3)

# driver = webdriver.Chrome()
# driver.get('https://firms.guanplus.com')
# login = LoginPage('https://firms.guanplus.com',driver)
# login.login(['18514509382','qq123456'])
# sleep(5)
# driver.find_element_by_link_text('滴滴答答').click()
# sleep(5)
# im = ImportStaffFile(driver)
# im.goToImportStaffPage('https://firms.guanplus.com')
# sleep(2)
# im.importStaffFile('F:\\autoTest_workspace\\python_code\\e2e-test\\test_data\\导入员工.xlsx')
# driver.quit()
# print('ssssss')