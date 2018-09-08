#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/12/3 22:56
# @File    :c3.py


class People(object):
    color = 'yellow'

    def __init__(self):
        self.dwell = 'Earth'

    def think(self):
        print "I am a %s" % self.color
        print "I am a thinker"


class Chiness(People):
    pass


cn = Chiness()
print cn.dwell
cn.think()