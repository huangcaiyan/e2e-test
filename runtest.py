import unittest
from test_case.transaction.record_outcome_spec import RecordOutcomeSpec
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    testSuite.addTest(RecordOutcomeSpec('test1'))
    testSuite.addTest(RecordOutcomeSpec('test2'))
    testReport = open('./report/result.html','wb')
    runner = HTMLTestRunner(stream = testReport,title = "记收支测试报告",description='测试用例执行情况：')
    runner.run(testSuite)
    testReport.close()