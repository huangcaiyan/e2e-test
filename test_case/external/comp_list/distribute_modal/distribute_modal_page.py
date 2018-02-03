from selenium import webdriver
import time

from .distribute_modal_elem import *
from util.public_page import PublicPage
from ..comp_list_page import CompListPage
from ...navigation.topbar.topbar_page import TopBarPage
from ...personal_info_modal.personal_info_modal_page import PersonalInfoModalPage


# @Time :18/1/19 上午11:46
# @Author :huangcaiyan
# @File : distribute_modal_page
# @Software : PyCharm
class DistributeModalPage( object ):
    
    def __init__( self , driver ):
        self.driver = driver  # self.driver = webdriver.Chrome()
    
    def invite_user( self , user_info ):
        """
        :param user_info: 用户名｛0:会计／助理／客户联系人，1:帐套名称［当等于current_user时，默认分配当前登陆用户］，2:用户名，3:手机号｝
        :return: 选择／邀请用户
        """
        publicPage = PublicPage( self.driver )
        topBarPage = TopBarPage( self.driver )
        compListPage = CompListPage( self.driver )
        compListPage.click_distribute_btn( user_info[ 0 ] , user_info[ 1 ] )
        names = self.get_name_list()
        
        if user_info[ 2 ] in names:
            self.select_name( user_info[ 2 ] )
        elif user_info[ 2 ] == 'current_user':
            current_user = topBarPage.get_login_user_name()
            self.select_name( current_user )
        elif user_info[ 3 ] not in self.get_phone_list():
            drop_loc = self.driver.find_element_by_xpath( name_drop_elem )
            publicPage.click_elem( drop_loc )
            name_loc = self.driver.find_element_by_partial_link_text( '+新增用户' )
            publicPage.click_elem( name_loc )
            self.set_name( user_info[ 0 ] )
            self.set_phone( user_info[ 1 ] )
        self.submit( 'save' )
    
    # ------------------------------------------------------------------------------------------------------------------
    
    def get_name_list( self ):
        """
        :return: 返回已经邀请过的用户名
        """
        publicPage = PublicPage( self.driver )
        drop_loc = self.driver.find_element_by_xpath( name_drop_elem )
        publicPage.click_elem( drop_loc )
        names_loc = self.driver.find_element_by_tag_name( 'ul' ).find_elements_by_tag_name( 'li' )
        names = [ ]
        for name_loc in names_loc:
            name = name_loc.find_element_by_xpath( 'div/a/div[2]' ).text
            names.append( name )
        print( names )
        return names
    
    def get_phone_list( self ):
        """
        :return: 返回已经邀请过的手机号
        """
        phones = [ ]
        names = self.get_name_list()
        for name in names:
            if names.index( name ) != 0:
                self.select_name( name )
                phone_loc = self.driver.find_element_by_xpath( phone_text_elem )
                phone = phone_loc.get_attribute( 'value' )
                phones.append( phone )
        print( 'phones=' , phones )
        return phones
    
    def set_name( self , name ):
        """
        :param name: 姓名
        :return:输入姓名
        """
        publicPage = PublicPage( self.driver )
        input_loc = self.driver.find_element_by_xpath( name_input_elem )
        publicPage.set_value( input_loc , name )
    
    def set_phone( self , phone_num ):
        """
        :param phone_num: 手机号
        :return:输入手机号
        """
        publicPage = PublicPage( self.driver )
        input_loc = self.driver.find_element_by_xpath( phone_input_elem )
        publicPage.set_value( input_loc , phone_num )
    
    def click_add_more_link( self ):
        """
        :return: 点击继续添加
        """
        publicPage = PublicPage( self.driver )
        link_loc = self.driver.find_element_by_partial_link_text( '继续添加' )
        publicPage.click_elem( link_loc )
    
    def select_name( self , user_name ):
        publicPage = PublicPage( self.driver )
        names = self.get_name_list()
        name_index = names.index( user_name )
        name_loc = self.driver.find_element_by_tag_name( 'ul' ).find_elements_by_tag_name( 'li' )[
            name_index ].find_element_by_xpath( 'div/a/div[2]' )
        publicPage.click_elem( name_loc )
    
    def submit( self , btn_name ):
        """
        :param btn_name: 按钮名称，可选值(save,cancel)
        :return:点击保存、取消按钮
        """
        if btn_name == 'save':
            submit_elem = save_elem
        elif btn_name == 'cancel':
            submit_elem = cancel_elem
        publicPage = PublicPage( self.driver )
        btn_loc = self.driver.find_element_by_xpath( submit_elem )
        return publicPage.click_elem( btn_loc )
