#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/12/3 21:41
# @File    :c2.py


class People(object):
    color = 'yellow'
    __age = 30

    def think(self):
        self.color = "black"
        print "I am a %s" % self.color
        print "I am a thinker"
        print self.__age


ren = People()
print ren.color
ren.think()
print ren.__dict__
