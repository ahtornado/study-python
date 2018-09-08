#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/14 20:44
# @File    :ralway.py

import sys
import time
sys.stdout.write('#' * 20)
sys.stdout.flush()
counter = 0

while True:
    sys.stdout.write('\r%s@%s' % ('#' * counter, '#' * (19 - counter)))
    sys.stdout.flush()
    counter += 1
    time.sleep(0.2)
    if counter == 20:
        counter = 0
