import requests
import json
from read_excel import readExcel
from pubulic_way.get_token import get_token


class testApi(object):
    def __init__(self, method, url, data):
        self.method = method
        self.url = url
        self.data = data


    @property
    def testApi(self):
        # 根据不同的访问方式来访问接口
        try:
            if self.method == 'post':
                r = requests.post(self.url, data=json.dumps(eval(self.data)))
            elif self.method == 'get':
                r = requests.get(self.url, params=eval(self.data))
            return r
        except:
            print('失败')

    def getCode(self):
        # 获取访问接口的状态码
        code = self.testApi.json()['error']
        return code

    def getJson(self):
        # 获取返回信息的json数据
        json_data = self.testApi.json()
        return json_data