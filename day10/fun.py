#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/11/1 22:01
# @File    :fun.py


def printinfo(*a, **aa):
    print a
    print info


atuple = (1, 2, 3)
info = {'name': 'tom', 'age': 28}
printinfo(*atuple, **info)




