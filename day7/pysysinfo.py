#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alvin.xie

import subprocess
# 查看系统信息

uname = "uname"
uname_arg = "-a"

print "Gathering System information with %s commnd:\n" % uname
subprocess.call([uname, uname_arg])

# 查看磁盘情况

diskspace = "df"
diskspace_arg = "-h"

print "Gathering Diskpace information with %s commnd:\n" % diskspace
subprocess.call([diskspace, diskspace_arg])
