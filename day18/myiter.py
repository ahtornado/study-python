#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/1 16:51
# @File    :myiter.py

alist = ["hello", "world"]

for item in alist:
    print item

for i in range(len(alist)):
    print "%s: %s" % (i, alist[i])

for element in enumerate(alist):
    print "%s: %s" % (element[0], element[1])

for m, n in enumerate(alist):
    print "%s: %s" % (m, n)