#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/21 12:29
# @File    :counter.py


def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]
    return incr


if __name__ == '__main__':
    a = counter()
    print a(); print a()
    b = counter(10)
    print b(); print b()
    print a()
    print b()