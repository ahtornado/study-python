#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/21 15:17
# @File    :deco.py

import time


def loop():
    result = []
    for i in range(1, 6):
        result.append(i)
        time.sleep(1)
    return result


if __name__ == '__main__':
    start = time.time()
    print loop()
    end = time.time()
    print "Program cost %5.3f seconds" % (end - start)