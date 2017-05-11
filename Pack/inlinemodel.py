#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from datetime import datetime, timedelta
# now = datetime.now()
# print(now)
# print(type(now))
# dt = datetime(2016, 9, 20, 9, 00)
# print(dt)
# print(dt.timestamp())
# x = now.timestamp()
# print(datetime.fromtimestamp(x))
# print(datetime.utcfromtimestamp(x))

# cday = datetime.strptime('2016-09-20 09:06:13', '%Y-%m-%d %H:%M:%S')
# print(cday)
# print(now.strftime('%a,%b,%d %H:%m'))

# now = datetime.now()
# print(now)
# # datetime.datetime(2016, 9, 18, 14, 23, 123456)
# k = now + timedelta(hours=10)
# print(k)
# k = now - timedelta(days=1)
# print(k)
# k = now - timedelta(days=1, hours=10)
# print(k)

# from datetime import datetime, timedelta, timezone
# tz_utc_8 = timezone(timedelta(hours=8))
# print(tz_utc_8)

# now = datetime.now()
# print(now)
# dt = now.replace(tzinfo=tz_utc_8)
# print(dt)

# utc = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc)
# bj_dt = dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)
# dj_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
# print(dj_dt)

# import re

# # 将带时区的时间转为时间戳


# def day2time(day, tz):
#     tmp = datetime.strptime(day, '%Y-%m-%d %H:%M:%S')
#     #ho = list(tz)
#     m = re.match(r'^UTC([-|+]\d{1,2}):\d{2}$', tz)
#     # return m.group(1)
#     # if ho[3] == '-':
#     #     tx_0 = timezone(timedelta(hours=(int(m.group(1)))))
#     # else:
#     tx_0 = timezone(timedelta(hours=int(m.group(1))))
#     tmp = tmp.replace(tzinfo=tx_0)
#     return tmp.timestamp()
# x = day2time('2015-6-1 08:10:30', 'UTC+7:00')
# print(x)
# x = day2time('2015-5-31 16:10:30', 'UTC-9:00')
# print(x)
# 1433142630.0
