#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/6/10 18:03
# @File    :ping.py

import os

for i in xrange(1,255):
    ip = "192.168.0.%s" % i
    result = os.system("ping -c2 %s &> /dev/null" % ip)
    if result:
        print "%s: down" % ip
    else:
        print "%s: up" % ip