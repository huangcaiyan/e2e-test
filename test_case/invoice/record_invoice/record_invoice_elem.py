# 记发票页面
# 记发票页面base xpath
record_invoice_base_xpath = '//*[@id="body"]/tab/new-'
# 发票类型下拉 结尾 xpath
invoice_type_drop_elem = '-invoice/div/div[2]/ul/div[1]/div/label[2]/ng-select'
# 发票状态 结尾xpath
invoice_status_drop_elem = '-invoice/div/div[2]/ul/div[1]/div/label[3]/ng-select'
# ++记收票
# 往来信息下拉 结尾 xpath
input_contact_drop_elem = '-invoice/div/div[2]/ul/div[1]/div/label[3]/ng-select'
# --记开票
# 往来信息下拉 结尾 xpath
output_contact_drop_elem = '-invoice/div/div[2]/ul/div[1]/div/label[4]/ng-select'
# ++记收票
# 发票号输入框 结尾 xpath
input_invoice_num_elem = '-invoice/div/div[2]/ul/div[1]/div/label[4]/div/input'
# --记开票
# 发票号输入框 结尾xpath
output_invoice_num_elem = '-invoice/div/div[2]/ul/div[1]/div/label[5]/div/input'
# 类别下拉 结尾xpath
category_drop_elem = '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[1]/ng-select'
# 类别下拉选择class
parent_elem = '.parent-options'
child_elem = '.children-options'
# 部门性质下拉 结尾xpath
department_drop_elem = '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[2]/ng-select'
# 税率下拉 结尾xpath
tax_rate_drop_elem = '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[3]/ng-select'
# 进项税类别下拉 结尾xpath
input_tax_category_drop_elem = '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[4]/ng-select'
# 价税合计input 结尾xpath
total_elem = '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[4]/bp-input/input'
# 备注input 结尾xpath
attachment_elem = '-invoice/div/div[2]/ul/table/tbody/tr[1]/td[5]/div/input'
# 保存并新增按钮 结尾xpath
save_and_new_btn_elem = '-invoice/div/div[2]/ul/div[3]/div/span/button[1]'
# 保存按钮 xpath
save_btn_elem = '-invoice/div/div[2]/ul/div[3]/div/span/button[2]'
# 取消按钮 结尾xpath
cancel_btn_elem = '-invoice/div/div[2]/ul/div[3]/div/span/button[3]'
