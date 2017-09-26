from selenium import webdriver

class Driver(object):

    def get_driver(self):
        driver = webdriver.Chrome()
        # driver = webdriver.PhantomJS()
        return driver