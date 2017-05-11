#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 审查清理文本字符串
s = 'pýtĥöñ\fis\tawesome\r\n'
print(ascii(s))

remap = {
    ord('\t'): '',
    ord('\f'): '',
    ord('\r'): None,  # deleted
}
a = s.translate(remap)
print(ascii(a))

# 格式化字符串
#
text = "hello world"
tmp = text.ljust(20)
print(tmp)
tmp = text.rjust(20)
print(tmp)
tmp = text.center(20)
print(tmp)
# 对齐方法可以填充字符
tmp = text.rjust(20, '=')
print(tmp)
tmp = text.ljust(20, '^')
print(tmp)
tmp = text.center(20, '*')
print(tmp)

# format也可以格式化
tmp = format(text, '>20')
print(tmp)
tmp = format(text, '<20')
print(tmp)
tmp = format(text, '^20')
print(tmp)

tmp = format(text, '=>20s')  # 前面填充
print(tmp)
tmp = format(text, '@<20s')  # 后面填充
print(tmp)
tmp = format(text, '*^20s')
print(tmp)

tmp = '{:>10s} {:>10s}'.format('hello', 'world')
print(tmp)
tmp = '{:^10s} {:^10s}'.format('hello', 'world')
print(tmp)

x = 1.2345
tmp = format(x, '>10')
print(tmp)

tmp = format(x, '^10.2f')
print(tmp)

# 拼接字符串

parts = ['Is', 'Chi', 'Not', 'Chis']
tmp = ' '.join(parts)
print(tmp)
tmp = ','.join(parts)
print(tmp)
tmp = ''.join(parts)
print(tmp)
# 使用加号(+)操作符去连接大量的字符串的时候是非常低效率的，
# 因为加号连接会引起内存复制以及垃圾回收操作
a = 'Is Chi'
b = 'Not Chis'
tmp = a + ' ' + b
print(tmp)

a = '123'
b = '456'
tmp = a + ' ' + b
print(tmp)

data = ['ACME', 50, 91.1]
tmp = ','.join(str(d) for d in data)
print(tmp)

a = '123'
b = '456'
c = '789'
print(a, b, c, sep=':')
