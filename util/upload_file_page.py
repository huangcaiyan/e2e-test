from selenium import webdriver
import time
import unittest
from util.public_page import PublicPage


class UploadFilePage( object ):
    def __init__( self , driver , ):
        self.driver = driver
    
    def upload_file( self , file_dir ):
        publicPage = PublicPage( self.driver )
        upload_btn_loc = self.driver.find_element_by_id( 'fileUploadBtn' )
        publicPage.is_element_present( upload_btn_loc )
        upload_btn_loc.send_keys( file_dir )  # time.sleep(5)
