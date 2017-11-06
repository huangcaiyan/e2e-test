from selenium import webdriver
from selenium.webdriver.common.by import By


# 更新于2017/11/06
class CashFlowsPage(object):
    # 根据table的class属性和table中的某一个元素定位其在table中的位置
    # table包括表头，位置坐标都是从1开始算
    # tableClass:table的class属性
    # tableID:table的id属性
    # queryContent:需要确定位置的内容
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    def get_table_content(self, tableClass, queryContent):
        arr = []
        arr1 = []
        table_loc = (By.CLASS_NAME,tableClass)
        # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
        table_tr_list = self.driver.find_element(*table_loc).find_elements(By.TAG_NAME, "tr")
        for tr in table_tr_list:
            # 以空格拆分成若干个（个数与列的个数相同）一维列表
            arr1 = (tr.text).split(" ")
            print(tr.text)
            print(arr1)
            # 将表格数据组成二维的列表
            arr.append(arr1)
            return arr

        # 循环遍历table数据，确定查询数据的位置
        for i in range (len(arr)):
            for j in range(len(arr[i])):
                if queryContent == arr[i][j]:
                    print ("%坐标为(%r,%r)" %(queryContent,i+1,j+1))


    # 进入现金流量表页面
    def goToCashFlowsModule(self, baseUrl):
        subUrl = '/app/reports/cashFlows-statement'
        self.driver.get(baseUrl + subUrl)