import requests
import json

__author__ = u'ych'

#stage company_id = '3a05a8b3-405f-4500-91af-e203d79fe179'
def testGetApi():
    url = 'https://api-firms.guanplus.com/api/v1/journal/search?year=2017&month=9&keyword=&pageIndex=2&pageSize=10&type='
    headers = {
        'Accept':'application/json',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        #账套id
        # 'accountbook_id':'1d6c7113-442f-4ec5-9097-63fcc93ccfea',
        #token
        # 'Authorization':'bearer 5NRm-LGEuo1EYMVTc6LPa2dS2XNET0_t2DAxw8DOpuXU72go0ayEp2VJOgu4xsLJ8LfaCUoo25GEGdNYWhZN5VSoNzTY09HTr8LDwtLywCUeuJ6LbTuvVPfLO6v-xeSdVWbeDQk2hIavG96D6MR3FzTB56k0hrvMxI9St7lAjrKJOONjcMTzQ4bzhXy_4qbs7WjNu0G_bWkHGE552O6LtVL2wg2mYa5gZ0xLoGUy6I6ahDEdhd8fkK8o8JvnEsoMHyJTT7ZHSb_f-T-Sg5UjVWRVHMM',
        'Cache-Control':'no-cache',
        #公司id
        # 'company_id':'5a8a5e65-0f17-4353-815a-9046199c6f5b',
        'Connection':'keep-alive',
        'Content-Type':'application/json',
        #主机地址
        'Host':'api-firms.guanplus.com',
        'Origin':'https://firms.guanplus.com',
        'Referer':'//firms.guanplus.com/app/finance/voucher',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
    }
    #调用token的api
    urlPost = 'https://api-identity.guanplus.com/api/v1/account/token'
    data = {"userName": "18514509382","password": "qq123456"}
    rPost = requests.post(url,data=data)
    au = json.loads(rPost.text)
    headers['Authorization']=au['token_type'] + ' ' + au['access_token']
    headers['company_id'] = au['user']['companies'][0]['id']

    #调用获得账套的api
    

    # headers['accountbook_id']=

    r = requests.get(url,headers = headers)
    print('api respose:')
    print(r.text.encode('utf-8'))

