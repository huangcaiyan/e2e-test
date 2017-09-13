import requests
import json
import xlrd
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../'))
from config import *

class CallJournalEntrySearchApi(object):

    def __init__(self):
        # self.url = '/api/v1/journal/search?year=2017&month=8&keyword=&pageIndex=2&pageSize=10&type='
        self.pageCount = 0

    def get_pageCount(self):
        return self.pageCount

    #调用查询凭证API接口,默认查询第一页 auComAcc [Authorization,company_id,accountbook_id] , urlPara 页数
    def callJournalEntrySearchApi(self,auComAcc,urlPara='1'):
        subUrl = '/api/v1/journal/search?year=2017&month=8&keyword=&pageIndex=' + urlPara + '&pageSize=10&type='
        url = ApiBaseUrl + subUrl
        headers = {
            'Accept':'application/json',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Content-Type':'application/json',

            # 'Authorization':'bearer 3atE5AZ3s8yxFdB9hjm7hh0d-46Fzn1kuW5hwg1s58hui8dKLYHGDFYGMeyDQj8jdnwcQB0L0Wt5LlOl50-bUmXp9RE88c27uveRUBEbTdl5vCAJus2H3GasiV4319moJkDW4A3VIZNrM91JBfsZbaL5L_ug8ncp5AMXvN4fMwtQHDoAuBFOVEKUJ9tZTFV6GUJCAxIqOhzxurmnuLKTva0uc9uM4lHOOCT8f6OXgoczSxtuMsKblUKpU5B2a0ZGTeUth76LniNdy8JIuURxji7w96A',
            # 'company_id':'5a8a5e65-0f17-4353-815a-9046199c6f5b',
            # 'accountbook_id':'a1786e72-6dbb-4847-82ff-573d23ef8468',

            'Host':'api-firms.guanplus.com',
            'Origin':'https://firms.guanplus.com',
            'Referer':'//firms.guanplus.com/app/finance/voucher',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        headers['Authorization'] = auComAcc[0]
        headers['company_id'] = auComAcc[1]
        headers['accountbook_id'] = auComAcc[2]
        request = requests.get(url,headers = headers)
        resposeData = json.loads(request.text)
        self.pageCount = resposeData['pageCount']
        if 'errors' in resposeData.keys():
            print('======================================== JournalEntrySearchApi is error start ========================================================')
            print(resposeData)
            print('======================================== JournalEntrySearchApi is error end   ========================================================')
        else:
            return resposeData

    #获取凭证列表数据并重组校验数据，如{'journalNumber':"1","accountCode":"560301","accountName":"利息费用","dcDirection":"Debit","amount":"111"} 
    #参数：auComAcc [Authorization,company_id,accountbook_id]
    def getJournalList(self,auComAcc,urlPara):
        resposeData = self.callJournalEntrySearchApi(auComAcc,urlPara)
        journalList = resposeData['list']
        checkJournalList = []
        for i in journalList:
            journalEntryLineItemList = i['journalEntryLineItemModels']
            for j in journalEntryLineItemList:
                checkJournalItemDict = {}
                checkJournalItemDict['journalNumber'] = i['journalEntryNumber']
                checkJournalItemDict['accountCode'] = j['account']['id']
                checkJournalItemDict['accountName'] = j['account']['name']
                checkJournalItemDict['dcDirection'] = j['debitCreditType']
                checkJournalItemDict['amount'] = str(j['amount'])
                checkJournalList.append(checkJournalItemDict)

        return checkJournalList

# callApi = CallJournalEntrySearchApi()
# #生成器
# def journalListGenerator(auComAcc,pageCount):
#     n = 1
#     while n < pageCount + 1:
#         yield callApi.getJournalList(auComAcc,str(n))
#         n += 1
# jlists = journalListGenerator('sd',16)
# for i in jlists:
#     print(i)
