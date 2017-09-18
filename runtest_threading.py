import unittest,time,os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from HTMLTestRunner import HTMLTestRunner
from test_case.transaction.record_outcome_spec import RecordOutcomeSpec
from test_case.transaction.record_income_spec import RecordIncomeSpec
from test_case.transaction.record_transfer_spec import RecordTransterSpec
from test_case.transaction.outcome_voucher_spec import OutcomeVoucherSpec
from test_case.invoice.record_input_invoice_spec import RecordInputInvoiceSpec
from test_case.invoice.record_output_invoice_spec import RecordOutputInvoiceSpec
from test_case.finance.voucher.generate_voucher_spec import GenerateVoucherSpec
from test_case.fixedassets.record_fixed_spec import RecordFixedSpec
from test_case.fixedassets.record_intangible_spec import RecordIntangibleSpec
from test_case.finance.voucher.record_business_spec import RecordBusinessSpec
from test_case.business_flow.positive_flow_spec import PositiveFlowSpec
from test_case.business_flow.positive_flow_specb import PositiveFlowSpec1
# from test_case.dashbaord.assistant_dashbaord_spec import AssistantDashbaordSPec
from test_case.dashbaord.assistant_dashbaord_spec import AssistantDashbaordSPec
import threading
from selenium.webdriver import Remote

#发送邮件
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    smtpserver = 'smtp.163.com'
    user = '18514509382@163.com'
    password = 'yang115817'
    sender = '18514509382@163.com'
    receiver = 'yangchunhong@concordya.com'

    msg = MIMEMultipart()
    msg['From'] = '18514509382@163.com'
    msg['Subject'] = Header(u'自动化测试报告','utf8').encode()
    msg['To'] = 'yangchunhong@concordya.com'
    msg.attach(MIMEText(mail_body,'html','utf-8'))
    smtp = smtplib.SMTP(smtpserver,25)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()

#查找最新的测试报告
def find_new_report(testReport):
    lists = os.listdir(testReport)
    lists.sort(key=lambda fn:os.path.getmtime(testReport + '//' + fn))
    file_new = os.path.join(testReport,lists[-1])
    return file_new

def runTest(testSuite,name):
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_dir = './report'
    filename = report_dir + '/' + now + '_' + name + '_result.html'
    testReport = open(filename,'wb')
    # runner = HTMLTestRunner(stream = testReport,title = "管有账测试报告",description='测试用例执行情况：')
    runner = unittest.TextTestRunner()
    runner.run(testSuite)
    testReport.close()

#记固定资产
def runRecordFixedSpec(testCase):
    testSuite = unittest.TestSuite()
    testSuite.addTest(RecordFixedSpec(testCase))

    runTest(testSuite,'RecordFixedSpec')
#记无形资产
def runRecordIntangibleSpec(testCase):
    testSuite = unittest.TestSuite()
    testSuite.addTest(RecordIntangibleSpec(testCase))

    runTest(testSuite,'RecordIntangibleSpec')

#导入
def importFile(testCase):
    
    testSuite = unittest.TestSuite()
    testSuite.addTest(AssistantDashbaordSPec(testCase))

    runTest(testSuite,'RecordFixedSpec')

#记收入
def runRecordIncomeSpec():
    testSuite = unittest.TestSuite()
    testSuite.addTest(RecordIncomeSpec('test8'))

    runTest(testSuite,'RecordFixedSpec')

#记支出
def runRecordOutcomeSpec():
    testSuite = unittest.TestSuite()
    testSuite.addTest(RecordOutcomeSpec('test8'))

    runTest(testSuite,'RecordFixedSpec')

#记账户互转
def runRecordTransterSpec():
    testSuite = unittest.TestSuite()
    testSuite.addTest(RecordTransterSpec('test8'))

    runTest(testSuite,'RecordFixedSpec')

#记收票
def runRecordInputInvoiceSpec(testCase):
    testSuite = unittest.TestSuite()
    testSuite.addTest(RecordInputInvoiceSpec(testCase))

    runTest(testSuite,'RecordFixedSpec')

#记开票
def runRecordOutputInvoiceSpec(testCase):
    testSuite = unittest.TestSuite()
    testSuite.addTest(RecordOutputInvoiceSpec(testCase))

    runTest(testSuite,'RecordFixedSpec')

#流程
def runPositive(testCase):
    testSuite = unittest.TestSuite()
    testSuite.addTest(PositiveFlowSpec1(testCase))

    runTest(testSuite,'RecordFixedSpec')


if __name__ == '__main__':
    
    threads = []
    #流程
    t1 = threading.Thread(target=runPositive,args=('test1',))
    t2 = threading.Thread(target=runPositive,args=('test2',))
    t3 = threading.Thread(target=runPositive,args=('test3',))
    t4 = threading.Thread(target=runPositive,args=('test4',))
    t5 = threading.Thread(target=runPositive,args=('test5',))
    t6 = threading.Thread(target=runPositive,args=('test6',))
    t7 = threading.Thread(target=runPositive,args=('test7',))
    t8 = threading.Thread(target=runPositive,args=('test8',))
    t9 = threading.Thread(target=runPositive,args=('test9',))
    t10 = threading.Thread(target=runPositive,args=('test10',))
    # threads = [t1,t2,t3,t4]
    threads = [t5,t6,t7,t8]


    #导入
    # t1 = threading.Thread(target=importFile,args=('test1',))
    # t2 = threading.Thread(target=importFile,args=('test2',))
    # t3 = threading.Thread(target=importFile,args=('test3',))
    # threads = [t1,t2,t3]
    

    # # for t in threads:
    # #     t.start()

    # # for t in threads:
    # #     t.join()
    # # threads.append(t2)

    # # #记收支
    # specList = [runRecordIncomeSpec,runRecordOutcomeSpec]
    # for i in specList:
    #     t = threading.Thread(target=i)
    #     threads.append(t)
   
    # # # #记固定资产
    # t1 = threading.Thread(target=runRecordFixedSpec,args=('test1',))
    # t2 = threading.Thread(target=runRecordFixedSpec,args=('test2',))
    # t3 = threading.Thread(target=runRecordIntangibleSpec,args=('test1',))
    # t4 = threading.Thread(target=runRecordIntangibleSpec,args=('test2',))
    # threads = [t1,t2,t3,t4]

    #记收票
    # t1 = threading.Thread(target=runRecordInputInvoiceSpec,args=('test2',))
    # t2 = threading.Thread(target=runRecordOutputInvoiceSpec,args=('test2',))
    # t2 = threading.Thread(target=runRecordOutputInvoiceSpec,args=('test1',))
    # t3 = threading.Thread(target=runRecordOutputInvoiceSpec,args=('test2',))
    # threads = [t1,t2]

    for t in threads:
        t.start()
        # t.join()

    for t in threads:
        t.join()
