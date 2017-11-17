from selenium import webdriver
import os,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 

class GetTableContent:


    def __init__(self, driver):
        self.driver = driver

    def get_table_content(self,tableId,queryContent):  
    
        
        table_rows = []
        row_list = []  
        table_elem = self.driver.find_element_by_id(tableId)
        # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据  
        table_rows = table_elem.find_elements_by_tag_name('tr') 
        print("总行数：",len(table_rows))
        table_list = []  #存放table数据  
        table_cols = table_rows[0].find_elements_by_tag_name('th') 
        print("总列数：",len(table_cols))
        
        
        #遍历每一个tr  
        for tr in table_rows:    
            #将每一个tr的数据根据td查询出来，返回结果为list对象 
            
            table_td_list = tr.find_elements_by_tag_name('td')  
                
            # print(22222222222222222)
            print(table_td_list)  
            #遍历每一个td  
            for td in table_td_list:    
                row_list.append(td.text)    #取出表格的数据，并放入行列表里  
                print("text:" + td.text)
            table_list.append(row_list)  

        
        # 循环遍历table数据，确定查询数据的位置  
        return table_list[queryContent[0]][queryContent[1]]