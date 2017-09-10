from selenium import webdriver
from time import sleep,ctime
from selenium.webdriver import Remote
from threading import Thread

# def login(host,browser):
#     print(host,browser)
#     user_text_id = 'usernameInput'
#     pass_text_id = 'passwordInput'
#     login_button_id = 'loginButton'
#     dc = {'browserName':browser}
#     driver = webdriver.Remote(command_executor=host,desired_capabilities=dc)
#     driver.get('https://web-gyz-stage.guanplus.com')
#     driver.find_element_by_id(user_text_id).send_keys('18514509382')
#     driver.find_element_by_id(pass_text_id).send_keys('qq123456')
#     driver.find_element_by_id(login_button_id).click()
#     sleep(5)
#     print('login lalalalla')
#     driver.quit()


# if __name__ == '__main__':
#     lists = {
#             'http://127.0.0.1:4444/wd/hub':'chrome',
#             'http://127.0.0.1:5555/wd/hub':'chrome'

#         }
#     threads = []
#     driver = webdriver.Chrome()
#     files = range(len(lists))
#     for host,browser in lists.items():
#         t = Thread(target=login,args=(host,browser))
#         threads.append(t)
#     for i in files:
#         threads[i].start()

#     for i in files:
#         threads[i].join()

class MyThread(Thread):
    def __init__(self,func,args,name=''):
        Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        self.func(*self.args)

def super_play(file_,time):
    for i in range(2):
        print('yang' + file_ + ctime())
        sleep(time)
lists = {'dsf':3,'sdfsf':5,'sfsgee3':4}
threads = []
files = range(len(lists))

for file_,time in lists.items():
    t = MyThread(super_play,(file_,time),super_play.__name__)
    threads.append(t)

if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    print('end' + ctime())