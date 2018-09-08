#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/21 12:11
# @File    :lsdir1.py

import os
import sys


def lsdir(folder):
    for path, dirs, files in os.walk(folder):
        print "%s:\n%s\n" % (path, (dirs + files))


if __name__ == '__main__':
    lsdir(sys.argv[1])