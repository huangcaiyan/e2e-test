import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


#发送邮件
def sendEmail():
    smtpserver = 'smtp.163.com'
    user = '18514509382@163.com'
    password = 'yang115817'

    sender = '18514509382@163.com'
    receiver = '1223777944@qq.com'
    # msg = MIMEText('hello from python test','plain','utf-8')
    msg = MIMEText('<html><body><h1>Hello</h1>' +
        '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
        '</body></html>', 'html', 'utf-8')
    msg['From'] = '18514509382@163.com <18514509382@163.com>'
    msg['Subject'] = Header(u'html from ych','utf8').encode()
    msg['To'] = '淡如水<1223777944@qq.com>'
    smtp = smtplib.SMTP(smtpserver,25)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print('send email success')

#发送带附件的邮件
def sendEmailAccessory():
    smtpserver = 'smtp.163.com'
    user = '18514509382@163.com'
    password = 'yang115817'

    sender = '18514509382@163.com'
    receiver = '1223777944@qq.com'
    msg = MIMEMultipart()
    msg['From'] = '18514509382@163.com <18514509382@163.com>'
    msg['Subject'] = Header(u'html from ych with accessory','utf8').encode()
    msg['To'] = '淡如水<1223777944@qq.com>'
    msg.attach(MIMEText('send with file...','plain','utf-8'))
    with open('F:\\autoTest_workspace\\python_code\\e2e-test\\report\images\\addAccountError.jpg','rb') as f:
        mime = MIMEBase('image','jpg',filename='addAccountError.jpg')
        mime.add_header('Content-Disposition', 'attachment', filename='test.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)
        smtp = smtplib.SMTP(smtpserver,25)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print('send email success')

#发送正文带图片的邮件
def sendEmailWithPicInmainFIle():
    smtpserver = 'smtp.163.com'
    user = '18514509382@163.com'
    password = 'yang115817'

    sender = '18514509382@163.com'
    # receiver = '1223777944@qq.com'
    receiver = 'yangchunhong@concordya.com'
    msg = MIMEMultipart()
    msg['From'] = '18514509382@163.com'
    msg['Subject'] = Header(u'failed','utf8').encode()
    # msg['To'] = '淡如水<1223777944@qq.com>'
    msg['To'] = 'yangchunhong@concordya.com'
    msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
        '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
        '</body></html>', 'html', 'utf-8'))
    with open('F:\\autoTest_workspace\\python_code\\e2e-test\\report\images\\addAccountError.jpg','rb') as f:
        mime = MIMEBase('image','jpg',filename='addAccountError.jpg')
        mime.add_header('Content-Disposition', 'attachment', filename='test.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)
        smtp = smtplib.SMTP(smtpserver,25)
    smtp.starttls()
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print('send email success')


sendEmailWithPicInmainFIle()
# sendEmailAccessory()