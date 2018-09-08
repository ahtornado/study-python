#!/usr/bin/env python
# _*_coding:utf_8_*_
# Author:Alvin.xie

import start
import math
import random

a = 123+123
print a

print math.pi
print math.sqrt(121)

print random.random()
print random.choice([1, 3, 5, 7, 9, 11, 13])


start.pstart()
print "------------------------------------------"

s = 'spam'
print len(s)

print s[1]
print s[-1]
print s[1:3]
print s[:3]
print s[1:]
print s[0:]
print s[:]
print s
print s.replace("pa", "xyz")

line = "aaa,bbb,cc,dd"
print line.split(",")
