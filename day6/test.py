#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/10/27 22:35
# @File    :test.py

f = open("aa", 'r')
# read是逐字符地读取,是read可以指定参数，设定需要读取多少字符，无论一个英文字母还是一个汉字都是一个字符
f_read = f.read()
print (f_read)
f.close()


f1 = open("aa", 'r')
# readline只能读取第一行代码，原理是读取到第一个换行符就停止。
f1_read = f1.readline()
print (f1_read)
f1.close()


f2 = open("aa", 'r')
# readlines会把内容以列表的形式输出。
f2_read = f2.readlines()
print (f2_read)
f2.close()

#使用for循环可以把内容按字符串输出。
# 输出一行内容输出一个空行，一行内容一行空格... 因为文件中每行内容后面都有
#一个换行符，而且print()语句本身就可以换行，如果不想输出空行，就需要使用下面的语句：：print(line.strip())
f3 = open('aa','r')
for line in f3.readlines():
    # print(line)
    print(line.strip())
f3.close()


