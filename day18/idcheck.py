#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/1 17:26
# @File    :idcheck.py

import string

first_chs = string.letters + '_'
other_chs = first_chs +string.digits

def check_id(myid):
    if myid[0] not in first_chs:
        print "1st char invalid."
        return

    for ind ,ch in enumerate(myid[1:]):
        if ch not in other_chs:
            print "char in position:%s invalid." % (ind +2)
            break

    else:
        print "%s is valid." % myid


if __name__ == '__main__':
    myid = raw_input("id to check: ")
    check_id(myid)