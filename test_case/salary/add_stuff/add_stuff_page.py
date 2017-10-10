# from selenium import webdriver
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from util.public_page import PublicPage
from .add_stuff_elem import *
from test_case.salary.salary_page import SalaryPage

# 添加员工
# 创建于2017-09-21-四
# caicai


class AddStuffPage(object):

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver

    # 警示框是否出现
    def has_danger_is_show(self):
        publicPage = PublicPage(self.driver)
        ui_loc = self.driver.find_element_by_css_selector(has_danger_elem)
        print('publicPage.is_element_present(ui_loc)=>',
              publicPage.is_element_present(ui_loc))
        return publicPage.is_element_present(ui_loc)

    # 设置编号(0)
    # num：编号
    def set_num(self, num):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(nun_elem)
            publicPage.set_value(input_loc, num)
        except Exception as e:
            print('[AddStuffPage] There was an exception when set_nun=>', str(e))

    # 设置名称(1)
    # name:名字
    def set_name(self, name):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(name_elem)
            publicPage.set_value(input_loc, name)
        except Exception as e:
            print('[AddStuffPage] There was an exception when set_name=>', str(e))

    # 选择国籍(2)
    # country:中国、非中国
    def select_country(self, country):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(country_drop_elem)
            publicPage.select_dropdown_item(drop_loc, country)
        except Exception as e:
            print('[AddStuffPage] There was an exception when select_country=>', str(e))

    # 设置身份证号(3)
    # id:身份证号
    def set_id(self, id):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(id_elem)
            publicPage.set_value(input_loc, id)
        except Exception as e:
            print('[AddStuffPage] There was an exception when set_id=>', str(e))

    # 选择性别(5)
    # sex:男、女
    def select_sex(self, sex):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(sex_drop_elem)
            publicPage.select_dropdown_item(drop_loc, sex)
        except Exception as e:
            print('[AddStuffPage] There was an exception when select_sex=>', str(e))

    # 选择部门性质(7)
    # partment:管理部门、销售部门
    def select_partment(self, partment):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(partment_drop_loc)
            publicPage.select_dropdown_item(drop_loc, partment)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when select_partment=>', str(e))

    # 职务(8)
    # position:职位
    def set_position(self, position):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(position_elem)
            publicPage.set_value(input_loc, position)
        except Exception as e:
            print('[AddStuffPage] There was an exception when set_position=>', str(e))

    # 是否是雇员(9)
    # employed:是、否
    def select_employed(self, employed):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(employ_drop_elem)
            publicPage.select_dropdown_item(drop_loc, employed)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when select_employed=>', str(e))

    # 个人股本投资额(10)
    # capital:股本金额（number）
    def set_capital(self, capital):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(capital_elem)
            publicPage.set_value(input_loc, capital)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_capital=>', str(e))

    # 是否残疾烈属孤老(11)
    # health:健康状况：是、否
    def select_health(self, health):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(health_drop_elem)
            publicPage.set_value(drop_loc, health)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when select_health=>', str(e))

    # 人员状态(12)
    # status:正常、离职
    def select_office_status(self, status):
        try:
            publicPage = PublicPage(self.driver)
            drop_loc = self.driver.find_element_by_xpath(
                office_status_drop_elem)
            publicPage.select_dropdown_item(drop_loc, status)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when select_office_status=>', str(e))

    # 电话(13)
    # phone：手机号
    def set_phone(self, phone):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(phone_elem)
            publicPage.set_value(input_loc, phone)
        except Exception as e:
            print('[AddStuffPage] There was an exception when set_phone=>', str(e))

    # 电子邮箱(14)
    # email：邮箱
    def set_email(self, email):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(email_elem)
            publicPage.set_value(input_loc, email)
        except Exception as e:
            print('[AddStuffPage] There was an exception when set_email=>', str(e))

    # 联系地址(15)
    # address:地址
    def set_address(self, address):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(address_elem)
            publicPage.set_value(input_loc, address)
        except Exception as e:
            print('[AddStuffPage] There was an exception when set_address=>', str(e))

    # 选择户口类型(16)
    # registered_type:农业、非农业
    def select_registered_type(self, registered_type):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(registered_drop_elem)
            publicPage.set_value(input_loc, registered_type)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when select_registered_type=>', str(e))

    # 开户银行(17)
    # bank_name:开户银行名
    def set_openning_bank(self, bank_name):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(opening_bank_elem)
            publicPage.set_value(input_loc, bank_name)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_openning_bank=>', str(e))

    # 银行账号(18)
    # bank_num：帐号
    def set_bank_num(self, bank_num):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(bank_num_elem)
            publicPage.set_value(input_loc, bank_num)
        except Exception as e:
            print('[AddStuffPage] There was an exception when set_bank_num=>', str(e))

    # 基本工资(19)
    # base_salary:基本工资（number）
    def set_basic_salary(self, basic_salary):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(basic_salary_elem)
            publicPage.set_value(input_loc, basic_salary)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_basic_salary=>', str(e))

    # 岗位工资(20)
    # actual_salary:岗位工资（number）
    def set_actual_salary(self, actual_salary):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(actual_salary_elem)
            publicPage.set_value(input_loc, actual_salary)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_actual_salary=>', str(e))

    # 选择缴纳公积金
    def click_fund_check(self):
        try:
            publicPage = PublicPage(self.driver)
            check_loc = self.driver.find_element_by_xpath(fund_check_elem)
            publicPage.click_elem(check_loc)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when click_fund_check=>', str(e))

    # 医疗保险缴纳基数(21)
    # medicare_care:医疗保险基数（number）
    def set_medicare_base(self, medicare_base):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(medicare_base_elem)
            publicPage.set_value(input_loc, medicare_base)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_medicare_base=>', str(e))

    # 养老保险缴纳基数(22)
    # pension_base:养老保险缴纳基数
    def set_pension_base(self, pension_base):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(pension_base_elem)
            publicPage.set_value(input_loc, pension_base)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_pension_base=>', str(e))

    # 个人社保
    # 医疗(23)
    # pers_medicare：医疗（number）
    def set_pers_medicare(self, pers_medicare):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(pers_medicare_elem)
            publicPage.set_value(input_loc, pers_medicare)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_pers_medicare=>', str(e))

    # 个人社保
    # 养老(24)
    # pers_pension:养老金（number）
    def set_pers_pension_insurance(self, pers_pension):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                pers_pension_insurance_elem)
            publicPage.set_value(input_loc, pers_pension)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_pers_pension_insurance=>', str(e))

    # 个人社保(25)
    # pers_unemploy:失业保险（number)
    def set_pers_unemploy_insurance(self, pers_unemploy):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                pers_unemploy_insurance_elem)
            publicPage.set_value(input_loc, pers_unemploy)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_pers_unemploy_insurance=>', str(e))

    # 公司社保(26)
    # comp_medicare：医疗（number)
    def set_comp_medicare(self, comp_medicare):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(comp_medicare_elem)
            publicPage.set_value(input_loc, comp_medicare)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_comp_medicare=>', str(e))

    # 公司社保(27)
    # comp_pension_insurance:养老（number）
    def set_comp_pension_insurance(self, comp_pension_insurance):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                comp_pension_insurance_elem)
            publicPage.set_value(input_loc, comp_pension_insurance)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_comp_pension_insurance=>', str(e))

    # 公司社保(28)
    # comp_unemploy_insurance：失业（number）
    def set_comp_unemploy_insurance(self, comp_unemploy_insurance):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                comp_unemploy_insurance_elem)
            publicPage.set_value(input_loc, comp_unemploy_insurance)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_comp_unemploy_insurance=>', str(e))

    # 公司社保
    # comp_birth_insurance:生育（number）
    def set_comp_birth_insurance(self, comp_birth_insurance):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                comp_birth_insurance_elem)
            publicPage.set_value(input_loc, comp_birth_insurance)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_comp_birth_insurance=>', str(e))

    # 公司社保
    # comp_injury_insurance：工伤（number）
    def set_comp_injury_insurance(self, comp_injury_insurance):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                comp_injury_insurance_elem)
            publicPage.set_value(input_loc, comp_injury_insurance)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_comp_injury_insurance=>', str(e))

    # 公积金缴纳基数
    # public_reserve_fund：公积金缴纳基数（number）
    def set_public_reserve_fund(self, public_reserve_fund):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                public_reserve_fund_elem)
            publicPage.set_value(input_loc, public_reserve_fund)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_public_reserve_fund=>', str(e))

    # 公积金公司缴纳金额
    # comp_public_reserve_fund:公积金公司缴纳金额（number）
    def set_comp_public_reserve_fund(self, public_reserve_fund):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                comp_public_reserve_fund_elem)
            publicPage.set_value(input_loc, comp_public_reserve_fund)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_comp_public_reserve_fund=>', str(e))

    # 公积金个人缴纳金额
    # pers_public_reserve_fund:公积金个人缴纳金额（number）
    def set_pers_public_reserve_fund(self, public_reserve_fund):
        try:
            publicPage = PublicPage(self.driver)
            input_loc = self.driver.find_element_by_xpath(
                pers_public_reserve_fund_elem)
            publicPage.set_value(input_loc, pers_public_reserve_fund)
        except Exception as e:
            print(
                '[AddStuffPage] There was an exception when set_pers_public_reserve_fund=>', str(e))

    # 保存
    def save(self):
        try:
            publicPage = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(save_btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print('[AddStuffPage] There was an exception when save=>', str(e))

    # 取消
    def cancel(self):
        try:
            publicPage = PublicPage(self.driver)
            btn_loc = self.driver.find_element_by_xpath(cancel_btn_elem)
            publicPage.click_elem(btn_loc)
        except Exception as e:
            print('[AddStuffPage] There was an exception when cancel=>', str(e))

    # 添加员工base
    # stuff_info[1]:姓名
    # stuff_info[2]:国籍
    # stuff_info[3]:身份证号
    # stuff_info[9]:是否雇员
    def add_stuff_base(self, stuff_info):
        publicPage = PublicPage(self.driver)
        random_num = str(publicPage.random_num(10000000000))
        salaryPage = SalaryPage(self.driver)
        salaryPage.go_to_add_stuff_page()
        if stuff_info[3] == '':
            random_num = ''
        else:
            random_num = random_num
        self.set_name(stuff_info[1])
        self.select_country(stuff_info[2])
        self.set_id(stuff_info[3] + random_num)
        self.select_employed(stuff_info[9])
        self.save()

    # 员工基本信息
    #
    def set_stuff_base_info(self, stuff_info):
        random_num = str(publicPage.random_num(10000000000))
        if stuff_info[3] == '':
            random_num = ''
        else:
            random_num = random_num
        self.set_num(stuff_info[0])
        self.set_name(stuff_info[1])
        self.select_country(stuff_info[2])
        self.set_id(stuff_info[3] + random_num)
        self.select_sex(stuff_info[5])
        self.select_partment(stuff_info[7])
        self.set_position(stuff_info[8])
        self.select_employed(stuff_info[9])
        self.set_capital(stuff_info[10])
        self.select_health(stuff_info[11])
        self.select_office_status(stuff_info[12])
        self.set_phone(stuff_info[13])
        self.set_email(stuff_info[14])
        self.set_address(stuff_info[15])
        self.select_registered_type(stuff_info[16])
        self.set_openning_bank(stuff_info[17])
        self.set_bank_num(stuff_info[18])

    # 基本工资
    def set_salary_base_info(self, stuff_info):
        self.set_basic_salary(stuff_info[19])
        self.set_actual_salary(stuff_info[20])

    # 医疗／养老保险缴纳基数
    def set_basic_insurance_payment(self, stuff_info):
        self.set_medicare_base(stuff_info[21])
        self.set_pension_base(stuff_info[22])

    # 个人社保缴纳
    def set_pers_social_security(self, stuff_info):
        self.set_pers_medicare(stuff_info[23])
        self.set_pers_pension_insurance(stuff_info[24])
        self.set_pers_unemploy_insurance(stuff_info[25])

    # 公司社保缴纳
    def set_comp_social_security(self, stuff_info):
        self.set_comp_medicare(stuff_info[26])
        self.set_comp_pension_insurance(stuff_info[27])
        self.set_comp_unemploy_insurance(stuff_info[28])
        self.set_comp_birth_insurance(stuff_info[29])
        self.set_comp_injury_insurance(stuff_info[30])

    # 公积金
    def set_fund(self, stuff_info):
        self.set_public_reserve_fund(stuff_info[31])
        self.set_comp_public_reserve_fund(stuff_info[32])
        self.set_pers_public_reserve_fund(stuff_info[33])
