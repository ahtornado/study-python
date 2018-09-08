#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/6/17 22:59
# @File    :mtping.py

import os
import threading

def ping(ip):
    result = os.system("ping -c2 %s &> /dev/null" % ip)
    if not result:
        print "%s:up" % ip
    else:
        print "%s:down" % ip

if __name__ == '__main__':
    for i in range(1, 255):
        ipaddr = "192.168.0.%s" % i
        t = threading.Thread(target=ping, args=[ipaddr])
        t.start()