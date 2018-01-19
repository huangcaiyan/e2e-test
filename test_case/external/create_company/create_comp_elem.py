# －－创建帐套
# 帐套编号 xpath
comp_num_elem = '//*[@id="createCompany"]/div[3]/div/table/new-company/div/tbody/tr/td[2]/div/input'
# 帐套名称 xpath
comp_name_elem = '//*[@id="createCompany"]/div[3]/div/table/new-company/div/tbody/tr/td[3]/div/input'
# 会计制度 name
accounting_standard_elem = 'accountingStandard'
# 帐套性质drop name
property_elem = 'property'
# 启用帐套日期drop
enable_date_drop_elem = '//*[@id="createCompany"]/div[3]/div/table/new-company/div/tbody/tr/td[6]/datepicker'
# 启用帐套日期 年展开xpath
year_open_link_elem = '//*[@id="createCompany"]/div[3]/div/table/new-company/div/tbody/tr/td[6]/datepicker/datepicker-inner/div/monthpicker/div[2]/table/thead/tr/th[2]/button'
# 启用日期年／月份class
month_elem = 'month-button'
# 详细信息栏'未查到详细信息提示文本'xpath
search_failed_elem = '//*[@id="createCompany"]/div[3]/div/table/new-company/div/tbody/tr/td[7]/div/label'

# 详细信息 编辑按钮 xpath
detail_edit_btn_elem = '//*[@id="createCompany"]/div[3]/div/table/new-company/div/tbody/tr/td[7]/label'
# 帐套信息弹窗标题
detail_title_elem = '/html/body/guanplus-app/create-company/companyinfo/div/div/div/div[1]/h4'
# //*[@id="createCompany"]/div[3]/div/table/new-company/div/tbody/tr/td[7]/div/label/a
# -------------------------------------------------------------------------------------------------------------
# －－帐套信息弹窗
# 成立日期展开id
setup_date_elem = 'setupDate'
# 法定代表人 xpath
legal_person_name_elem = '//*[@id="confirmText "]/div[2]/div[2]/input'
# 注册资金 name
registered_capital_elem = 'registeredCapital'
# 税号输入框 xpath
tax_num_elem = '//*[@id="confirmText "]/div[4]/div[2]/input'
# 行业信息 drop name
industry_drop_elem = 'industry'
# 省份、市、区drop name
prov_drop_elem = 'province'
city_drop_elem = 'city'
dist_drop_elem = 'district'

# 帐套信息保存按钮 id
msg_save_btn_elem = 'confirmButton'
# 帐套信息取消按钮 id
msg_cancel_btn_elem = 'cancelButton'

# ----------------------------------------------------------------------------------------------------------

# 创建按钮 xpath
create_btn_elem = '//*[@id="createCompany"]/div[2]/div[2]/ol/li[2]/button'
# 取消创建按钮 xpath
cancel_btn_elem = '//*[@id="createCompany"]/div[2]/div[2]/ol/li[1]/button'

# 批量设置公司性质按钮xpath
multi_setting_comp_property_elem = '//*[@id="createCompany"]/div[3]/div/div/div[1]/div[1]/button'
# 批量设置启用帐套日期按钮xpath
multi_setting_enable_date_elem = '//*[@id="createCompany"]/div[3]/div/div/div[1]/div[2]/button'
