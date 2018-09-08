#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/12/1 22:25
# @File    :digui.py


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    print fact(1)
    print fact(5)
