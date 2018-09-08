#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/10/30 21:48
# @File    :mysort.py

# 把一个数字的list从小到大排序，然后写入文件，
# 然后再从文件中读取出来文件内容，反序排列，再追加到文件的下一行中
import codecs

import re

lists = [2, 32, 43, 453, 54, 6, 576, 5, 7, 6, 8, 78, 7, 89]


def fanxu(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] < lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    fo = open("sort.txt", "a")
    fo.write('\n')
    fo.write(str(lists))
    fo.close()


def asort(alist):
    blist = sorted(lists)
    writefile(str(blist))


def readfile():
    fo = codecs.open("sort.txt", "r")
    for line in fo.readlines():
        line = line.strip()
    find_lst = re.findall('\[(.*?)\]', line)
    result = find_lst[0].strip(',').split(',')
    blist = map(eval, result)
    # paixu(blist)
    fo.close()
    fanxu(blist)


def writefile(afile):
    fo = open("sort.txt", "w")
    fo.write(afile)
    fo.close()


if __name__ == '__main__':
    asort(lists)
    readfile()
