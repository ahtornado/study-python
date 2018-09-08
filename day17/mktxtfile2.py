#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/6/29 22:27
# @File    :mktxtfile2.py

import os

contents = []

while True:
    fname = raw_input("filename: ")
    if not os.path.exists(fname):
        break
    print "%s already exists. Try again." % fname

while True:
    data = raw_input("(Enter to quit)> ")
    if not data:
        break
    contents.append(data + '\n')

fobj = open(fname, 'w')
fobj.writelines(contents)
fobj.close()