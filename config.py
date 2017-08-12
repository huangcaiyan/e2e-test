from selenium import webdriver

#PhantomJS webdriver
Driver = webdriver.PhantomJS()
# Driver = webdriver.Chrome()

#dev环境地址
# BaseUrl = 'http://guanplus-app-accountingfirm-web-dev-1.cn-north-1.eb.amazonaws.com.cn'

#stage环境地址
# BaseUrl = 'https://web-gyz-stage.guanplus.com'

#pro环境地址
BaseUrl = 'https://firms.guanplus.com'

#dev环境:账户->账套 [账户，密码，公司名]
# AccountCompany = ['18201215366','qq123456','一般纳税人07251510'] 

#stage环境:账户->账套 [账户，密码，公司名]
AccountCompany = ['18514509382','qq123456','羊羊羊08101921']
# AccountCompany = ['18201215366','qq123456','钰一般纳税人07271520'] 
# AccountCompany = ['15201072356','qq123456','一般纳税人07261454']
# AccountCompany = ['13546465643','qq123456','一般纳税人07261454']

#pro环境测试：账户->账套 [账户，密码，公司名]
# AccountCompany = ['18514509382','qq123456','一般纳税人07272015'] 
# AccountCompany = ['18514509382','qq123456','美乐家'] 

Environment = [BaseUrl,AccountCompany]

# #pro环境地址-创建公司-》进入账套
# BaseUrl2 = 'https://firms.guanplus.com'
# Account = ['18514509382','qq123456']
# address = ['北京市','市辖区','海淀区']
# CompanyInfo = ['一般纳税人07291909','羊羊羊','12',address,'1','222222221111112','批发、零售','一般纳税人','7']
# RoleInfo = [['羊羊羊','18514509382'],'yang','yang']

# Environment2 = [BaseUrl2,Account,CompanyInfo,RoleInfo]