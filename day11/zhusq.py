#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/11/3 23:47
# @File    :zhusq.py


for i in xrange(1, 10):
    for j in xrange(1, i + 1):
        print "%sx%s=%s" % (j, i, j * i),
    print

