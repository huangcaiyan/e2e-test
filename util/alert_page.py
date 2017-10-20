from selenium import webdriver

# alert 窗口提示信息


class AlertPage:
    alert_msg_tagname = 'alert'

    def __init__(self, driver):
        self.driver = driver

    # 获取带alert标签的信息内容
    def get_alert_msg(self):
        alert_msg_elem = self.driver.find_element_by_tag_name(
            self.alert_msg_tagname)
        alert_msg = alert_msg_elem.text
        if alert_msg == '':
            print('alert_msg 为空，获取alert 内容失败！')
            exit()
        else:
            alert_info_array = alert_msg.split('\n')
            print('The alert message is ', alert_info_array[2])
            return alert_info_array[2]
        print('alert_msg=', alert_msg)
            
