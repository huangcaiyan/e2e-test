import time
from util.public_page import PublicPage
from .setting_elem import *

# 设置page
# 创建于2017-8
# caicai


class SettingPage(object):

    def __init__(self, driver,base_url):
        self.driver = driver
        self.base_url = base_url

# 去帐套信息页面（管理员角色）
    def go_to_setting_page(self):
        try:
            publicPage = PublicPage(self.driver)
            self.driver.get(self.base_url + comp_billing_url)
            time.sleep(3)
            comp_billing_loc = self.driver.find_element_by_xpath(
                comp_billing_xpath)
            if publicPage.is_element_present(comp_billing_loc):
                print('[SettingPage]＋＋＋＋＋＋ 去帐套信息页面 成功＋＋＋＋＋＋')
            else:
                print('[SettingPage]－－－－－－ 去帐套信息页面 失败！－－－－－－')
        except Exception as e:
            print(
                '[SettingPage] There was an exception when go_to_setting_page= %s', str(e))

# 去往来信息页面
    def go_to_contact_page(self):
        try:
            publicPage = PublicPage(self.driver)
            self.driver.get(self.base_url + contact_url)
            time.sleep(3)
            add_loc = self.driver.find_element_by_xpath(contact_xpath)
            if publicPage.is_element_present(add_loc):
                print('[SettingPage]＋＋＋＋＋＋ 去往来信息页面 成功＋＋＋＋＋＋')
            else:
                print('[SettingPage]－－－－－－ 去往来信息页面 失败！－－－－－－')
        except Exception as e:
            print(
                '[SettingPage] There was an exception when go_to_contact_page= %s', str(e))

# 去用户管理页面
    def go_to_mutil_user_page(self):
        try:
            publicPage = PublicPage(self.driver)
            self.driver.get(self.base_url + mutil_user_url)
            time.sleep(3)
            start_loc = self.driver.find_element_by_xpath(multi_user_xpath)
            if publicPage.is_element_present(start_loc):
                print('[SettingPage]＋＋＋＋＋＋ 去用户管理页面 成功＋＋＋＋＋＋')
            else:
                print('[SettingPage]－－－－－－ 去用户管理页面 失败！－－－－－－')
        except Exception as e:
            print(
                '[SettingPage] There was an exception when go_to_mutil_user_page= %s', str(e))

# 去股东页面
    def go_to_partnerset_page(self):
        try:
            publicPage = PublicPage(self.driver)
            self.driver.get(self.base_url + partner_set_url)
            time.sleep(3)
            add_loc = self.driver.find_element_by_xpath(partner_set_url)
            if publicPage.is_element_present(start_loc):
                print('[SettingPage]＋＋＋＋＋＋ 去股东页面 成功＋＋＋＋＋＋')
            else:
                print('[SettingPage]－－－－－－ 去股东页面 失败！－－－－－－')
        except Exception as e:
            print(
                '[SettingPage] There was an exception when go_to_partner_set_page= %s', str(e))

# 去税率设置页面
    def go_to_tax_rate_page(self):
        try:
            publicPage = PublicPage(self.driver)
            self.driver.get(self.base_url + tax_rate_url)
            time.sleep(3)
            tax_loc = self.driver.find_element_by_xpath(tax_rate_url)
            if publicPage.is_element_present(tax_loc):
                print('[SettingPage]＋＋＋＋＋＋ 去税率设置页面 成功＋＋＋＋＋＋')
            else:
                print('[SettingPage]－－－－－－ 去税率设置页面 失败！－－－－－－')
        except Exception as e:
            print(
                '[SettingPage] There was an exception when go_to_tax_rete_page= %s', str(e))
