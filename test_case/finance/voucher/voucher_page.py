from selenium import webdriver
from time import sleep

class VoucherPage(object):

    def __init__(self,driver):
        self.driver = driver

    #进入凭证列表页面
    def goToVoucherListPage(self,url):
        self.driver.get(url)
        sleep(3)