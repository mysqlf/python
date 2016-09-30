#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
    # 正文

# 输入邮箱账号密码
from_addr = '1154505909@qq.com'  # input('From:')
password = 'ihktpbrqhppzbaab'  # input('password:')
to_addr = 'z1154505909@163.com'  # input('To:')
smtp_service = 'smtp.qq.com'  # input('SMTP service:')

msg = MIMEText('Hello ,send by python study', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自银河系的问候', 'utf-8').encode()
service = smtplib.SMTP_SSL(smtp_service, 465)
service.set_debuglevel(1)
service.login(from_addr, password)
service.sendmail(from_addr, [to_addr], msg.as_srting())  # msg.attach(msg1)
service.quit()
