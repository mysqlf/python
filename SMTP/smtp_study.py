#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from email.mime.text import MIMEText  # , MIMEMultipart
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
    # 正文

# 输入邮箱账号密码
from_addr = '1154505909@qq.com'  # input('From:')
password = 'dsvqcprzbimvjgie'  # input('password:')
to_addr = '1575453783@qq.com'  # input('To:')
smtp_service = 'smtp.qq.com'  # input('SMTP service:')

# content = '努力学习，只为以后有能力让你可以任性'
# msg = MIMEText(content, 'plain', 'utf-8')
# # content = '<html><body><h1>Hello</h1><p>send by <a href="http://www.python.org">Python</a>...</p></body></html>'
# # msg = MIMEText(content, 'html', 'utf-8')
# msg['From'] = _format_addr('学习爱好者<%s>' % from_addr)
# msg['To'] = _format_addr('吾爱<%s>' % to_addr)
# msg['Subject'] = Header('来自浪子的问候', 'utf-8').encode()
# server = smtplib.SMTP_SSL(smtp_service, 465)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())  # msg.attach(msg1)
# server.quit()
msg = MIMEMultipart()
msg['From'] = _format_addr('学习爱好者<%s>' % from_addr)
msg['To'] = _format_addr('吾爱<%s>' % to_addr)
msg['Subject'] = Header('来自浪子的问候', 'utf-8').encode()
msg.attach(MIMEText('send with file', 'plain', 'utf-8'))
#f = open('D:/Git/python/code1.jpg', 'r')

with open('D:/Git/python/code1.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='code1.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='code1.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_service, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())  # msg.attach(msg1)
server.quit()
