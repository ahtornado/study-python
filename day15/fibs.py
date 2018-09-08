#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/6/10 17:39
# @File    :fibs.py

fib = [0,1]

number = int(raw_input("please input a number: "))

for i in range(number - 2):
    fib.append(fib[-1] + fib[-2])

print fib
