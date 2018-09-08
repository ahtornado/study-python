#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/15 11:59
# @File    :divsion3.py

try:
    num = int(raw_input("Please input a number: "))
    result = 100.0 / num
except (KeyboardInterrupt, EOFError):
    print "User Cancelled!"
except (ValueError, ZeroDivisionError), e:
    print "Invalid input.", e
else:
    print result