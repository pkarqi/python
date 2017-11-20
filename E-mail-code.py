#coding=utf-8
import smtplib

import string

HOST = "smtp.exmail.qq.com"
SUBJECT = "数据问题"
TO = "pkarqi@163.com"
FROM = 'yunwei@xxxxxxxxx.com'
text = '数据问题'
BODY = string.join(("FROM: %s" % FROM,
                    "TO: %s" %TO,
                    "Subject: %s" %SUBJECT,
                    "",
                    text
                    ),"\r\n")



server = smtplib.SMTP()
server.connect(HOST,'25')
server.starttls()
server.login("yunwei@xxxxxxx.com","xx   xxxxxx")
server.sendmail(FROM, [TO], BODY)
server.quit()