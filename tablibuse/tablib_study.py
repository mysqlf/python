#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tablib
head = ('first_name', 'last_name')
data = [('John', 'Adams'),
        ('George', 'Washington')
        ]
data = tablib.Dataset(*data, headers=head)
data.append(('Zuo', 'Lang'))
data.append_col((90, 67, 83), header='age')
# print(data[:2])
# # [('John', 'Adams', 90), ('George', 'Washington', 67)]
# print(data['first_name'])
# # ['John', 'George', 'Zuo']
# print(data.json)
# # [{"first_name": "John", "last_name": "Adams", "age": 90}, {"first_name": "George", "last_name": "Washington", "age": 67}, {"first_name": "Zuo", "last_name": "Lang", "age": 83}]
# print(data.yaml)
# - {age: 90, first_name: John, last_name: Adams}
# - {age: 67, first_name: George, last_name: Washington}
# - {age: 83, first_name: Zuo, last_name: Lang}
# print(data.csv)

# first_name,last_name,age

# John,Adams,90

# George,Washington,67

# Zuo,Lang,83
