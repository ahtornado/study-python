#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/15 11:45
# @File    :divsion1.py

import sys
try:
    num = int(raw_input("Please input a number: "))
    result = 100.0 / num
except (KeyboardInterrupt, EOFError):
    print "User Cancelled!"
    sys.exit(1)
except (ValueError, ZeroDivisionError):
    print "Invalid input."
    sys.exit(2)

print result