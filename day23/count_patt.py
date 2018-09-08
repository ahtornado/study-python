#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/8/19 17:55
# @File    :count_patt.py

import re
import collections


class CountPatt(object):
    def __init__(self, patt):
        self.cpatt = re.compile(patt)

    def count_patt(self, fname):
        c = collections.Counter()
        with open(fname) as fobj:
            for line in fobj:
                m = self.cpatt.search(line)
                if m:
                    c.update([m.group])
        return c


if __name__ == '__main__':
    log_file = '/var/log/httpd/access_log'
    ip_patt = "^(\d+\.){3}\d+"
    br_patt = "Firefox|MSIE"
    c1 = CountPatt(ip_patt)
    print c1.count_patt(log_file)
    print c1.count_patt(log_file).most_common(2)
    c2 = CountPatt(br_patt)
    print c2.count_patt(log_file)
    print c2.count_patt(log_file).most_common(2)
