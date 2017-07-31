from selenium import webdriver
import unittest

#校验生成凭证
class VoucherCheck(unittest.TestCase):
    def __init__(self,driver):
        super(VoucherCheck,self).__init__()
        self.driver = driver

    def voucherCheck(self,generateVoucherData):
        tbodyLists = self.driver.find_element_by_xpath('//*[@id="body"]/finance/div/voucher/div[1]/div[3]/div[1]/div/table').find_elements_by_tag_name('tbody')
        for tbody,voucherData in zip(tbodyLists,generateVoucherData):
            trLists = tbody.find_elements_by_tag_name('tr')
            for tr,lineVoucherData in zip(trLists,voucherData):
               tdLists = tr.find_elements_by_tag_name('td') 
               if 9 == len(tdLists):  
                    for td,voucherFieldData in zip(tdLists[2:6],lineVoucherData):
                        self.assertEqual(voucherFieldData,td.text)
               if 4 == len(tdLists):
                    for td,voucherFieldData in zip(tdLists,lineVoucherData):
                        self.assertEqual(voucherFieldData,td.text)
               if 5 == len(tdLists):
                    for td,voucherFieldData in zip(tdLists[2:4],lineVoucherData):
                        self.assertEqual(voucherFieldData,td.text)