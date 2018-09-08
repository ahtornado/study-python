#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/10/15 19:43
# @File    :convertip.py


def int2ip(num):
    ip_list = []
    for i in range(4):
        num, mod = divmod(num, 256)
        ip_list.insert(0, str(mod))

    return '.'.join(ip_list)


def ip2int(ip):
    ip_list = ip.split('.')
    num = 0
    for i in range(len(ip_list)):
        num += int(ip_list[i]) * 256 ** (3-i)
    return num


if __name__ == '__main__':
    print int2ip(3232235786)
    print ip2int('192.168.1.10')
