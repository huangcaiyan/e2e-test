import requests
import json
import xlrd
import sys
import os
ApiBaseUrl = 'https://api-firms.guanplus.com'

def callJournalEntrySearchApi():
        url = ApiBaseUrl + '/api/v1/journal/search?year=2017&month=8&keyword=&pageIndex=1&pageSize=10&type='
        headers = {
            'Accept':'application/json',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Content-Type':'application/json',
            'Authorization':'bearer q-4t-YlH93ilqBkjd79r5H45rZ5nVllr3X--2FLRi993mc5QP95U1A7K05ZyAifSraWrCOUSXuQwCquVPTgGm3jda3xUaYZma9b9Um5nWJQhveTdIyJgHPk0VIwtnkLxP40dXs-jO_OYBP_om3ahAlvQlB-tc4UvoFZ6Mz3v0WllGvLZfzAzE_f_IzdvFRSodg-eqjj08obCpqqy5joa7klAb2GZllgNiKE8yJQOf9BaS6cKvcYb0XpS5Fs3WITwMRD7xtGWFKDeBf90aK3Xq4uv0q8',
            'company_id':'5a8a5e65-0f17-4353-815a-9046199c6f5b',
            'accountbook_id':'fb8b651d-c750-4748-b623-c4168ec0e173',
            'Host':'api-firms.guanplus.com',
            'Origin':'https://firms.guanplus.com',
            'Referer':'//firms.guanplus.com/app/finance/voucher',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        # headers['Authorization'] = auComAcc[0]
        # headers['company_id'] = auComAcc[1]
        # headers['accountbook_id'] = auComAcc[2]
        request = requests.get(url,headers = headers)
        resposeData = json.loads(request.text)
        if 'errors' in resposeData.keys():
            print('======================================== JournalEntrySearchApi is error start ========================================================')
            print(resposeData)
            print('======================================== JournalEntrySearchApi is error end   ========================================================')
        else:
            print(resposeData)
            return resposeData

callJournalEntrySearchApi()