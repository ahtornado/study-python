#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/12/3 20:10
# @File    :c1.py


class People(object):
    color = 'yellow'

    def think(self):
        self.color = "black"
        print "I am a %s" % self.color
        print "I am a thinker"


ren = People()
print ren.color
ren.think()