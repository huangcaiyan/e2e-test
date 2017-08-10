# import requests
# import json

# __author__ = u'ych'

# def test():
#     url = 'https://api-firms.guanplus.com/api/v1/invoice/8459a51b-6e10-4750-8bc1-d27687f6bf1e'
#     data = {
#                 "userName": "18514509382",
#                 "password": "qq123456"

#             }
#     headers = {
#         'Accept':'application/json',
#         'Accept-Encoding':'gzip, deflate, sdch',
#         'Accept-Language':'zh-CN,zh;q=0.8',
#         'accountbook_id':'49fcab56-9b11-497c-bc8b-3502a3b4ad00',
#         'Authorization':'bearer inR5zoqhGz3m-R7R3pcl6s7Qylmey49CExiGT2MBoHRuCGnMmUeRTtiWaIeD99rw5FI-1aw6hpJLYwlkDhATLKwMqcP2ZiWLonPpxcY7pwq10LVPM3pqpYvKHjqCgfljOBXOuIqoWYNEuNzAUMaIviJyrm7YNgwzBtY9QNolGoh41VT1O1HoR08RZfftDobfxHv_upUWOnlrZY-f4ov_X8FAz2DacVHLZE_28ZPH7FbD-l1G9wYEivTxgLJ_P0srCZpotR8l0x7U-wFUC-H-fUxttFQ',
#         'Cache-Control':'no-cache',
#         'company_id':'5a8a5e65-0f17-4353-815a-9046199c6f5b',
#         'Connection':'keep-alive',
#         'Content-Type':'application/json',
#         'Host':'api-firms.guanplus.com',
#         'Origin':'https://firms.guanplus.com',
#         'Referer':'https://firms.guanplus.com/app/reconcile/detail/history;id=77c6c498-48ff-4b9e-b7bb-25e032b71499',
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
#     }

#     r = requests.get(url,headers = headers)
#     print('resposegfffffffffffff:'+str(r.text.encode('utf-8')))


# test()
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

