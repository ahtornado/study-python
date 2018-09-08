#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alvin.xie
import subprocess


# 查看系统信息
def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print "Gathering System information with %s commnd:\n" % uname
    subprocess.call([uname,uname_arg])


# 查看磁盘情况
def disk_func():
    """

    :rtype : object
    """
    diskspace = "df"
    diskspace_arg = "-h"
    print "Gathering Diskpace information with %s commnd:\n" % diskspace
    subprocess.call([diskspace, diskspace_arg])

# 主函数调用


if __name__ == '__main__':
    uname_func()
    disk_func()
