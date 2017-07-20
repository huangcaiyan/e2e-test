import time

class LoginPage:

    # element location
    user_text_id = 'usernameInput'
    pass_text_id = 'passwordInput'
    login_button_id = 'loginButton'

    def __init__(self,url,driver):
        self.url = url
        self.driver = driver

    def login(self,username,password):
        #open url
        self.driver.get(self.url)
        #locate username
        username_text = self.driver.find_element_by_id(self.user_text_id)
        #clear username text
        username_text.clear()
        #input username
        username_text.send_keys(username)
        #locate password
        password_text = self.driver.find_element_by_id(self.pass_text_id)
        #clear password
        password_text.clear()
        #input password
        password_text.send_keys(password)
        #locate login button
        login_button = self.driver.find_element_by_id(self.login_button_id)
        #click login button
        login_button.click()
        #delay
        time.sleep(20)
     


