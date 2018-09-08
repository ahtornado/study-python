#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/14 21:15
# @File    :u2d.py

import sys
import os

def unix2dos(fname):
    dfname = os.path.splitext(fname)[0] + '.win'
    src_fobj = open(fname)
    dst_fobj = open(dfname, 'w')

    for line in src_fobj:
        dst_fobj.write(line.rstrip('\n\r') + '\r\n')
    src_fobj.close()
    dst_fobj.close()


if __name__ == '__main__':
    if len(sys.argv) !=2:
        print "Usage: %s filename" % sys.argv[0]
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print "No such file: %s" % filename
        sys.exit(2)

    unix2dos(filename)