import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from smtplib import SMTP_SSL


# 发送邮箱服务器
smtpserve = 'smtp.126.com'

# 发送邮箱用户／密码
user = 'huangcaiyantest@126.com'
password = 'Qq123456'
# 发送邮箱
sender = 'huangcaiyantest@126.com'
# 接收邮箱
receiver = '374342187@qq.com'
# 发送邮箱主题
mail_content = '管有帐测试报告'
mail_title = '测试报告'

# 编写HTML类型的邮件正文
msg = MIMEText('<html><h1>您好</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')

# 链接发送邮件
smtp =smtplib.SMTP()
smtp.connect(smtpserve)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()