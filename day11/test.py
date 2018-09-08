#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/11/3 23:03
# @File    :test.py
import time


def run():
    print "I'm run."


def run():
    print time.ctime()
    print "I'm run."
    print time.ctime()



# def fib(n):
#     a = 1
#     b = 1
#     i = 0
#
#     yield a
#     yield b
#
#     while(i<n):
#         a, b = b, a+b
#         i+=1
#         yield b
#
#
# for x in fib(10):
#     print x