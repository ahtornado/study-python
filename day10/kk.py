#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/10/31 0:44
# @File    :kk.py

import re


# a = 'abc[1,2,3]abc'
n = '[2,5,6,6,7,7,8,32,43,54,78,89,453,576]'
find_lst = re.findall('\[(.*?)\]', n)
result = find_lst[0].strip(',').split(',')
blist = map(eval, result)
print blist.reverse()
print type(result)

