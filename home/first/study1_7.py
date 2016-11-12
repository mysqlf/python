#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 在为了能控制一个字典中元素的顺序，
# 可以使用 collections 模块中的 OrderedDict 类。
# 在迭代操作的时候它会保持元素被插入时的顺序，
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
d['foo'] = 5
for key in d:
    print(key, d[key])
import json
print(json.dumps(d))
