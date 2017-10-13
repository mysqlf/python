#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Greedywolf
# 句子翻转
def str_reverse(str_src):
    #句子分割为list
    str_dst=str_src.split()
    #翻转list
    str_dst.reverse()
    #返回翻转后的list
    return str_dst
if __name__ == '__main__':
    for str_out in str_reverse('please input your sentense'):
        print(str_out)
