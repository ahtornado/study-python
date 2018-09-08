#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/15 11:34
# @File    :divsion.py

import sys
try:
    num = int(raw_input("Please input a number: "))
    result = 100 / num
except:
    print "Some Error"
    sys.exit(1)

print result