from selenium import webdriver
import time
from transaction_list_elem import *

class TransactionListPage(object):

    def __init__(self,driver):
        self.driver = webdriver.Chrome()
        # self.driver = driver


    