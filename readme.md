一、环境说明：

python版本：       3.6.1
selenum版本：      2.0
chrome版本：       59.0.3071.115
chromedriver版本： 2.30.477700
pip命令使用配置:   将python安装文件目录下Scripts配置到系统环境变量中的path里面
将HTMLTestRunner拷贝到 'C:\Users\yangchunhong\AppData\Local\Programs\Python\Python36\Lib'目录下

二、涉及的第三方模块
（注：快速下载第三方模块pip3 install --index https://pypi.mirrors.ustc.edu.cn/simple/）
1、操作excel： xlrd, openpyxl
2、http协议相关：  requests
3、连接PostgreSQL数据库模块：psycopg2 
 sqlalchemy  sqlalchemy

# pip3 install -U selenium
# pip3 install xlrd
# pip3 install openpyxl
# pip3 install requests
# pip3 install html-testRunner


<!-- 代码规范 -->
# class name(类名)：
# # 驼峰命名方法，首字母大写，单词之间大写字母连接，
# # eg：LoginPage()

# method name(方法名)：
# # 字母小写，单词之间用下划线 _ 连接
# # eg：set_password()

# variable name(变量名)：
# # 字母小写，单词之间用下划线 _ 连接
# # eg：login_btn_elem

# 包版本
# # chromedriver2.37
# # python3.6.5
# # Selenium
# # pip10.0.0b2
# # requests2.18.4
# # selenium3.11.0
# # setuptools9.0.1
# # urllib31.22
# # wheel0.31.0
# # xlrd1.1.0

