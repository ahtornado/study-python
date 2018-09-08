# #!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alvin.Xie

from string import whitespace


def lrmsps(astr):
    str_list = list(astr)
    for i in range(len(str_list)):
        if str_list[0] not in whitespace:
            break
        str_list.pop(0)
    return "".join(str_list)


def rrmsps(astr):
    str_list = list(astr)
    for i in range(len(str_list)):
        if str_list[-1] not in whitespace:
            break
        str_list.pop()
    return "".join(str_list)


def rmsps(astr):
    return rrmsps(lrmsps(astr))


if __name__ == '__main__':
    hi = "    hell0   \t"
    print "|%s|" % lrmsps(hi)
    print "|%s|" % rrmsps(hi)
    print "|%s|" % rmsps(hi)