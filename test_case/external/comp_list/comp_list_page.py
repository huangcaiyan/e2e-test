from selenium import webdriver
import unittest , time
import re

from util.public_page import PublicPage
from .comp_list_elem import *
from comp_info import CompInfo
from test_case.login.login_page import LoginPage


# @Time :18/1/19 上午11:46
# @Author :huangcaiyan
# @File : comp_list_page
# @Software : PyCharm

class CompListPage( object ):
    def __init__( self , driver ):
        self.driver = driver
    
    def go_create_ways_page( self ):
        """
        页面跳转至创建帐套方式页面
        """
        publicPage = PublicPage( self.driver )
        self.driver.get( CompInfo.BASE_URL + '/create-ways' )
        if not publicPage.wait_until_loader_disapeared():
            if '/create-ways' in self.driver.current_url:
                print( '创建帐套方式页面now' )
            else:
                print( '－－去创建帐套方式页面 失败！' )
                exit()
        else:
            print( '－－加载效果未消失，请求超时！' )
    
    def go_to_create_comp_page( self ):
        """
        页面跳转至创建帐套页面
        """
        publicPage = PublicPage( self.driver )
        self.driver.get( CompInfo.BASE_URL + '/create-company' )
        if not publicPage.wait_until_loader_disapeared():
            if '/create-company' in self.driver.current_url:
                print( '创建帐套页面now' )
            else:
                print( '－－去创建帐套页面失败！' )
                exit()
        else:
            print( '－－加载效果未消失，请求超时！' )
            exit()
    
    def get_comp_num( self ):
        """
        :return:返回帐套数量
        """
        text_loc = self.driver.find_element_by_xpath( comp_num_elem )
        publicPage = PublicPage( self.driver )
        text = publicPage.get_value( text_loc )
        comp_num = re.findall( '\d+' , text )
        print( 'comp_num=' , comp_num[ 0 ] )
        return comp_num[ 0 ]
    
    # 点击创建帐套按钮
    def click_create_comp_btn( self ):
        try:
            public_page = PublicPage( self.driver )
            btn_loc = self.driver.find_element_by_xpath( create_comp_btn_elem )
            public_page.click_elem( btn_loc )
        except Exception as e:
            print( '[CompListPage]点击创建帐套按钮失败=>' , str( e ) )
    
    def get_accounting_book_property( self , accounting_book_name ):
        """
        :param accounting_book_name: 帐套名称
        :return:帐套类型
        """
        table = self.driver.find_element_by_tag_name( 'table' )
        trList = table.find_elements_by_tag_name( 'tr' )
        print( 'trList=>' , trList )
        table_value = [ ]
        for row in trList:
            tdList = row.find_elements_by_tag_name( 'td' )
            cell_value = [ ]
            for col in tdList:
                value = col.text
                cell_value.append( value )
            table_value.append( cell_value )
        print( 'table_value=>' , table_value )
        
        for name in cell_value:
            if accounting_book_name == name:
                tr_index = cell_value.index()
            print( 'tr_index=>' , tr_index )
        
        accounting_book_property_elem = '//*[@id="company-table"]/tbody/tr[' + tr_index + ']/td[3]/div/span'
        accounting_book_property_loc = self.driver.find_element_by_xpath( accounting_book_property_elem )
        accounting_book_property = accounting_book_property_loc.text
        print( 'accounting_book_property=>' , accounting_book_property )
        return accounting_book_property
    
    def get_comp_name_list( self ):
        """
        :return:获取帐套列表中所有帐套名称，并以list的形式返回。
        """
        publicPage = PublicPage( self.driver )
        tr_locs = self.driver.find_element_by_tag_name( 'tbody' ).find_elements_by_tag_name( 'tr' )
        names = [ ]
        for tr_loc in tr_locs:
            tr_index = tr_locs.index( tr_loc )
            if len( tr_locs[ tr_index ].find_elements_by_tag_name( 'a' ) ) == 2:
                name_xpath = 'td[1]/div/div/a[2]'
            else:
                name_xpath = 'td[1]/div/div/a'
            name_loc = tr_locs[ tr_index ].find_element_by_xpath( name_xpath )
            name = publicPage.get_value( name_loc )
            names.append( name )
        print( 'comp_name_list=' , names )
        return names
    
    def enter_comp( self , comp_name=None ):
        """
        :param comp_name: 帐套名称(当帐套名称为空时，默认进入最后一个帐套）
        :return: 点击帐套名称进入帐套
        """
        try:
            publicPage = PublicPage( self.driver )
            if comp_name is None:
                tr_locs = self.driver.find_element_by_tag_name( 'tbody' ).find_elements_by_tag_name( 'tr' )
                index = int( self.get_comp_num() ) - 1
                print( 'index=' , index )
                if len( tr_locs[ index ].find_elements_by_tag_name( 'a' ) ) == 2:
                    print( '1' )
                    name_xpath = 'td[1]/div/div/a[2]'
                else:
                    print( '2' )
                    name_xpath = 'td[1]/div/div/a'
                name_loc = tr_locs[ index ].find_element_by_xpath( name_xpath )
                comp_name = publicPage.get_value( name_loc )
                print( 'comp_name=' , comp_name )
            comp_loc = self.driver.find_element_by_partial_link_text( comp_name )
            publicPage.click_elem( comp_loc )
        except Exception as e:
            print( '[CompListPage]enter_comp：进入帐套失败，失败原因=>' , str( e ) )
    
    def click_distribute_btn( self , role , comp_name=None ):
        """
        :param comp_name:帐套名称（当公司名称为空时，默认分配最后一个帐套⚠️）
        :param role:要分配的角色，可选值（客户联系人，会计，助理）
        :return:点击填写／分配按钮
        """
        publicPage = PublicPage( self.driver )
        row_locs = self.driver.find_element_by_tag_name( 'tbody' ).find_elements_by_tag_name( 'tr' )
        names = [ ]
        for tr_index in range( len( row_locs ) ):
            a_loc = self.driver.find_element_by_tag_name( 'tbody' ).find_elements_by_tag_name( 'tr' )[
                tr_index ].find_element_by_tag_name( 'td' ).find_elements_by_tag_name( 'a' )
            if len( a_loc ) == 1:
                name_loc = a_loc[ 0 ]
            elif len( a_loc ) == 2:
                name_loc = a_loc[ 1 ]
            
            name = name_loc.text
            names.append( name )
        # 获取当前帐套名称所在行索引
        if comp_name is None:
            print( 'kong ' )
            index = self.get_comp_num()
        else:
            index = names.index( comp_name ) + 1
        if role == '客户联系人':
            distribute_td_index = 4
        elif role == '会计':
            distribute_td_index = 5
        elif role == '助理':
            distribute_td_index = 6
        distribute_elem = 'tr[' + str( index ) + ']/td[' + str( distribute_td_index ) + ']/div'
        distribute_loc = self.driver.find_element_by_tag_name( 'tbody' ).find_element_by_xpath( distribute_elem )
        class1 = distribute_loc.find_element_by_tag_name( 'div' ).get_attribute( 'class' )
        print( 'class1=' , class1 )
        
        # if 'unassign' in class1:
        publicPage.click_elem( distribute_loc )
        time.sleep( 2 )
    
    # －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－


'//*[@id="company-table"]/tbody/tr[95]/td[1]/div/div/a[2]'
