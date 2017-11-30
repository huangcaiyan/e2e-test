from selenium.webdriver import Remote
from selenium import webdriver

# 启用驱动器


def browser():
    host = 'localhost:4444'  # 运行主机：端口号
    dc = {'browserName': 'chrome'}   # 制定浏览器（'chrome','firefox')
    driver = Remote(command_executor='http://:' + host + '/wd/hub',
                    desired_capabilities=dc
                    )
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get('https://firms.guanplus.com')
    dr.quit()
