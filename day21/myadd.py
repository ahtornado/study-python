#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/18 21:09
# @File    :myadd.py

from functools import partial


def add(x, y):
    return x+y


if __name__ == '__main__':
    print add(10, 8)
    print add(10, 30)
    print add(10, 5)
    add10 = partial(add, 10)
    print add10(50)

