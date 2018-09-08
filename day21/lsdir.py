#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/21 11:47
# @File    :lsdir.py

import os
import sys


def lsdir(folder):
    contents = os.listdir(folder)
    print "%s:\n%s\n" % (folder, contents)
    for item in contents:
        full_path = os.path.join(folder, item)
        if os.path.isdir(full_path):
            lsdir(full_path)


if __name__ == '__main__':
    lsdir(sys.argv[1])