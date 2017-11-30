from selenium import webdriver
import unittest
import time
import logging
import ddt
from selenium.common.exceptions import NoSuchElementException
import sys,os
print('sys.path',sys.path)
print('sys.path[0]==>',sys.path[0])
print('os.path.abspath(sys.path[0])==>',os.path.abspath(sys.path[0]))
print('os.path.abspath(_file_)==>',os.path.abspath(__file__))
print('__file_==>',str(__file__))

# 初始化日志对象
logging.basicConfig(
    # 日志级别
    level=logging.INFO,
    # 日志格式
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    # 打印日志的时间
    datefmt='%a,%d %b %Y %H:%M: %S',
    # 日志文件存放的目录（目录必须存在）及日志文件名
    filename='./report/caicai_test/report.log',
    # 打开日志文件的方式
    filemode='w'
)


@ddt.ddt
class TestDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    @ddt.data(['神奇动物在哪里', '叶ci'],
              ['疯狂动物城', '古德温'],
              ['大话西游之月光宝盒', '周星驰']
              )
    @ddt.unpack
    def test_dataDrivenByObj(self, testdata, expectdata):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        self.driver.implicitly_wait(30)
        try:
            self.driver.find_element_by_id('kw').send_keys(testdata)
            self.driver.find_element_by_id('su').click()
            time.sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error('查找的页面元素不存在，异常堆栈信息:' + str(traceback.format_exc()))
        except AssertionError as e:
            logging.info('搜索 %s ,期望 %s,失败' % (testdata, expectdata))
        except Exception as e:
            logging.error('未知错误，错误信息：' + str(traceback.format_exc()))
        else:
            logging.info('搜索 %s,期望 %s 通过' % (testdata, expectdata))


if __name__ == '__main__':
    unittest.main()
