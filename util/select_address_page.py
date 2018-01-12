from .public_page import PublicPage
from selenium.common.exceptions import NoSuchElementException
import traceback, logging


class SelectAddressPage(object):
    def __init__(self, driver):
        self.driver = driver

    def select_address(self, prov, city, distr):
        """
        :param prov: 省份
        :param city: 市
        :param dist: 区
        """
        self.select_prov(prov)
        self.select_city(city)
        self.select_dist(distr)

    def select_prov(self, prov_drop_elem, prov):
        """
        :param prov_drop_elem:省份下拉元素定位
        :param prov: 省份
        """
        try:
            public_page = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(prov_drop_elem)
            public_page.select_dropdown_item(drop_loc, prov)
        except NoSuchElementException as e:
            logging.error('[CreateCompPage]select_prov－－查找元素不存在，异常堆栈信息：', str(traceback.format_exc()))
        except Exception as e:
            logging.error('[CreateCompPage]select_prov－－选择省份失败,失败原因=>', str(e))

    def select_city(self, city_drop_elem, city):
        """
        :param city_drop_elem:市下拉元素定位
        :param city: 市名
        """
        try:
            public_page = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(city_drop_elem)
            public_page.select_dropdown_item(drop_loc, city)
        except NoSuchElementException as e:
            logging.error('[CreateCompPage]select_city－－查找元素不存在，异常堆栈信息：', str(traceback.format_exc()))
        except Exception as e:
            print('[CreateCompPage]select_city－－选择 市 失败,失败原因=>', str(e))

    def select_dist(self, dist_drop_elem, dist):
        """
        :param dist_drop_elem:区下拉元素定位
        :param dist: 区
        """
        try:
            public_page = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_name(dist_drop_elem)
            public_page.select_dropdown_item(drop_loc, dist)
        except NoSuchElementException as e:
            logging.error('[CreateCompPage]select_dist－－查找元素不存在，异常堆栈信息：', str(traceback.format_exc()))
        except Exception as e:
            print('[CreateCompPage]select_dist－－选择 区 失败,失败原因=>', str(e))
