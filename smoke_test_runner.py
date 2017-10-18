import unittest
import time
import os
import smtplib
from HTMLTestRunner import HTMLTestRunner
from test_case.login.login_spec import LoginSpec
from test_case.setting.setting_spec import SettingSpec
from test_case.setting.comp_billing.comp_billing_spec import CompBillingSpec
from test_case.setting.contact.contact_spec import ContactSpec
from test_case.salary.add_stuff.add_stuff_spec import AddStuffSpec
from test_case.external.enter_comp_spec import EnterCompSpec
from test_case.external.create_comp.create_comp_spec import CreateCompSpec
from test_case.external.user_setting.user_setting_spec import UserSettingSpec
from test_case.transaction.record_transaction.record_transaction_spec import RecordTransactionSpec
from test_case.invoice.record_invoice.record_invoice_spec import RecordInvoiceSpec
if __name__ == '__main__':
    testSuite = unittest.TestSuite()

    # 登录测试
    # testSuite.addTest(LoginSpec('test_verify_login'))
    # testSuite.addTest(LoginSpec('test_unexit_username'))
    testSuite.addTest(LoginSpec('test_wrong_password'))
    # testSuite.addTest(LoginSpec('test_empty_username'))
    # testSuite.addTest(LoginSpec('test_empty_password'))
    # testSuite.addTest(LoginSpec('test_typeerror_username'))

    # 设置页面
    # testSuite.addTest(SettingSpec('test_go_to_comp_billing_page'))
    # testSuite.addTest(SettingSpec('test_go_to_contact_page'))
    # testSuite.addTest(SettingSpec('test_go_to_mutil_user_page'))
    # testSuite.addTest(SettingSpec('test_go_to_partner_set_page'))
    # testSuite.addTest(SettingSpec('test_go_to_tax_rate_page'))

    # 设置－帐套信息页面
    # testSuite.addTest(CompBillingSpec('test_comp_name_empty'))
    # testSuite.addTest(CompBillingSpec('test_legal_person_name_empty'))
    # testSuite.addTest(CompBillingSpec('test_tax_num_empty'))
    # testSuite.addTest(CompBillingSpec('test_verify_edit_comp_info'))

    # 设置－往来性质
    # testSuite.addTest(ContactSpec('test_show_add_modal'))
    # testSuite.addTest(ContactSpec('test_name_empty'))
    # testSuite.addTest(ContactSpec('test_phone_num_typeError'))
    # testSuite.addTest(ContactSpec('test_contact_input_show'))
    # testSuite.addTest(ContactSpec('test_contact_property_is_unit'))
    # testSuite.addTest(ContactSpec('test_contact_property_is_personal'))

    #
    # 工资－添加员工
    # testSuite.addTest(AddStuffSpec('test_name_empty'))
    # testSuite.addTest(AddStuffSpec('test_country_empty'))
    # testSuite.addTest(AddStuffSpec('test_id_empty'))
    # testSuite.addTest(AddStuffSpec('test_employed_empty'))
    # testSuite.addTest(AddStuffSpec('test_verify_add_stuff'))
    # testSuite.addTest(AddStuffSpec('test_verify_add_labour'))
    # testSuite.addTest(AddStuffSpec('test'))

    # 记收支
    # 记所有科目和账户的收支、互转
    # testSuite.addTest(RecordTransactionSpec('test_record_income'))
    # testSuite.addTest(RecordTransactionSpec('test_record_outcome'))
    # testSuite.addTest(RecordTransactionSpec('test_record_transfer'))

    # 记发票
    # 记所有类别发票
    testSuite.addTest(RecordInvoiceSpec('test_record_input_invoice'))

    # external
    # testSuite.addTest(EnterCompSpec('test_enter_comp'))
    # testSuite.addTest(CreateCompSpec('create_account_book_empty_comp_name'))
    # testSuite.addTest(UserSettingSpec('test_go_to_comp_billing_page'))

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_dir = './report'
    filename = report_dir + '/' + now + '_result.html'
    testReport = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=testReport, title="管有账测试报告", description='测试用例执行情况：')
    runner.run(testSuite)
    testReport.close()
