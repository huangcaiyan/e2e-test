from .public_page import PublicPage
from selenium.common.exceptions import NoSuchElementException
import traceback, logging


class SelectAddressPage(object):
    def __init__( self, driver ):
        self.driver = driver

    def select_address( self, prov_drop_loc, province, city_drop_loc, city, distr_drop_loc, district ):
        """
        :param prov_drop_loc:省份webelement
        :param province:省份 名
        :param city_drop_loc:市 webelement
        :param city:市 名
        :param distr_drop_loc:区 webelement
        :param district:区 名
        :return:返回详细地址
        """
        self.select_prov(prov_drop_loc, province)
        self.select_city(city_drop_loc, city)
        self.select_dist(distr_drop_loc, district)

    def select_prov( self, prov_drop_loc, province ):
        """
        :param prov_drop_loc:省份下拉元素定位webelement
        :param province: 省份
        """
        try:
            public_page = PublicPage(self.driver)
            public_page.select_dropdown_item(prov_drop_loc, province)
        except NoSuchElementException as e:
            logging.error('[CreateCompPage]select_prov－－查找元素不存在，异常堆栈信息：', str(traceback.format_exc()))
        except Exception as e:
            logging.error('[CreateCompPage]select_prov－－选择省份失败,失败原因=>', str(e))

    def select_city( self, city_drop_loc, city ):
        """
        :param city_drop_loc:市下拉元素定位
        :param city: 市名
        """
        try:
            public_page = PublicPage(self.driver)
            public_page.select_dropdown_item(city_drop_loc, city)
        except NoSuchElementException as e:
            logging.error('[CreateCompPage]select_city－－查找元素不存在，异常堆栈信息：', str(traceback.format_exc()))
        except Exception as e:
            print('[CreateCompPage]select_city－－选择 市 失败,失败原因=>', str(e))

    def select_dist( self, dist_drop_loc, district ):
        """
        :param dist_drop_loc:区下拉元素定位
        :param district: 区
        """
        try:
            public_page = PublicPage(self.driver)
            public_page.select_dropdown_item(dist_drop_loc, district)
        except NoSuchElementException as e:
            logging.error('[CreateCompPage]select_dist－－查找元素不存在，异常堆栈信息：', str(traceback.format_exc()))
        except Exception as e:
            print('[CreateCompPage]select_dist－－选择 区 失败,失败原因=>', str(e))
