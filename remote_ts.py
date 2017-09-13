from selenium import webdriver
from time import sleep
from selenium.webdriver import Remote
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



# def login():
#     # driver = webdriver.Chrome()
#     binary = FirefoxBinary('C:\\Users\yangchunhong\\AppData\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\selenium\\webdriver\\firefox\\firefox_binary.py')
#     driver = webdriver.Firefox(firefox_binary=binary)

#     driver.get('http://guanplus-app-accountingfirm-web-dev-1.cn-north-1.eb.amazonaws.com.cn')
#     userNameInput = driver.find_element_by_id('usernameInput')
#     userNameInput.clear()
#     userNameInput.send_keys('18514509382')
#     passwordInput = driver.find_element_by_id('passwordInput')
#     passwordInput.clear()
#     passwordInput.send_keys('qq123456')
#     loginButton = driver.find_element_by_id('loginButton')
#     loginButton.click()
#     sleep(10)
#     driver.quit()

lists = {
            'http://127.0.0.1:4444/wd/hub':'chrome',
            # 'http://192.168.38.88:5555/wd/hub':'chrome'
            'http://127.0.0.1:5556/wd/hub':'chrome'

        }


for host,browser in lists.items():
    print(host,browser)
    driver = Remote(command_executor=host,
                    desired_capabilities={ 
                                            'platform':'ANY',
                                            'browserName':browser,
                                            'version':'',
                                            'javascriptEnabled':True,
                                            'acceptInsecureCerts':True
                                        }
                    )
    driver.get('http://guanplus-app-accountingfirm-web-dev-1.cn-north-1.eb.amazonaws.com.cn')
    userNameInput = driver.find_element_by_id('usernameInput')
    userNameInput.clear()
    userNameInput.send_keys('18514509382')
    passwordInput = driver.find_element_by_id('passwordInput')
    passwordInput.clear()
    passwordInput.send_keys('qq123456')
    loginButton = driver.find_element_by_id('loginButton')
    loginButton.click()
    sleep(10)
    driver.quit()
    
