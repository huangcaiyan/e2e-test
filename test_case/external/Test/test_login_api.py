from read_excel import readExcel
from pubulic_way.test_api_way import testApi
import unittest


class testLoginApi(unittest.TestCase):
    def testLoginApi(self):
        '''测试发布评伦接口。'''
        excel = readExcel(r'.test_data/cai/reqeust_test_data.xlsx')
        name = excel.get_name
        data = excel.get_data
        url = excel.get_url
        method = excel.get_method
        uid = excel.get_uid
        code = excel.get_code
        row = excel.get_row
        for i in range(0, row - 1):
            api = testApi(method[i], url[i], data[i])
            apicode = api.getCode()
            apijson = api.getJson()
            if apicode == code[i]:
                print('{}、{}:测试成功。json数据为:{}'.format(i + 1, name[i], apijson))
            else:
                print('{}、{}:测试失败'.format(i + 1, name[i]))


if __name__ == '__main__':
    unittest.main(verbosity=2)