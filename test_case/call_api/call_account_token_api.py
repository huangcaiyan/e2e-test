import requests
import json
import xlrd
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../../'))
from config import *

__author__ = u'ych'

class CallAccountTokenApi(object):
    def __init__(self):
        self.url = '/api/v1/account/token'

    def callTokenApi(self):
        url = IdentityApiBaseUrl + self.url
        data = {"application":"GuanYouZhang"}
        wb = xlrd.open_workbook(os.path.dirname(__file__) + '/' + '../../test_data/' + '创建公司.xlsx')
        sh = wb.sheet_by_name(u'登陆账号')
        loginData = sh.row_values(1)
        data['userName'] = loginData[0]
        data['password'] = loginData[1]
        requestApi = requests.post(url,data=data)
        resposeData = json.loads(requestApi.text)
        
        return resposeData

    #获取authorization和company_id
    def getAuthorizationComid(self):
        resposeData = self.callTokenApi()
        authorization = resposeData['token_type'] + ' ' + resposeData['access_token']
        company_id = resposeData['user']['currentCompany']['id']
        result = [authorization,company_id]

        return result