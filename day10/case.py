#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/10/23 23:33
# @File    :case.py


import sys

ops = ['create', 'modify', 'delete']

op = sys.argv[1]
if op in ops:
    print "%s user" % op
else:
    print "Usage: create | modify |delete user"

