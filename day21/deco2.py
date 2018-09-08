#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/21 15:54
# @File    :deco2.py

#装饰器

import time


def deco(func):
    def timeit():
        start = time.time()
        res = func()
        end = time.time()
        print "Program cost %5.3f seconds" % (end - start)
        return res

    return timeit


@deco
def loop():
    result = []
    for i in range(1, 6):
        result.append(i)
        time.sleep(1)
    return result


if __name__ == '__main__':
    print loop()