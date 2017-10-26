from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from account_dashboard_elem import *
from util.public_page import PublicPage

# 会计首页
# 创建于2017-10-23日
# caicai


class AccountDashbaordPage(object):
    """会计首页－page"""

    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        # self.driver = driver

    # 点击操作按钮
    def click_operation_btn(self):
        page_url = self.driver.current_url
        print('[AccountDashbaordPage]--page_url=>', page_url)
        if '/app/home-page/accounting' in page_url:
            try:
                publicPage = PublicPage(self.driver)
                btn_loc = self.driver.find_element_by_xpath(operation_btn_elem)
                publicPage.click_elem(btn_loc)
                if publicPage.is_element_present(btn_drop_ite_elem):
                    print('[AccountDashbaordPage]click_operation_btn－－点击下拉操作 成功－－')
                else:
                    print('[AccountDashbaordPage]click_operation_btn－－点击下拉操作 失败－－')
                    exit()
            except Exception as e:
                print(
                    '[AccountDashbaordPage]click_operation_btn－－点击下拉操作 失败－－失败原因＝>', str(e))
                exit()
        elif '/app/home-page/assist' in page_url:
            print('[AccountDashbaordPage]click_operation_btn－－当前页面是助理首页，点击下拉操作 失败')
        else:
            print('[AccountDashbaordPage]click_operation_btn－－非助理／会计首页，操作失败！')
            exit()

    # 点击结转、过帐、反过帐、驳回审核按钮
    def select_operation_item(self, item_index):
        if item_index == 0:
            operation_name = '结转'
        elif item_index == 1:
            operation_name = '过帐'
        elif item_index == 2:
            operation_name = '反过帐'
        elif item_index == 3:
            operation_name = '驳回审核'
        page_url = self.driver.current_url
        print('[AccountDashbaordPage]--page_url=>', page_url)
        if '/app/home-page/accounting' in page_url:
            try:
                publicPage = PublicPage(self.driver)
                item_loc = self.driver.find_element_by_css_selector(
                    btn_drop_item_elem).find_elements_by_tag_name(btn_tag_name_elem)[item_index]
                publicPage.click_elem(btn_loc)
            except Exception as e:
                print('[AccountDashbaordPage]select_operation_item－－' +
                      operation_name + ' 失败－－失败原因＝>', str(e))
        elif '/app/home-page/assist' in page_url:
            print('[AccountDashbaordPage]select_operation_item－－' +
                  operation_name + '失败')
        else:
            print('[AccountDashbaordPage]select_operation_item－－' +
                  operation_name + '失败！')
