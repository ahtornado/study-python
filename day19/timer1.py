#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/14 20:40
# @File    :timer1.py

import time
import sys

for i in range(1,11):
    sys.stdout.write("\r%s" % i)
    sys.stdout.flush()
    time.sleep(0.5)
