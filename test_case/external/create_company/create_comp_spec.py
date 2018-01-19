from selenium import webdriver
import unittest, time
from .create_comp_page import CreateCompPage
from util.read_excel import ReadExcel
from util.public_page import PublicPage
from util.danger_page import DangerPage
from test_case.login.login_page import LoginPage
from comp_info import CompInfo
from ..comp_list.comp_list_page import CompListPage

'''
进入帐套
创建于2017-09-29-五
caicai
'''


class CreateCompSpec(unittest.TestCase):
    create_comp_data_dir = './test_data/cai/external/创建帐套测试数据.xlsx'

    @classmethod
    def setUpClass( self ):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        PublicPage(self.driver).max_window()
        self.driver.maximize_window()

        loginPage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginPage.login(CompInfo.LOGIN_DATA)

    @classmethod
    def tearDownClass( self ):
        self.driver.quit()

    def test_verify_create_comp( self ):
        """确认创建帐套功能，创建成功"""
        page = CreateCompPage(self.driver)
        readExcel = ReadExcel(self.create_comp_data_dir)
        comp_data = readExcel.get_value_by_row('创建帐套测试数据', 1)
        compLisPage = CompListPage(self.driver)
        compLisPage.go_to_create_comp_page()
        if 'create-company' in self.driver.current_url:
            page.set_comp_base_info(comp_data)
            page.set_comp_detail_info(comp_data)
            time.sleep(2)
            self.assertIn('company-list', self.driver.current_url)
        else:
            print('去创建帐套失败！')
            self.assertEqual(0, 1)

    def test_create_comp_empty_comp_name( self ):
        """创建帐套-帐套名称为空,红框提醒保存失败"""
        page = CreateCompPage(self.driver)
        dangerPage = DangerPage(self.driver)
        compLisPage = CompListPage(self.driver)
        readExcel = ReadExcel(self.create_comp_data_dir)

        comp_data = readExcel.get_value_by_row('创建帐套测试数据', 2)
        compLisPage.go_to_create_comp_page()
        if 'create-company' in self.driver.current_url:
            page.set_comp_base_info(comp_data)
            page.submit(comp_data[17])
            alert_danger_msg = dangerPage.get_alert_danger_msg()
            self.assertEqual(alert_danger_msg, comp_data[19])
            time.sleep(2)
            self.assertNotIn('company-list', self.driver.current_url)
        else:
            print('去创建帐套失败！')
            self.assertEqual(0, 1)

    def test_create_comp_empty_legal_person( self ):
        """创建帐套－公司性质为空，红框提醒，保存失败"""
        page = CreateCompPage(self.driver)
        publicPage = PublicPage(self.driver)
        readExcel = ReadExcel(self.create_comp_data_dir)
        excel_date = readExcel.get_value_by_row('创建帐套测试数据', 3)
        for comp_data in excel_date:
            page.set_comp_base_info(comp_data)
        result = publicPage.has_danger_is_show()
        self.assertEqual(result, 1)
        self.assertNotIn('company-list', self.driver.current_url)

    def test_create_comp_not_type_comp_detail_info( self ):
        """创建帐套－帐套详细信息不填写，保存失败，红框提醒"""
        page = CreateCompPage(self.driver)
        publicPage = PublicPage(self.driver)
        read_excel = ReadExcel(self.create_comp_data_dir)
        excel_data = read_excel.get_value_by_row('创建帐套测试数据', 4)
        for comp_data in excel_data:
            page.set_comp_base_info(comp_data)
            page.set_comp_detail_info(comp_data)
        result = publicPage.has_danger_is_show()
        self.assertEqual(result, 1)
        self.assertNotIn('company-list', self.driver.current_url)

    def test_create_comp_empty_legal_person( self ):
        """创建帐套－成立日期为空，红框提醒，保存失败"""
        page = CreateCompPage(self.driver)
        publicPage = PublicPage(self.driver)
        readExcel = ReadExcel(self.create_comp_data_dir)
        excel_date = readExcel.get_value_by_row('创建帐套测试数据', 5)
        for comp_data in excel_date:
            page.set_comp_base_info(comp_data)
            page.set_comp_detail_info(comp_data)
        result = publicPage.has_danger_is_show()
        self.assertEqual(result, 1)
        self.assertNotIn('company-list', self.driver.current_url)


if __name__ == '_main_':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(CreateCompSpec('test_confirm_create_account_book'))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
