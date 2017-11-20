#coding=utf-8
import smtplib
from email.mime.text import MIMEText
import string

fp = open('tmp.txt', 'rb')
msg = MIMEText(fp.read())

fp.close()
HOST = "smtp.exmail.qq.com"
SUBJECT = "数据问题"
TO = "pkarqi@163.com"
FROM = 'yunwei@xxxxxxxx.com'
text = '数据问题1111111'
BODY = string.join(("FROM: %s" % FROM,
                    "TO: %s" %TO,
                    "Subject: %s" % SUBJECT,

                    "",
                    text

                    ),"\r\n")



server = smtplib.SMTP()
server.connect(HOST,'25')
server.starttls()
server.login("yunwei@xxxxxx.com","12121212121")
server.sendmail(FROM, [TO], BODY, )

server.quit()