#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
"""
Topic: 时区
Desc :
"""
from datetime import datetime
from pytz import timezone
d = datetime(2017, 3, 30, 17, 36, 0)
print(d)

central = timezone('US/Ce')
