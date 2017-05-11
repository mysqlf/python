#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from xml.parsers.expat import ParserCreate


class Defa(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s attrs:%s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element:%s' % name)

    def char_data(self, text):
        print('sax:char_data:%s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = Defa()
parsers = ParserCreate()
parsers.StartElementHandler = handler.start_element
parsers.EndElementHandler = handler.end_element
parsers.CharacterDataHandler = handler.char_data
parsers.Parse(xml)
