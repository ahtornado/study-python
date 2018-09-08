#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/11/7 21:57
# @File    :class2.py


class A(object):

    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print 'A.__private()'

    def public(self):
        print 'A.public()'

    # 获取私有方法

    def get_pri(self):
        return self.__private()


a = A( )
a.get_pri()