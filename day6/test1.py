#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/10/27 22:53
# @File    :test1.py


# 打开文件
import codecs

fo = codecs.open("file.txt", "r")
for line in fo.readlines():
    line = line.strip()
    print "读取的数据是：%s" % (line)

# 关闭文件
fo.close()


