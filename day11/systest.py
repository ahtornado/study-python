#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/11/11 9:28
# @File    :systest.py

import sys
# 使用sys.argv[0]获得脚本名称
print 'Script name is :', sys.argv[0]
# 根据sys.path的路径来搜索module.name
print 'Path has', sys.path

# 使用sys模块查找内建模块


def dump(module):
    print module, '=>',
    if module in sys.builtin_module_names:
        print '内建模块'
    else:
        module = __import__(module)
        print module.__file__


dump("os")
dump("sys")
dump("string")
dump("strop")
dump("zlib")
