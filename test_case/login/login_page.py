import time
from .login_elem import *

# 更新于2017-09-06
class LoginPage(object):

    def __init__(self, url, driver):
        self.url = url
        self.driver = driver
        

    # 输入用户名
    def type_username(self, username):
        username_text = self.driver.find_element_by_id(username_elem)
        username_text.clear()
        username_text.send_keys(username)

    # 输入密码
    def type_password(self, password):
        password_text = self.driver.find_element_by_id(password_elem)
        password_text.clear()
        password_text.send_keys(password)

    # 点击登录
    def click_login_btn(self):
        login_button = self.driver.find_element_by_css_selector(login_btn_elem)
        login_button.click()

    # 个人信息名称
    def personal_name_show(self):
        personal_name = self.driver.find_element_by_xpath(personal_name_elem)
        return personal_name.text

    # 登陆成功用户名展示
    # login_data:username,password
    def login(self,login_data):
        print('aaa=>',self.driver)
        self.driver.delete_cookie('OAUTH_TOKEN')
        self.driver.get(self.url)
        self.type_username(login_data[0])
        self.type_password(login_data[1])
        self.click_login_btn()
        time.sleep(5)



