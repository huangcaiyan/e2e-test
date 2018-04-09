import unittest
import time
from HTMLTestRunner import HTMLTestRunner

from test_case.invoice.record_invoice.record_invoice_spec import RecordInvoiceSpec
from test_case.external.create_company.create_comp_spec import CreateCompSpec
from test_case.external.beginning_period.beginning_period_spec import BeginningPeriodSpec

if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    
    # # 登录测试
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
    
    # 设置－帐套信息页面
    # testSuite.addTest(CompBillingSpec('test_comp_name_empty'))
    # testSuite.addTest(CompBillingSpec('test_legal_person_name_empty'))
    # testSuite.addTest(CompBillingSpec('test_tax_num_empty'))
    # testSuite.addTest(CompBillingSpec('test_verify_edit_comp_info'))
    
    # 设置－往来性质(done)
    # testSuite.addTest(ContactSpec('test_show_add_modal'))
    # testSuite.addTest(ContactSpec('test_name_empty'))
    # testSuite.addTest(ContactSpec('test_phone_num_typeError'))
    # testSuite.addTest(ContactSpec('test_contact_input_show'))
    # testSuite.addTest(ContactSpec('test_contact_property_is_unit'))
    # testSuite.addTest(ContactSpec('test_contact_property_is_personal'))
    # testSuite.addTest(ContactSpec('test_name_repeat'))
    
    # 设置－股东信息(done)
    # testSuite.addTest(PartnersetSpec('test_click_add_btn_modal_is_show'))
    # testSuite.addTest(PartnersetSpec('test_partnerset_empty_invalid'))
    # testSuite.addTest(PartnersetSpec('test_actual_paid_empty_valid'))
    # testSuite.addTest(PartnersetSpec('test_partset_name_repeat_invalid'))
    # testSuite.addTest(PartnersetSpec('test_add_a_partner_valid'))
    # testSuite.addTest(PartnersetSpec('test_edit_partnerset_valid'))
    # testSuite.addTest(PartnersetSpec('test'))
    
    #
    # # 工资－添加员工
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
    
    # # 记发票
    # # # 记所有类别发票
    # testSuite.addTest(RecordInvoiceSpec('test_record_input_invoice'))
    # testSuite.addTest(RecordInvoiceSpec('test_record_output_invoice'))
    # testSuite.addTest(RecordInvoiceSpec('test_record_output_invoice_xgm'))
    #
    # 报表
    # 
    # testSuite.addTest(ReportDataReadySpec('test_record_income'))
    # testSuite.addTest(ReportDataReadySpec('test_record_outcome'))
    # testSuite.addTest(ReportDataReadySpec('test_record_transfer'))
    # testSuite.addTest(ReportDataReadySpec('test_record_input_invoice'))
    # testSuite.addTest(ReportDataReadySpec('test_record_output_invoice'))
    
    # external
    # 记录完全部收入、支出、互转，手指列表本月收入为42,650.92，支出为70,584.30
    # testSuite.addTest(EnterCompSpec('test_enter_comp'))
    # 创建帐套
    # testSuite.addTest( CreateCompSpec( 'test_verify_create_comp' ) )
    # testSuite.addTest(CreateCompSpec('test_create_comp_empty_comp_name'))
    # testSuite.addTest(CreateCompSpec('test_create_comp_empty_legal_person'))
    # 帐套列表
    # 分配会计／助理／客服联系人
    # testSuite.addTest(DistributeModalSpec('test_distribute_accounting'))
    # 启用期初帐页面
    testSuite.addTest( BeginningPeriodSpec( 'test_import_initial_account' ) )
    
    # testSuite.addTest(UserSettingSpec('test_go_to_comp_billing_page'))
    # testSuite.addTest(SidebarSpec('test_get_current_account_period'))
    # testSuite.addTest(CreateWaysSpec('test_input_comp_name_jump_to_create_page'))
    
    now = time.strftime( '%Y-%m-%d %H_%M_%S' )
    report_dir = './report/cai_test'
    filename = report_dir + '/' + now + '_result.html'
    testReport = open( filename , 'wb' )
    runner = HTMLTestRunner( stream=testReport , title="管有账测试报告" , description='测试用例执行情况：' )
    runner.run( testSuite )
    testReport.close()
