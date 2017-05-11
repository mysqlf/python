#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from urllib import request
# # with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
# #     data = f.read()
# #     print('Status', f.status, f.reason)
# #     for k, v in f.getheaders():
# #         print('%s:%s' % (k, v))
# #     print('Data', data.decode('utf-8'))

# req = request.Request('https://www.douban.com/')
# req.add_header(
#     'User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# 模拟登陆微博  IDE下无法完全交互
from urllib import request, parse

print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', '1154505909@qq.com'),
    ('password', '520zuochao'),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer',
     'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header(
    'User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header(
    'Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# D:\Git\python\Pack>Urllib_study.py
# Login to weibo.cn...
# Email: 1154505909@qq.com
# Password: 520zuochao
# Status: 200 OK
# Server: nginx/1.2.0
# Date: Mon, 26 Sep 2016 21:26:19 GMT
# Content-Type: text/html
# Transfer-Encoding: chunked
# Connection: close
# Vary: Accept-Encoding
# Cache-Control: no-cache, must-revalidate
# Expires: Sat, 26 Jul 1997 05:00:00 GMT
# Pragma: no-cache
# Access-Control-Allow-Origin: https://passport.weibo.cn
# Access-Control-Allow-Credentials: true
# Set-Cookie: SUB=_2A2567eIrDeTxGeRP41IT8C7PyDiIHXVWEY5jrDV6PUJbkdBeLXLtkW1idAf-vV
# YZbzgkG84C7WmPgXn3jQ..; Path=/; Domain=.weibo.cn; Expires=Tue, 26 Sep 2017 21:26
# :19 GMT; HttpOnly
# Set-Cookie: SUHB=0HTwucHXGUD0Ql; expires=Tuesday, 26-Sep-17 21:26:19 GMT; path=/
# ; domain=.weibo.cn
# Set-Cookie: SCF=AuMiK-22TGdgN_1mhciZmfXVin6fbQAGte8Hepk1pmwu075OjuZTBy1i5ANdIiLy
# hEIs8qVJn7_vY9IQpiafdL8.; expires=Thursday, 24-Sep-26 21:26:19 GMT; path=/; doma
# in=.weibo.cn; httponly
# Set-Cookie: SSOLoginState=1474925179; path=/; domain=weibo.cn
# Set-Cookie: ALF=1477517179; expires=Wednesday, 26-Oct-16 21:26:19 GMT; path=/; d
# omain=.sina.cn
# DPOOL_HEADER: dryad23
# SINA-LB: aGEuMzIuZzEucXhnLmxiLnNpbmFub2RlLmNvbQ==
# SINA-TS: ZTZjYTk0Y2UgMCAwIDAgNyAxMDc5Cg==
# Data: {"retcode":20000000,"msg":"","data":{"loginresulturl":"https:\/\/passport.
# weibo.com\/sso\/crossdomain?entry=mweibo&action=login&proj=1&ticket=ST-MjE4MDIwM
# DMzNA%3D%3D-1474925179-gz-E28CAEBC7277CFA150C2CEC38BB291FF&display=0&cdurl=https
# %3A%2F%2Flogin.sina.com.cn%2Fsso%2Fcrossdomain%3Fentry%3Dmweibo%26action%3Dlogin
# %26proj%3D1%26ticket%3DST-MjE4MDIwMDMzNA%253D%253D-1474925179-gz-9C3F147B9AEC873
# 834FD1A3F36DA865F%26display%3D0%26cdurl%3Dhttps%253A%252F%252Fpassport.sina.cn%2
# 52Fsso%252Fcrossdomain%253Fentry%253Dmweibo%2526action%253Dlogin%2526display%253
# D0%2526ticket%253DST-MjE4MDIwMDMzNA%25253D%25253D-1474925179-gz-762D8BC5044AB438
# 3FBC34C72F6766B5","uid":"2180200334"}}
