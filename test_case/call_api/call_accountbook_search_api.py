import requests
import json
import xlrd
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../../'))
from config import *

class CallAccountBookSearchApi(object):

    def __init__(self):
        self.url = '/api/v1/accountbook/search?pageIndex=1&pageSize=0&year=0&month=0&keyword=&status=&assignStatus=All'

    def callAccountbookApi(self,authorizationComid):
        url = ApiBaseUrl + self.url
        headers = {
            'Accept':'application/json',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Content-Type':'application/json',
            'Host':'api-firms.guanplus.com',
            'Origin':'https://firms.guanplus.com',
            'Referer':'//firms.guanplus.com/app/finance/voucher',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        headers['Authorization'] = authorizationComid[0]
        headers['company_id'] = authorizationComid[1]
        request = requests.get(url,headers=headers)
        resposeData = json.loads(request.text)

        return resposeData

    #获取账套id 和 names
    def getAccountBook(self,authorizationComid):
        resposeData = self.callAccountbookApi(authorizationComid) 
        companyList = resposeData['list']
        resultCompanyDict = {}
        for i in companyList:
            companyId = i['id']
            companyName = i['name']
            resultCompanyDict[companyName] = [companyId]   

        return resultCompanyDict
