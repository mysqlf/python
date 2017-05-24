#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# IO 操作
import io
s=io.StringIO()
s.write('hello')
print('this is test',file=s)
print(s.getvalue())
