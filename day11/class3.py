#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/11/7 22:13
# @File    :class3.py


# 类定义
class People(object):
    name = 'ken'
    age = 39
    sex = 'F'

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def speak(self):
        print ("%s is speaking: I am %d years old" % (self.name, self.age))


p = People('tom', 10)
p.speak()


class Speaker(object):
    topic = ''
    name = 'bob'

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print ("I am %s,I am a speaker!My topic is %s" % (self.name, self.topic))


test = Speaker('Tim', 'Python')
test.speak()


#
class Sample(People, Speaker):
    a = ''

    def __init__(self):
        print 'my name is {0}'.format(self.name)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    # 类的重写，只需要重新定义

    def get_sex(self):
        print "sex is man"


a = Sample()
print a.get_name()
print a.get_age()
a.get_sex()


