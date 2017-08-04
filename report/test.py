import requests
import json

__author__ = u'ych'

def test():
    url = 'https://api-firms.guanplus.com/api/v1/invoice/8459a51b-6e10-4750-8bc1-d27687f6bf1e'
    data = {
                "userName": "18514509382",
                "password": "qq123456"

            }
    headers = {
        'Accept':'application/json',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'accountbook_id':'49fcab56-9b11-497c-bc8b-3502a3b4ad00',
        'Authorization':'bearer inR5zoqhGz3m-R7R3pcl6s7Qylmey49CExiGT2MBoHRuCGnMmUeRTtiWaIeD99rw5FI-1aw6hpJLYwlkDhATLKwMqcP2ZiWLonPpxcY7pwq10LVPM3pqpYvKHjqCgfljOBXOuIqoWYNEuNzAUMaIviJyrm7YNgwzBtY9QNolGoh41VT1O1HoR08RZfftDobfxHv_upUWOnlrZY-f4ov_X8FAz2DacVHLZE_28ZPH7FbD-l1G9wYEivTxgLJ_P0srCZpotR8l0x7U-wFUC-H-fUxttFQ',
        'Cache-Control':'no-cache',
        'company_id':'5a8a5e65-0f17-4353-815a-9046199c6f5b',
        'Connection':'keep-alive',
        'Content-Type':'application/json',
        'Host':'api-firms.guanplus.com',
        'Origin':'https://firms.guanplus.com',
        'Referer':'https://firms.guanplus.com/app/reconcile/detail/history;id=77c6c498-48ff-4b9e-b7bb-25e032b71499',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    }

    r = requests.get(url,headers = headers)
    print('resposegfffffffffffff:'+str(r.text.encode('utf-8')))


test()
