# -*- coding:utf-8 -*-
import smtplib
import string


HOST = 'smtp.qq.com'    # SMTP 第三方
SUBJECT = 'Test email from python'      # 主题
TO = '848864947@qq.com'     # 发送给此用户
FROM = '30733705@qq.com'        # 来自该用户
FROM_PS = 'hmufwafxwebbcbai'        # 手机短信获取的授权码
TEXT = 'Python rulese them all!'    # 正文内容
BODY = string.join((
    "FROM: %s" % FROM,
    "TO: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    TEXT
), "\r\n")
try:
    server = smtplib.SMTP_SSL(HOST, 465)
    server.login(FROM, FROM_PS)
    server.sendmail(FROM, TO, BODY)
    server.quit()
    print u"邮件发送成功"
except smtplib.SMTPException, e:
    print e