#获取账套api
def getAccountbook():
    accountbookSearchUrl = 'https://api-firms.guanplus.com/api/v1/accountbook/search?pageIndex=1&pageSize=0&year=0&month=0&keyword=&status=&assignStatus=All'
    headers = {
        'Accept':'application/json',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Content-Type':'application/json',
        # 'Authorization':'bearer ckoV3wI73CWWxWbBHjVl1nfok_2HSsYYdM2lvlCEWm6yVmZObpKjvep4Utpu7vNzZx_UNYcxLtr4DqW7YjBQ2yZlZZWcolJDBRwlXx049h47Ce08_JZwEWHsNWGs82k2AFIvqbaDGwor7mGznoAD7aww1yTNXnmlp4srpGtWOcjf7XX05Nd-zCCpqbvX4tCvtaqbnOC3p3Qmf9eXTXaPqRKcNnFjhuPlGfp2XQgzd2mHpa0ammaeROLJ3cbLaoR4krqgaOfEFJzPIis7Eu7bKCpdZHc',
        # 'company_id':'5a8a5e65-0f17-4353-815a-9046199c6f5b',
        'Host':'api-firms.guanplus.com',
        'Origin':'https://firms.guanplus.com',
        'Referer':'//firms.guanplus.com/app/finance/voucher',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    aucompanid = getTokenAPi()
    print('au:'+aucompanid[0])
    print('id:'+aucompanid[1])
    headers['Authorization']=aucompanid[0]
    headers['company_id']=aucompanid[1]
    r = requests.get(accountbookSearchUrl,headers = headers)
    pythonDict = json.loads(r.text)
    companyList = pythonDict['list']
    expectCompanyList = {}
    for i in companyList:
        dictId = i['id']
        dictName = i['name']
        expectCompanyList[dictId] = dictName
        
    print(expectCompanyList)
    


def getTokenAPi():
    url = 'https://api-identity.guanplus.com/api/v1/account/token'
    data = {"userName": "18514509382","password": "qq123456","application":"GuanYouZhang"}
    r = requests.post(url,data=data)
    dlo = json.loads(r.text)
    useinfp = dlo['user']
    authorization =dlo['token_type'] + ' ' + dlo['access_token']
    company_id =  dlo['user']['currentCompany']['id']
    result = [authorization,company_id]
    return result
    
#获取凭证
def getJournalList():
    url = 'https://api-accountingfirm-stage.guanplus.com/api/v1/journal/search?year=2017&month=8&keyword=&pageIndex=1&pageSize=10&type='
    headers = {
        'Accept':'application/json',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Content-Type':'application/json',
        'Authorization':'bearer 8PcsjIR--y8xEEhYgU8kr8v4ryRSAzay7gBkh5sET0eHgtY3lqVlVq-x5YqeN9pyFd0yLbHp3kMkuyWAn2avY59bWHcZhtHsQSaTcjOE5L-HvNw4-u11_gWaJoaFvWxL_gisLUOYbqDVppZQPSn4jkNA8xNM9pvQDbjIygzSZWTrgAWV1eR6h_WTxxP0EEDR5aq9AIKK3imGETPFoTc40QwDS0-ewgNF__3TZuXa540_yKgOu766n5kbN8CSuzFLOmu0Ki6A_VK-ZERxsLMdROWHsqM',
        'company_id':'3a05a8b3-405f-4500-91af-e203d79fe179',
        'accountbook_id':'89416cc4-effe-4add-bf0f-e95817cb0d0d',
        'Host':'api-firms.guanplus.com',
        'Origin':'https://firms.guanplus.com',
        'Referer':'//firms.guanplus.com/app/finance/voucher',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    }

    resposeData = requests.get(url,headers = headers)
    json2Python = json.loads(resposeData.text)
    journalList = json2Python['list']
    checkJournalList = []
    for i in journalList:
        journalEntryLineItemList = i['journalEntryLineItemModels']
        for j in journalEntryLineItemList:
            checkJournalItemDict = {}
            checkJournalItemDict['journalNumber'] = i['journalEntryNumber']
            checkJournalItemDict['accountCode'] = j['account']['id']
            checkJournalItemDict['accountName'] = j['account']['name']
            checkJournalItemDict['dcDirection'] = j['debitCreditType']
            checkJournalItemDict['amount'] = j['amount']
            checkJournalList.append(checkJournalItemDict)

    print(checkJournalList)
    

getJournalList()
# getTokenAPi()
# getAccountbook()
# testGetApi()

# from tkinter import *

# class Application(Frame):
#     def __init__(self,master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()

# app = Application()
# app.master.title('Hello World!')
# app.mainloop()

# import pymysql.cursors

# connect = pymysql.Connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     passwd='115@817&',
#     db='mysql',
#     charset='utf8'
# )
# cursor = connect.cursor()
# cursor.execute('select * from user')
# valuse = cursor.fetchall()
# print(valuse[0])
# print(len(valuse[0]))
# cursor.close()
# connect.close()

#Remote应用
# from selenium.webdriver import Remote

# dicts = {
#     'http://127.0.0.1:4444/wd/hub':'chrome',
#     'http://127.0.0.1:5555/wd/hub':'phantomjs',
#     'http://127.0.0.1:5554/wd/hub':'firefox'
# }

# for host,browser in dicts.items():
#     print(host,browser)
#     driver = Remote(command_executor=host,desired_capabilities={
#         'platform':'ANY',
#         'browserName':browser,
#         'version':'',
#         'javascriptEnabled':True
#     })
#     driver.get('http://www.baidu.com')
#     driver.find_element_by_id('kw').send_keys(browser)
#     driver.find_element_by_id('su').click()
#     driver.close()

# #网络编程
# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn',80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# s.close()

# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

#连接数据库
# import psycopg2

# conn = psycopg2.connect(database='dev_accountfirm0',user='awsuser_dba',password='C0nC0rdya!',host='gp-dev-stage-accountingfirm.cuoe2e3mlfgi.rds.cn-north-1.amazonaws.com.cn',port='5432')
# cur = conn.cursor()
# cur.execute("select * from \"Contact\"")
# rows = cur.fetchall()
# print(rows[0])
# cur.close()
# conn.close()

