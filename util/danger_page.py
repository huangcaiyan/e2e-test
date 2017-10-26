from .public_page import PublicPage


class DangerPage:
    # 元素
    # class 为 text_danger
    text_danger_msg_elem = '.text-danger'
    # class 为 alert_danger
    alert_danger_msg_elem = '.alert_danger'
    # 错误提示信息 id
    error_msg_elem = 'errMsg'
    # 输入框警示文字class
    input_alert_msg_elem = '.error'
    alert_msgs = []
    def __init__(self, driver):
        self.driver = driver

    # alert 框danger提示内容
    def get_alert_danger_msg(self):
        publicPage = PublicPage(self.driver)
        alert_danger_msg_loc = self.driver.find_element_by_class_name(
            self.alert_danger_msg_elem)
        publicPage.is_element_present(alert_danger_msg_loc)
        alert_danger_msg = self.alert_danger_msg_loc.text
        print('The alert danger message is ', alert_danger_msg)
        return alert_danger_msg

    # 输入框下警示文字
    def get_text_danger_msg(self):
        publicPage = PublicPage(self.driver)
        text_danger_msg_loc = self.driver.find_element_by_css_selector(
            self.text_danger_msg_elem)
        publicPage.is_element_present(text_danger_msg_loc)
        text_danger_msg = text_danger_msg_loc.text
        print('The text danger message is ', text_danger_msg)
        return text_danger_msg

    # 获取错误提示信息
    def get_error_msg(self):
        publicPage = PublicPage(self.driver)
        error_msg_loc = self.driver.find_element_by_id(self.error_msg_elem)
        publicPage.is_element_present(error_msg_loc)
        error_msg = error_msg_loc.text
        print('The error message is ', error_msg)
        return error_msg

    #  输入框警示文字
    def get_input_alert_msg(self):
        publicPage = PublicPage(self.driver)
        input_alert_msg_loc = self.driver.find_element_by_css_selector(
            self.input_alert_msg_elem)
        publicPage.is_element_present(input_alert_msg_loc)
        input_alert_msg = input_alert_msg_loc.text
        print('The text danger message is ', input_alert_msg)
        return input_alert_msg
