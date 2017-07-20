import unittest
from selenium import webdriver


class RecordIncomeSpec(unittest.TestCase):
    def setUp(self):
        self.url = 'https://web-gyz-stage.guanplus.com'
        self.driver = webdriver.Chrome()

    def test1(self):

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
