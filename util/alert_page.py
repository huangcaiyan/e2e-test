from selenium import webdriver

# alert 窗口提示信息
class AlertPage:
    alert_msg_tagname = 'alert'    
    def __init__(self,driver):
        self.driver = driver

    # 获取带alert标签的信息内容    
    def get_alert_msg(self):
        alert_msg_elem = self.driver.find_element_by_tag_name(self.alert_msg_tagname)
        alert_msg = alert_msg_elem.text
<<<<<<< HEAD
        print('alert_msg=',alert_msg)
=======
        print (alert_msg)
>>>>>>> 330b7db7e58d2f203a53f8d6fe04b38dc481db11
        alert_info_array = alert_msg.split('\n')
        print('The alert message is ',alert_info_array[2])
        return alert_info_array[2]

    
        
        






