#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
from urllib.request import urlopen

class UrlTrmplate:
    def __init__(self,template):
        self.template=template
    def open(self,**kwargs):
        return urlopen(self.template.format_map(kwargs))
