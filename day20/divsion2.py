#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/15 11:50
# @File    :divsion2.py

import sys
try:
    num = int(raw_input("Please input a number: "))
    result = 100.0 / num
except (KeyboardInterrupt, EOFError):
    print "User Cancelled!"
    sys.exit(1)
except (ValueError, ZeroDivisionError), e:
    print "Invalid input.", e
    sys.exit(2)

print result