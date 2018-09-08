#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alvin.xie

import subprocess

from funsysinfo import disk_func


def tmp_space():
    tmp_usage = "du"
    tmp_arg = "-h"
    path = "/tmp"
    print "Space used in /tmp directory"
    subprocess.call([tmp_usage, tmp_arg, path])


# 主函数调用
if __name__ == "__main__":
    disk_func()
    tmp_space()
