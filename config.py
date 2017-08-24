from selenium import webdriver

#api地址
ApiBaseUrl = 'https://api-firms.guanplus.com'
IdentityApiBaseUrl = 'https://api-identity.guanplus.com'


#PhantomJS webdriver
# Driver = webdriver.PhantomJS()
Driver = webdriver.Chrome()

#dev环境地址
# BaseUrl = 'http://guanplus-app-accountingfirm-web-dev-1.cn-north-1.eb.amazonaws.com.cn'

#stage环境地址
BaseUrl = 'https://web-gyz-stage.guanplus.com'

#pro环境地址
# BaseUrl = 'https://firms.guanplus.com'

#dev环境:账户->账套 [账户，密码，公司名]
# AccountCompany = ['18201215366','qq123456','一般纳税人07251510'] 

#stage环境:账户->账套 [账户，密码，公司名]
AccountCompany = ['18514509382','qq123456','羊羊羊08101921']

#pro环境测试：账户->账套 [账户，密码，公司名]
# AccountCompany = ['18514509382','qq123456','一般纳税人07272015'] 
# AccountCompany = ['18514509382','qq123456','美乐家'] 

Environment = [BaseUrl,AccountCompany]
