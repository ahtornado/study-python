#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/6/10 15:47
# @File    :while_web.py

import webbrowser
import time

url = "http://www.baidu.com"
counter = 0
while counter  < 11:
    webbrowser.open_new_tab(url)
    time.sleep(1)
    counter += 1