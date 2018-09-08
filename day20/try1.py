#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/15 10:43
# @File    :try1.py

import time

for i  in range(1,11):
    print i
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        #pass
        continue

print 'Game over!'