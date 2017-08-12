import smtplib
import email.mime.multipart
import email.mime.text

def test():
    msg = email.mime.multipart.MIMEMultipart()
    msg['Subject'] = 'duanx'
    msg['From'] = '1223777944@qq.com'
    msg['To'] = '18514509382@163.com'
    content = '''''
        你好，xiaoming
                这是一封自动发送的邮件。

            www.ustchacker.com
    '''
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    #smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com', '465')
    smtp.login('1223777944@qq.com', 'tvatjryzicluiged')
    smtp.sendmail('1223777944@qq.com','18514509382@163.com' , msg.as_string())
    smtp.quit()
    print('邮件发送成功email has send out !')

test()