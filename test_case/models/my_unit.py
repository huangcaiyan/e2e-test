from selenium import webdriver
from .driver import browser
import unittest
import os


# 定义测试框架类
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


class MyTestClass(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = browser()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        self.driver.quit()
