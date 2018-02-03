from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.select import Select
import time
import random
import logging, traceback
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import platform


class PublicPage:
    # location
    pre_button_xpath = '//*[@id="ui-datepicker-div"]/div/a[1]'
    next_button_xpath = '//*[@id="ui-datepicker-div"]/div/a[2]'
    # 日期年下拉 class
    datepicker_year_drop_elem = '.ui-datepicker-year'
    # 日期 月下拉 class
    datepicker_month_drop_elem = 'ui-datepicker-month'

    def __init__( self, driver ):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    # 判断元素是否显示
    @staticmethod
    def is_element_present( elem_loc ):
        try:
            elem_loc
        except NoSuchElementException as e:
            print('查找元素不存在，异常堆栈信息:', str(traceback.format_exc()))
            return False
        else:
            return True

    def wait_until_loader_disapeared( self ):
        """
        等待直到加载蒙板消失
        :return: 返回蒙板状态，is_disapeared = False时，表示蒙板消失
        """
        is_disapeared = WebDriverWait(self.driver, 30, 1).until_not(
            lambda x: self.driver.find_element_by_css_selector('.loader').is_displayed())
        return is_disapeared

    def wait_until_svg_disapeared( self ):
        """
        等待黑色logo svg矢量图蒙板消失
        :return:返回蒙板状态，is_disapeared = False时，表示svg图消失；
        """
        is_dispeared = WebDriverWait(self.driver, 30, 1).until_not(
            lambda x: self.driver.find_element_by_css_selector('.splash').is_displayed())
        print('is_dispeared=>', is_dispeared)

    def is_alert_present( self ):
        """
        判断alert框是否出现
        :return:False，True
        """
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            logging.error('[PublicPage]is_alert_present--查找元素不存在，异常堆栈信息：', str(traceback.format_exc()))
            return False
        return True

    def close_alert_and_get_its_text( self ):
        """
        关闭alert框，且获取alert内容
        :return: alert 内容
        """
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def select_option( self, select_loc, option_value, drop_loc=None ):
        """
        :param drop_loc: 展开下拉元素定位 webelement
        :param select_loc: <select>元素定位 webelement
        :param option_value: 选择方式（value／index），可以是options里的value值，也可以是options的索引
        :return: 选择option
        """
        try:
            if drop_loc is not None:
                drop_loc.click()
                time.sleep(1)
            select = Select(select_loc)
            if type(option_value) == str:
                selected = select.select_by_value(option_value)
            elif type(option_value) == int:
                selected = select.select_by_index(option_value)
            else:
                print('输入的option_value值有误，应该是string或integer类型！')
                selected = None
            return selected
        except NoSuchElementException as e:
            logging.error('查找元素失败，异常堆栈信息是＝>', str(traceback.format_exc(e)))
        except Exception as e:
            logging.error('发生未知错误，错误信息是=>', str(e))

    # 日历
    def select_date( self, calen_xpath, day ):
        """
        :param calen_xpath: 日历位置xpath
        :param day:日期（1、2、3...）
        :return:
        """
        calen_loc = self.driver.find_element_by_xpath(calen_xpath)
        self.click_elem(calen_loc)
        pre_button = self.driver.find_element_by_xpath(self.pre_button_xpath)
        next_button = self.driver.find_element_by_xpath(self.next_button_xpath)
        time.sleep(2)
        if pre_button:
            return self.driver.find_element_by_link_text(day).click()
        else:
            return False

    def select_date_by_ymd( self, calen_drop_loc, year, month, day ):
        """
        :param calen_drop_loc: 日历下拉元素
        :param year: 年（2012、2017、2018...）
        :param month: 月（一月、二月...）
        :param day: 日（1、2、3...）
        :return: 返回年月日
        """
        try:
            self.click_elem(calen_drop_loc)
            year_drop_loc = self.driver.find_element_by_css_selector(self.datepicker_year_drop_elem)
            self.select_dropdown_item(year_drop_loc, year)

            month_drop_loc = self.driver.find_element_by_css_selector(self.datepicker_month_drop_elem)
            self.select_dropdown_item(month_drop_loc, month)

            day_loc = self.driver.find_element_by_link_text(day)
            self.click_elem(day_loc)
        except NoSuchElementException as e:
            logging.error('[PublicPage]select_date_by_ymd--查找元素不存在，异常堆栈信息:', str(traceback.format_exc()))
        except Exception as e:
            print('[PublicPage]select_date_by_ymd－－选择年月日失败,错误原因=>', str(e))

    def select_month( self, calen_drop_loc, month ):
        """
        :param calen_drop_loc: 日历展开元素定位
        :param month: 月（1,2,3...）
        :return: 月份选择插件
        """
        month_index = int(month) - 1
        print('month_index=>', month_index)
        try:
            self.click_elem(calen_drop_loc)
            pre_btn = self.driver.find_element_by_css_selector('.pull-left')
            time.sleep(2)
            if pre_btn:
                return self.driver.find_elements_by_css_selector('.month-button')[month_index].click()
            else:
                return False
        except NoSuchElementException as e:
            logging.error('[PublicPage]select_month－－查找元素不存在，异常堆栈信息：', str(traceback.format_exc()))
        except Exception as e:
            print('[PublicPage]select_month－－选择月份失败,错误原因=>', str(e))

    def delete_date( self, elem_xpath ):
        """
        :param elem_xpath: 删除日历日期按钮xpath
        :return:清除日历日期
        """
        del_loc = self.driver.find_element_by_xpath(elem_xpath)
        self.scroll_to_elem(del_loc)
        return del_loc.click()

    @staticmethod
    def random_num( num ):
        """
        :param num: 随机数范围（10，表示0到10的随机数；100：表示0到100的随机数；）
        :return: 返回0 到 num范围内的随机数
        """
        return random.randrange(0, num)

    @staticmethod
    def eight_random_nums():
        """
        :return: 返回 8 位数的随机数
        """
        return random.randint(10000000, 100000000)

    @staticmethod
    def get_system_name():
        """
        :return: 运行代码的系统名称
        """
        running_system = platform.system()
        print("system=>", running_system)
        if running_system == 'Darwin':
            current_system_name = 'Mac'
        elif running_system == 'Windows':
            current_system_name = 'Windows'
        else:
            current_system_name = 'others'
            print('自动化测试程序在 非Mac 或 windows 机器上运行！')
        return current_system_name

    def max_window( self ):
        """
        :return: windows系统下浏览器最大化
        """
        if self.get_system_name() == 'Windows':
            self.driver.max_winddows()

    def click_elem( self, elem_loc ):
        """
        :param elem_loc: 单击元素的元素定位
        :return: 点击元素
        """
        try:
            if not self.wait_until_loader_disapeared():
                self.scroll_to_elem(elem_loc)
                return elem_loc.click()
            else:
                time.sleep(1)
                self.scroll_to_elem(elem_loc)
                return elem_loc.click()
        except NoSuchElementException as e:
            logging.error('[PublicPage]click_elem--查找元素不存在，异常堆栈信息是：', str(traceback.format_exc()))
        except Exception as e:
            print('[PublicPage]click_elem--未知错误，错误信息是：', str(e))

    def double_click_elem( self, elem_loc ):
        """
        :param elem_loc: 双击元素元素定位
        :return: 双击元素elem_loc
        """
        try:
            if self.is_element_present(elem_loc):
                action = ActionChains(self.driver)
                action.move_to_element(elem_loc).double_click()
            else:
                action = ActionChains(self.driver)
                self.scroll_to_elem(elem_loc)
                action.move_to_element(elem_loc).double_click()
        except Exception as e:
            print('There was an exception when double_click_elem %s', str(e))

    def set_value( self, elem_loc, input_value ):
        """
        :param elem_loc: input框元素定位
        :param input_value: input框输入值
        :return:给输入框输入值
        """
        try:
            if self.is_element_present(elem_loc):
                self.move_to_element_to_click(elem_loc)
            else:
                self.scroll_to_elem(elem_loc)
            elem_loc.clear()
            elem_loc.send_keys(input_value)
        except NoSuchElementException as e:
            logging.error('[PublicPage]set_value--查找元素不存在，堆栈异常信息是：', str(traceback.format_exc(e)))
        except Exception as e:
            logging.error('[PublicPage]set_value--未知错误，错误信息是：', str(e))

    @staticmethod
    def keys_enter( elem_loc ):
        """
        :param elem_loc: 需要摁回车键的元素定位
        :return:键盘输入enter
        """
        try:
            elem_loc.send_keys(Keys.ENTER)
        except NoSuchElementException as e:
            logging.error('[PublicPage]keys_enter--查找元素不存在，对战异常信息：', str(traceback.format_exc()))
        except Exception as e:
            logging.error('[PublicPage]keys_enter--未知错误，错误信息：', str(e))

    def click_backspace_btn( self, elem_loc ):
        """
        :param elem_loc: delete键元素定位
        :return: 点击delete键
        """
        try:
            if self.is_element_present(elem_loc):
                elem_loc.send_keys(Keys.BACKSPACE)
            else:
                self.scroll_to_elem(elem_loc)
                elem_loc.send_keys(Keys.BACKSPACE)
        except Exception as e:
            print('There was an exception when click_backspace_btn=>', str(e))

    def scroll_to_set_value( self, elem_loc, input_value ):
        """
        :param elem_loc:输入框元素定位
        :param input_value: 输入框输入值
        :return:
        """
        try:
            self.is_element_present(elem_loc)
            self.scroll_to_elem(elem_loc)
            elem_loc.clear()
            elem_loc.send_keys(input_value)
        except Exception as e:
            print('There was an exception when scroll_to_set_value=>', str(e))

    def get_value( self, elem_loc ):
        """
        :param elem_loc: 文本位置元素定位
        :return:获取文本的内容text
        """
        try:
            self.scroll_to_elem(elem_loc)
            text_value = elem_loc.text
            return text_value
        except NoSuchElementException as e:
            logging.error('[PublicPage]get_value--查找元素不存在，异常堆栈信息是：', str(traceback.format_exc()))
        except Exception as e:
            logging.error('[PublicPage]get_value--未知错误，错误信息是', str(traceback.format_exc()))

    # 光标移动到元素为止并做点击操作
    def move_to_element_to_click( self, elem_loc ):
        """
        :param elem_loc:
        :return:
        """
        action = ActionChains(self.driver)
        action.move_to_element(elem_loc).click().perform()

    # 移动到元素element对象的“底端”与当前窗口的“底部”对齐
    def scroll_to_elem( self, elem_loc ):
        try:
            return self.driver.execute_script("arguments[0].scrollIntoView(false);", elem_loc)
            time.sleep(1)
        except WebDriverException:
            self.driver.execute_script('window.scrollBy(0,-100);')
            time.sleep(2)

    # 移动到页面到中部
    def scroll_to_page_center( self ):
        return self.driver.execute_script("window.scrollTo(0, 1000)")

    # 将光标定位到页面顶部
    def scroll_to_top( self ):
        return self.driver.execute_script('scroll(250,0)')

    # 将光标定位到页面底部
    def scroll_to_bottom( self ):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 跳转至modal框
    def switch_to_add_contact_modal_dialog( self ):
        self.driver.switch_to_active_element()

    # 获取元素位置坐标
    @staticmethod
    def get_elem_location( elem_loc ):
        try:
            location = elem_loc.location
            size = elem_loc.size
            print('location=>', location, '\nsize=>', size)
            return location
        except Exception as e:
            print('[PublicPage]There was an exception when get_elem_location=>', str(e))

    def select_dropdown_item( self, drop_loc, item_name ):
        """
        :param drop_loc: 下拉元素定位
        :param item_name:下拉可选值text
        :return:选择下拉项
        """
        try:
            self.click_elem(drop_loc)
            time.sleep(1)
            item_loc = self.driver.find_element_by_link_text(item_name)
            if self.is_element_present(item_loc):
                self.click_elem(item_loc)
            else:
                print('item_loc=' + item_name + 'is not show!')
                self.driver.quit()
        except NoSuchElementException as e:
            logging.error('[PublicPage]select_dropdown_item--查找元素不存在，异常堆栈信息:', str(traceback.format_exc()))
        except Exception as e:
            print('[PublicPage]select_dropdown_item--未知错误，错误信息是：', str(e))
            self.driver.quit()

    # 必填项红框警示
    def has_danger_is_show( self ):
        publicPage = PublicPage(self.driver)
        ui_loc = self.driver.find_element_by_css_selector('.has-danger')
        print('publicPage.is_element_present(ui_loc)=>', publicPage.is_element_present(ui_loc))
        return publicPage.is_element_present(ui_loc)

    def click_operation_btn( self, name_td_index, item_name, btn_td_index, btn_name ):
        """
        :param name_td_index: 名称的td索引（表格行中任意唯一值，如收支表里的单号td索引，股东表里股东名称的索引,即唯一值在一行中第几列）
        :param item_name: 名称（表格行中的任意唯一值，如收支里的单号，股东里的股东名）
        :param btn_td_index: 操作按钮索引（表格中‘操作’列的td索引，如收支列表中操作列的td索引是‘5’
        :param btn_name: 操作按钮名称（可选值'edit'、'delete')
        :return:点击操作按钮
        """
        row_elems = self.driver.find_elements_by_tag_name('tr')
        # 获取列表中所有行的名称（唯一值）
        names = []
        for tr_index in range(1, len(row_elems)):
            # if tr_index == 0:
            #     tr_index = tr_index + 1
            name_loc = self.driver.find_elements_by_tag_name('tr')[tr_index].find_elements_by_tag_name('td')[
                name_td_index].find_element_by_tag_name('span')
            name = name_loc.text
            names.append(name)
        print('names=>', names)

        # 获取所选名称所在行的索引；
        index = names.index(item_name)
        # 点击对应名称行的操作按钮；
        if btn_name == 'edit':
            btn_index = 0
        elif btn_name == 'delete':
            btn_index = 1
        else:
            False
        btn_loc = self.driver.find_elements_by_tag_name('tr')[index].find_elements_by_tag_name('td')[
            btn_td_index].find_elements_by_tag_name('button')[btn_index]
        return btn_loc.click()

    # ----------------------------------------------------------------------------------------------------------------------
