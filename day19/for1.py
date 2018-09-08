#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/14 15:23
# @File    :for1.py

astr = 'hello'
alist = ['tudou', 'cn']
adict = {'name': 'bob', 'age': 21}
aset = set(["new","world"])
myiter = iter((10, 20))
fname = '/etc/hosts'

for ch in astr: print ch
for item in alist: print item
for key in adict: print "%s: %s" % (key, adict[key])
for element in aset: print element
for i in myiter: print i
fobj = open(fname)
for line in fobj:
    print line,
fobj.close()