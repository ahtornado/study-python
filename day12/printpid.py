#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/12/1 20:46
# @File    :printpid.py

import os


def isNum(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            break

    else:
        print "%s is a number" %s


for i in os.listdir('/proc'):
    isNum(i)