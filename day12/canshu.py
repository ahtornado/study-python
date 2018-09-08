#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/12/1 20:37
# @File    :canshu.py


import sys


def isNum(s):
    for i in s:
        if i in '0123456789':
            pass
        else:
            print "%s is not a number" %s
            sys.exit()
    else:
        print "%s is a number" %s


if __name__ == '__main__':
    isNum(sys.argv[1])