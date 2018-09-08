#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/7 22:57
# @File    :rmsps2.py

from string import whitespace


def lrmsps(astr):
    str_list = list(astr)
    for i in range(len(str_list)):
        if str_list[0] not in whitespace:
            break
        str_list.pop(0)

    return ''.join(str_list)


def rrmsps(astr):
    str_list = list(astr)
    for i in range(len(str_list)):
        if str_list[-1] not in whitespace:
            break
        str_list.pop()

    return ''.join(str_list)


def rmsps(astr):
    return lrmsps(rrmsps(astr))


if __name__ == '__main__':
    #hi = ""
    #hi = "      "
    hi = "     hello \t"
    print "|%s|" % lrmsps(hi)
    print "|%s|" % rrmsps(hi)
    print "|%s|" % rmsps(hi)