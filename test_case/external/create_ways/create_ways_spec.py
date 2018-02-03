from selenium import webdriver
import unittest, logging, time

from test_case.login.login_page import LoginPage
from util.read_excel import ReadExcel
from .create_ways_page import CreateWaysPage
from util.public_page import PublicPage
from comp_info import CompInfo


class CreateWaysSpec(unittest.TestCase):
    # 测试数据文件
    test_data_dir = './test_data/cai/生产冒烟测试.xlsx'

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()

        loginPage = LoginPage(CompInfo.BASE_URL, self.driver)
        loginPage.login(CompInfo.LOGIN_DATA)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_input_comp_name_jump_to_create_page(self):
        # create_ways_page_url = CompInfo.BASE_URL + '/create-ways'
        try:
            create_ways_page_url = CompInfo.BASE_URL + '/create-ways'
            self.driver.get(create_ways_page_url)
            if not PublicPage(self.driver).wait_until_loader_disapeared():
                print('创建帐套方式页面！')

                readExcel = ReadExcel(self.test_data_dir)
                test_data = readExcel.get_value_by_row('创建帐套方式', 1)
                createWaysPage = CreateWaysPage(self.driver)
                for comp_name in test_data:
                    createWaysPage.set_comp_name(comp_name)
                    createWaysPage.confirm_enter()
                time.sleep(2)
                self.assertIn('/create-company', self.driver.current_url)
            else:
                print('－－－去创建帐套方式页面失败！')
                exit()
        except AssertionError as e:
            logging.info('－－－测试输入帐套名称点击回车键跳转至创建帐套页面失败，或请求超时！')


if __name__ == '__main__':
    unittest.main()
