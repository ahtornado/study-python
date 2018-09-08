#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/11/7 22:48
# @File    :class4.py


class testPrivate:
    def __init__(self):
        self.__data = []

    def add(self, item):
        self.__data.append(item)

    def printData(self):
        print (self.__data)


t = testPrivate()
t.add('tom')
t.add('hello')
# t.printData()
print(t._testPrivate__data)