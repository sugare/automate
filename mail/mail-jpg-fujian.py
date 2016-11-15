# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText    # 导入MIMEText
from email.mime.multipart import MIMEMultipart  # 导入MIMEMultipart类
from email.mime.image import MIMEImage      # 导入MIMEImage类

HOST = 'smtp.qq.com'    # SMTP 第三方
SUBJECT = u'官网流量报表'      # 主题
TO = '848864947@qq.com'     # 发送给此用户
FROM = '30733705@qq.com'        # 来自该用户
FROM_PS = 'hmufwafxwebbcbai'        # 手机短信获取的授权码

def addimg(src,imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage

msg = MIMEMultipart('related')
msgtext = MIMEText("<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>","html","utf-8")
msg.attach(msgtext)
msg.attach(addimg("img/weekly.png","weekly"))

attach = MIMEText(open("doc/week_report.xlsx", "rb").read(), "base64", "utf-8")
attach["Content-Type"] = "application/octet-stream"
attach["Content-Disposition"] = "attachment; filename=\"业务服务质量周报(12周).xlsx\"".decode("utf-8").encode("gb18030")
msg.attach(attach)

msg['Subject'] = SUBJECT
msg['From']=FROM
msg['To']=TO

try:
    server = smtplib.SMTP_SSL(HOST, 465)
    server.login(FROM, FROM_PS)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print u"邮件发送成功"
except smtplib.SMTPException, e:
    print e
