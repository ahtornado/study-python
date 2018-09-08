# #!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alvin.Xie

from string import whitespace


def lrmsps(astr):
    if not astr:
        return astr

    for i in range(len(astr)):
        if astr[i] not in whitespace:
            break
    else:
        return ""
    return astr[i:]


def rrmsps(astr):
    if not astr:
        return astr

    for i in range(-1, -(len(astr)+1), -1):
        if astr[i] not in whitespace:
            break
    else:
        return ""

    return astr[:(i+1)]


def rmsps(astr):
    return rrmsps(lrmsps(astr))


if __name__ == '__main__':
    hi = "    hello  \t"
#    hi = "    "
    print "|%s|" % lrmsps(hi)
    print "|%s|" % rrmsps(hi)
    print "|%s|" % rmsps(hi)
