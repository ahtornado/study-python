#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/12/3 20:19
# @File    :wc.py


def wordCount(s):
    chars = len(s)
    words = len(s.split())
    lines = s.count('\n')
    print lines, words, chars


s = open('/etc/passwd').read()

if __name__ == '__main__':
    wordCount(s)
