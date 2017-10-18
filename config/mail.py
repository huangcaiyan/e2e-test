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

def mail():
    ret = True
    try:
        # ssl 登陆
        smtp = SMTP_SSL(smtpserve)
        # set_debuglevel()用来测试的参数值未1表示开启调试模式，参数未0关闭调试模式
        smtp.set_debuglevel(1)
        smtp.ehlo(smtpserve)
        smtp.login(user,password)
        msg = MIMEText(mail_content,'plain','utf-8')
        msg['Subject']=Header(mail_title, 'utf-8')
        msg['From']=sender_mail
        msg['To']=receiver_mail
        smtp.sendmail(sender_mail, receiver_mail, msg.as_string())
        smtp.quit()
    except Exception as ex: #如果try中的语句没有执行，则会执行下面的ret=False
        print(ex)
        ret=False
    return ret

ret = mail()
if ret:
    print ("邮件发送成功")
else:
    print("邮件发送失败")

# # 编写HTML类型的邮件正文
# msg = MIMEText('<html><h1>您好</h1></html>','html','utf-8')
# msg['Subject'] = Header(subject,'utf-8')

# # 链接发送邮件
# smtp =smtplib.SMTP()
# smtp.connect(smtpserve)
# smtp.login(user,password)
# smtp.sendmail(sender,receiver,msg.as_string())
# smtp.quit()