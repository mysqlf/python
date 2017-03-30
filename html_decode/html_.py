# from html.parser import HTMLParser
# from html.entities import name2codepoint


# class MyHTMLParser(HTMLParser):

#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)

#     def handle_endtag(self, tag):
#         print('</%s>' % tag)

#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)

#     def handle_data(self, data):
#         print(data)

#     def handle_comment(self, data):
#         print('<!--', data, '-->')

#     def handle_entityref(self, name):
#         print('&%s;' % name)

#     def handle_charref(self, name):
#         print('&#%s;' % name)

# parser = MyHTMLParser()
from html.parser import HTMLParser
from html.entities import name2codepoint
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 改变标准输出的默认编码
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
# cmd运行编码


# class MyHTMLParser(HTMLParser):

#     def handle_starttag(self, tag, attrs):
#         print("Start tag:", tag)
#         for attr in attrs:
#             print("     attr:", attr)

#     def handle_endtag(self, tag):
#         print("End tag  :", tag)

#     def handle_data(self, data):
#         print("Data     :", data)

#     def handle_comment(self, data):
#         print("Comment  :", data)

#     def handle_entityref(self, name):
#         c = chr(name2codepoint[name])
#         print("Named ent:", c)

#     def handle_charref(self, name):
#         if name.startswith('x'):
#             c = chr(int(name[1:], 16))
#         else:
#             c = chr(int(name))
#         print("Num ent  :", c)

#     def handle_decl(self, data):
#         print("Decl     :", data)

# parser = MyHTMLParser()
# parser.feed(
#     '<html><head></head><body><span class="age stonefont">&#xece7;&#xecef;岁</span></body></html>')
import re
import binascii
# print(re.sub(r'&#x....;',
#              lambda match: convert(match.group()),
#              ss))
# print(binascii.hexlify('&#xecef'))  # .decode("hex"))
# print(binascii.unhexlify('&#xecef'))

from lxml import html
text = '&#x4e2d'
#;&#xed10;
print(html.fromstring(text).text)


def convert(s):
    s = s.strip('&#x;')  # 把'&#x957f;'变成'957f'
    s = bytes(r'\u' + s, 'ascii')  # 把'957f'转换成b'\\u957f'
    return s.decode('unicode_escape')

print(convert('&#xece7;&#xecef;'))  # => '长'&#x957f;


def _chunks(str, chunk_size):
    for i in range(0, len(str), chunk_size):
        yield str[i:i + chunk_size]


def hex_to_bin(hex):
    return ''.join('{:08b}'.format(int(x, 16)) for x in _chunks(hex, 2))


def str_to_bin(str):
    return ''.join('{:08b}'.format(ord(c)) for c in str)


def bin_to_hex(bin):
    return ''.join('{:02x}'.format(int(b, 2)) for b in _chunks(bin, 8))


def str_to_hex(str):
    return ''.join('{:02x}'.format(ord(c)) for c in str)


def bin_to_str(bin):
    return ''.join(chr(int(b, 2)) for b in _chunks(bin, 8))


def hex_to_str(hex):
    return ''.join(chr(int(x, 16)) for x in _chunks(hex, 2))
# print(hex_to_str("&#xece7;;"))
# from html.parser import HTMLParser
# from html.entities import name2codepoint


# class MyHTMLParser(HTMLParser):

#     def handle_starttag(self, tag, attrs):
#         print("Start tag:", tag)
#         for attr in attrs:
#             print("     attr:", attr)

#     def handle_endtag(self, tag):
#         print("End tag  :", tag)

#     def handle_data(self, data):
#         print("Data     :", data)

#     def handle_comment(self, data):
#         print("Comment  :", data)

#     def handle_entityref(self, name):
#         c = chr(name2codepoint[name])
#         print("Named ent:", c)

#     def handle_charref(self, name):
#         if name.startswith('x'):
#             c = chr(int(name[1:], 16))
#         else:
#             c = chr(int(name))
#         print("Num ent  :", c)

#     def handle_decl(self, data):
#         print("Decl     :", data)

# parser = MyHTMLParser()
# parser.feed('&gt;&#62;&#x3E;')
