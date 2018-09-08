#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/21 16:10
# @File    :colorefun.py

#装饰器


def color(func):
    def color_font(astr):
        return "\033[31;1m%s\033[0m" % func(astr)
    return color_font


@color
def say_hi(word):
    return "Hello %s." % word


@color
def greet(name):
    return "Welcome %s!" % name


if __name__ == '__main__':
    print say_hi("kite")
    print greet('bob')

