from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from util.public_page import PublicPage
from .personal_info_modal_elem import *
from ..comp_list.comp_list_page import CompListPage


# @Time :18/1/19 上午11:46
# @Author :huangcaiyan
# @File : personal_info_modal_page
# @Software : PyCharm

class PersonalInfoModalPage:
    
    def __init__( self , driver ):
        self.driver = driver  # self.driver = webdriver.Chrome()
    
    def modify_password( self , data ):
        compListPage = CompListPage( self.driver )
        compListPage.click_modify_password_link()
        WebDriverWait( self.driver , 30 , 1 ).until(
            lambda driver: self.driver.find_element_by_css_selector( modal_title_elem ) )
        self.set_old_password( data[ 0 ] )
        self.set_new_password( data[ 1 ] )
        self.set_confirm_password( data[ 2 ] )
        self.submit( data[ 3 ] )
    
    # -------------------------------------------------------------------------------------------------------------------
    
    def get_modal_title( self ):
        """
        获取modal框标题
        :return:标题（个人信息）
        """
        publicPage = PublicPage( self.driver )
        title_loc = self.driver.find_element_by_css_selector( modal_title_elem )
        publicPage.get_value( title_loc )
    
    def get_phone_num( self ):
        """
        :return:获取当前用户的手机号
        """
        publicPage = PublicPage( self.driver )
        num_loc = self.driver.find_element_by_id( phone_elem )
        publicPage.get_value( num_loc )
    
    def set_old_password( self , old_password ):
        """
        输入原密码
        :param old_password: 原密码
        """
        publicPage = PublicPage( self.driver )
        input_loc = self.driver.find_element_by_name( old_password_elem )
        publicPage.set_value( input_loc , old_password )
    
    def set_new_password( self , new_password ):
        """
        设置新密码
        :param new_password: 新密码
        """
        publicPage = PublicPage( self.driver )
        input_loc = self.driver.find_element_by_name( new_password_elem )
        publicPage.set_value( input_loc , new_password )
    
    def set_confirm_password( self , confirm_password ):
        """
        设置确认密码
        :param confirm_password: 确认密码
        """
        publicPage = PublicPage( self.driver )
        input_loc = self.driver.find_element_by_name( confirm_password_elem )
        publicPage.set_value( input_loc , confirm_password )
    
    def submit( self , btn_name ):
        """
        点击保存或取消按钮
        :param btn_name: 按钮名称,可选值(save,cancel)
        """
        if btn_name == 'save':
            btn_elem = save_btn_elem
            operation_name = '保存'
        elif btn_name == 'cancel':
            btn_elem = cancel_btn_elem
            operation_name = '取消'
        else:
            btn_elem = None
            print( '按钮名称输入错误，请检查输入值。' )
        print( '正在做' + operation_name + '修改的操作：' )
        publicPage = PublicPage( self.driver )
        btn_loc = self.driver.find_element_by_id( btn_elem )
        publicPage.click_elem( btn_loc )
