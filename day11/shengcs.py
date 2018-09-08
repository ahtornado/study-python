#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/11/3 22:00
# @File    :shengcs.py

m = [x for x in range(1, 10)]
print m

g=(x for x in range(1, 10))
print g.next()
print g.next()

for x in g:
    print x