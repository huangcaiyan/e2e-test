import unittest
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from HTMLTestRunner import HTMLTestRunner
from test_case.login.login_spec import LoginSpec
from test_case.transaction.record_outcome_spec import RecordOutcomeSpec
from test_case.transaction.record_income_spec import RecordIncomeSpec
from test_case.transaction.record_transfer_spec import RecordTransterSpec
from test_case.invoice.record_input_invoice_spec import RecordInputInvoiceSpec
from test_case.invoice.record_output_invoice_spec import RecordOutputInvoiceSpec
from test_case.finance.voucher.generate_voucher_spec import GenerateVoucherSpec
from test_case.setting.setting_spec import SettingSpec
from test_case.setting.contact.contact_spec import ContactSpec
from test_case.salary.add_stuff.add_stuff_spec import AddStuffSpec
from test_case.external.enter_comp_spec import EnterCompSpec 

if __name__ == '__main__':
    testSuite = unittest.TestSuite()



    # 登录测试
    # testSuite.addTest(LoginSpec('test_verify_login'))
    # testSuite.addTest(LoginSpec('test_unexit_username'))
    # testSuite.addTest(LoginSpec('test_wrong_password'))
    # testSuite.addTest(LoginSpec('test_empty_username'))
    # testSuite.addTest(LoginSpec('test_empty_password'))
    # testSuite.addTest(LoginSpec('test_typeerror_username'))

    # 设置页面
    # testSuite.addTest(SettingSpec('test_go_to_comp_billing_page'))
    # testSuite.addTest(SettingSpec('test_go_to_contact_page'))
    # testSuite.addTest(SettingSpec('test_go_to_mutil_user_page'))
    # testSuite.addTest(SettingSpec('test_go_to_partner_set_page'))
    # testSuite.addTest(SettingSpec('test_go_to_tax_rate_page'))
    testSuite.addTest(ContactSpec('test_show_add_modal'))
    

    # 工资
    # testSuite.addTest(AddStuffSpec('test_name_empty'))
    # testSuite.addTest(AddStuffSpec('test_country_empty'))
    # testSuite.addTest(AddStuffSpec('test_id_empty'))
    # testSuite.addTest(AddStuffSpec('test_employed_empty'))
    # testSuite.addTest(AddStuffSpec('test_verify_add_stuff'))
    # testSuite.addTest(AddStuffSpec('test_verify_add_labour'))
    
    # external
    # testSuite.addTest(EnterCompSpec('test_enter_comp'))

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_dir = './report'
    filename = report_dir + '/' + now + '_result.html'
    testReport = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=testReport, title="管有账测试报告", description='测试用例执行情况：')
    runner.run(testSuite)
    testReport.close()
