#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/11/6 22:41
# @File    :class1.py


# 类定义
class People:
    name = ''
    age = 0
    _weight = 0
    _grade = 0

    def __init__(self, n, a, w, g):
        self.name = n
        self.age = a
        self._weight = w
        self._grade = g

    def speak(self):
        print ("%s is speaking: I am %d years old" % (self.name, self.age))


p = People('tom', 10, 30, 1)
p.speak()


class Speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print ("I am %s,I am a speaker!My topic is %s" % (self.name, self.topic))


test = Speaker('Tim', 'Python')
test.speak()


# 多重继承
class Sample(Speaker, People):
    a = ''
    # _grade = 4

    def __init__(self, n, a, w, g, t):
        People.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)
        print ("I am %s,I am %d years old,and I am %d, I am in grade %d and my topic is %s" % (self.name, self.age, self._weight, self._grade, self.topic))


test = Sample('Ken', 25, 80, 4, 'python')
