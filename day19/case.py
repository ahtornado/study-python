#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/14 12:51
# @File    :case.py

import sys
ops = ['create', 'modify', 'delete']
op = sys.argv[1]

if op in ops:
    print "%s user" % op
else:
    print "Usage: create | modify | delete"