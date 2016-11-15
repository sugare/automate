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

def addimg(src,imgid):      # 添加图片函数，参数1：图片路径，参数2：图片id
    fp = open(src, 'rb')    # 打开文件
    msgImage = MIMEImage(fp.read())     # 创建MIMEImage对象，读取图片内容作为参数
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage

msg = MIMEMultipart('related')
msgtext = MIMEText("""
<table width="600" border="0" cellspacing="0" cellpadding="4">
      <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
      </tr>
      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
        <td>
         <img src="cid:io"></td><td>
         <img src="cid:key_hit"></td>
      </tr>
      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
         <td>
         <img src="cid:men"></td><td>
         <img src="cid:swap"></td>
      </tr>
    </table>""","html","utf-8")
msg.attach(msgtext)
msg.attach(addimg("img/bytes_io.png","io"))
msg.attach(addimg("img/myisam_key_hit.png","key_hit"))
msg.attach(addimg("img/os_mem.png","men"))
msg.attach(addimg("img/os_swap.png","swap"))

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
