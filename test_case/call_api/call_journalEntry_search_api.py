import requests
import json
import xlrd
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../../../'))
from config import *

class CallJournalEntrySearchApi(object):

    def __init__(self):
        self.url = '/api/v1/journal/search?year=2017&month=8&keyword=&pageIndex=1&pageSize=10&type='

    def callJournalEntrySearchApi(self,auComAcc):
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
        headers['Authorization'] = auComAcc[0]
        headers['company_id'] = auComAcc[1]
        headers['accountbook_id'] = auComAcc[2]
        request = requests.get(url,headers = headers)
        resposeData = json.loads(request.text)
        if 'errors' in resposeData.keys():
            print('======================================== JournalEntrySearchApi is error start ========================================================')
            print(resposeData)
            print('======================================== JournalEntrySearchApi is error end   ========================================================')
        else:
            return resposeData

    #获取凭证列表数据并重组校验数据，如{'journalNumber':"1","accountCode":"560301","accountName":"利息费用","dcDirection":"Debit","amount":"111"} 
    def getJournalList(self,auComAcc):
        resposeData = self.callJournalEntrySearchApi(auComAcc)
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
                checkJournalItemDict['amount'] = str(round(int(j['amount'])))
                checkJournalList.append(checkJournalItemDict)

        return checkJournalList
