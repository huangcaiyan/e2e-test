import threading
import time
from selenium import webdriver
# from queue import Queue
import queue
import time
import unittest 

class MyTest(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()

    def tearDown(self):
        driver.quit()

    def test_baidu(self):
        driver.get('http://www.baidu.com')

    def test_bing(self):
        driver.get('http://www.bing.com')


class MyThread(threading.Thread):

    def __init__(self, func, args=(), name=''):
        super(MyThread, self).__init__(target=func, args=args, name=name)
        self.name = name
        self.func = func
        self.args = args


    def run(self):
        while True:
            print('jjkjjllljjl')
            if  myqueue.empty() == False:
                suite = myqueue.get()
                self.func.run(suite)
            else:
                break


testcase=['test_baidu','test_bing']
myqueue = queue.Queue(maxsize = 10)
# threads = []

for i in testcase:
    suite = unittest.TestSuite()
    suite.addTest(MyTest(i))
    myqueue.put(suite)
    # t = threading.Thread(target=suite)
    # threads.append(t)

def test():
    runner = unittest.TextTestRunner()
    n=1
    for i in range(n):
        t = MyThread(runner)
        t.start()
if __name__ == '__main__':
    test()