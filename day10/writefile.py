#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/10/30 21:45
# @File    :writefile.py

# 分别把 string， list， tuple， dict写入到文件中

astr = "I love python"
alist = [2, 6, 3, 9, 10, 12, 7]
atuple = ('a', 'p', 'y', 't', 'h', 'o', 'n')
adict = {'name': 'tom', 'address': 'shanghai'}

# print astr
# print alist
# print atuple
# print adict

blist = str(alist)
btuple = str(tuple(atuple))
bdict = str(adict)


def writefile(afile):
    fo = open("test.txt", "a")
    fo.write(afile)
    fo.write('\n')
    fo.close()


if __name__ == '__main__':
    writefile(astr)
    writefile(blist)
    writefile(btuple)
    writefile(bdict)
