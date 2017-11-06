# 收票列表
# 发票列表pre xpath
list_base_elem = '//*[@id="body"]/]'

# 记收票按钮 xpath
record_invoice_btn_elem = '-invoice/div[2]/div[2]/span/button[1]'
# 筛选按钮 xpath
search_btn_elem = '-invoice/div[2]/div[2]/span/button[3]'
# 筛选
# 筛选开始日期
begin_date_drop_elem = '-invoice/div[3]/div[1]/div/div[1]/p-calendar[1]'
# 筛选结束日期
end_date_drop_elem = '-invoice/div[3]/div[1]/div/div[1]/p-calendar[2]'
# 发票类型drop xpath
invoice_type_drop_elem = '-invoice/div[3]/div[1]/div/div[2]/ng-select'
# 对方信息搜索框 xpath
contact_input_elem = '-invoice/div[3]/div[1]/div/div[3]/div/input'
# 税率下拉 xpath
tax_rate_drop_elem = '-invoice/div[3]/div[1]/div/div[4]/ng-select'
# 发票号搜索框
tax_num_input_elem = '-invoice/div[3]/div[2]/div/div/input'
# 清空搜索按钮
empty_btn_elem = '-invoice/div[3]/div[3]/div/div[3]/label'
# 发票合计 xpath
list_total_elem = '-invoice/div[3]/table/thead[2]/tr/th[3]'
