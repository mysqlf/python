#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mine.text import MIMEText
# 正文
msg = MIMEText('Hello ,send by python study', 'plain', 'utf-8')

# 输入邮箱账号密码
from_addr = input('From:')
password = input('password:')
to_addr = input('To:')
smtp_service = input('SMTP service:')
import smtplib
service = smtplib.SMTP(smtp_service, 25)
service.set_debuglevel(1)
service.login(from_addr, password)
service.sendmail(from_addr, [to_addr], msg.as_srting())
service.quit()
