# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText    # 导入MIMEText


HOST = 'smtp.qq.com'    # SMTP 第三方
SUBJECT = u'官网流量报表'      # 主题
TO = '848864947@qq.com'     # 发送给此用户
FROM = '30733705@qq.com'        # 来自该用户
FROM_PS = 'hmufwafxwebbcbai'        # 手机短信获取的授权码
msg = MIMEText("""
    <table width="800" border="0" cellspacing="0" cellpadding="4">
      <tr>
      </tr>
      <tr>
        <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
        1）日访问量:<font color=red>152433</font>  访问次数:23651 页>面浏览量:45123 点击数:545122  数据流量:504Mb<br>
        2）状态码信息<br>
        &nbsp;&nbsp;500:105  404:3264  503:214<br>
        3）访客浏览器信息<br>
        &nbsp;&nbsp;IE:50%  firefox:10% chrome:30% other:10%<br>
        4）页面信息<br>
        &nbsp;&nbsp;/index.php 42153<br>
        &nbsp;&nbsp;/view.php 21451<br>
        &nbsp;&nbsp;/login.php 5112<br>
        </td>
      </tr>
    </table>""","html","utf-8")
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
