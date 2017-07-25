import unittest
from test_case.transaction.record_outcome_spec import RecordOutcomeSpec
from test_case.invoice.income_invoice_spec import RecordIncomeInvoiceSpec
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
    #记收票测试
    testSuite.addTest(RecordIncomeInvoiceSpec('test1'))
    testSuite.addTest(RecordIncomeInvoiceSpec('test2'))
    testReport = open('./report/result.html','wb')
    runner = HTMLTestRunner(stream = testReport,title = "记收支测试报告",description='测试用例执行情况：')
    runner.run(testSuite)
    testReport.close()