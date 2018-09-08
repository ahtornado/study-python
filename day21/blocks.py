#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/21 22:20
# @File    :blocks.py


def blocks(fobj):
    block = []
    counter = 0
    for line in fobj:
        block.append(line)
        counter += 1
        if counter == 10:
            yield block
            counter = 0
            block = []
    yield block


if __name__ == '__main__':
    with open('/etc/passwd') as fobj:
         a = blocks(fobj)
         for lines in a:
             print lines


         '''
             for lines in blocks(fobj):
                 print lines

         '''