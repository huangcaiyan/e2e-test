import unittest
from test_case.transaction.record_outcome_spec import RecordOutcomeSpec
from test_case.transaction.record_income_spec import RecordIncomeSpec
from test_case.transaction.record_transfer_spec import RecordTransterSpec
from test_case.transaction.outcome_voucher_spec import OutcomeVoucherSpec
from test_case.invoice.record_input_invoice_spec import RecordInputInvoiceSpec
from test_case.invoice.record_output_invoice_spec import RecordOutputInvoiceSpec
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    #记支出测试
    # testSuite.addTest(RecordOutcomeSpec('test1'))
    # testSuite.addTest(RecordOutcomeSpec('test2'))
    # testSuite.addTest(RecordOutcomeSpec('test3'))
    # testSuite.addTest(RecordOutcomeSpec('test4'))
    # testSuite.addTest(RecordOutcomeSpec('test5'))
    # testSuite.addTest(RecordOutcomeSpec('test6'))
    # testSuite.addTest(RecordOutcomeSpec('test7'))
    # testSuite.addTest(RecordOutcomeSpec('test8'))

    # #记收入测试
    # testSuite.addTest(RecordIncomeSpec('test1'))
    # testSuite.addTest(RecordIncomeSpec('test2'))
    # testSuite.addTest(RecordIncomeSpec('test3'))
    # testSuite.addTest(RecordIncomeSpec('test4'))
    # testSuite.addTest(RecordIncomeSpec('test5'))
    # testSuite.addTest(RecordIncomeSpec('test6'))
    # testSuite.addTest(RecordIncomeSpec('test7'))
    # testSuite.addTest(RecordIncomeSpec('test8'))

    #记账户互转
    # testSuite.addTest(RecordTransterSpec('test1'))
    # testSuite.addTest(RecordTransterSpec('test2'))
    # testSuite.addTest(RecordTransterSpec('test3'))
    # testSuite.addTest(RecordTransterSpec('test4'))
    # testSuite.addTest(RecordTransterSpec('test5'))
    # testSuite.addTest(RecordTransterSpec('test6'))
    # testSuite.addTest(RecordTransterSpec('test7'))
    # testSuite.addTest(RecordTransterSpec('test8'))

    #记收票测试
    # testSuite.addTest(RecordInputInvoiceSpec('test1'))
    # testSuite.addTest(RecordInputInvoiceSpec('test2'))

    #记开票测试
    testSuite.addTest(RecordOutputInvoiceSpec('test1'))
    testSuite.addTest(RecordOutputInvoiceSpec('test2'))

    #支出-生成凭证测试
    # testSuite.addTest(OutcomeVoucherSpec('test1'))

    testReport = open('./report/result.html','wb')
    runner = HTMLTestRunner(stream = testReport,title = "管有账测试报告",description='测试用例执行情况：')
    runner.run(testSuite)
    testReport.close()