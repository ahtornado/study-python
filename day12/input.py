#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/12/1 20:27
# @File    :input.py


def fun():
    sth = raw_input("please input something:")
    try:
        if type(int(sth)) == type(1):
            print "%s is a number" % sth
    except ValueError:
        print "%s is not number" % sth


if __name__ == '__main__':
    fun()