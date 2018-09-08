#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/12/8 21:13
# @File    :input.py

name = raw_input("please input a name:")
age = raw_input("please input your age:")
job = raw_input("please input your job:")
salary = raw_input("please input your Salary:")

info = '''
-------------info of %s-------------------
Name:%s
Age:%s
Job:%s
Salary:%s
''' % (name, name, age, job, salary)

print (info)
