import time
from .login_elem import *
from util.public_page import PublicPage


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
        login_button = self.driver.find_element_by_xpath(login_btn_elem)
        login_button.click()

    # 密码框错误 
    def get_input_error(self, input_name):
        public_page = PublicPage(self.driver)
        error_loc = self.driver.find_element_by_id(input_name + '-error')
        public_page.is_element_present(error_loc)
        error_msg = error_loc.text
        print('The text danger message is ', error_msg)
        return error_msg

    # 个人信息名称
    def personal_name_show(self):
        personal_name = self.driver.find_element_by_xpath(personal_name_elem)
        return personal_name.text

    # 登陆成功用户名展示
    # login_data:username,password
    def login(self, login_data):
        self.driver.delete_cookie('OAUTH_TOKEN')
        self.driver.get(self.url)
        self.type_username(str(login_data[0]))
        self.type_password(login_data[1])
        self.click_login_btn()
        time.sleep(5)
