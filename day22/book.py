#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/25 21:19
# @File    :book.py

# 魔法方法


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title

    def __call__(self):
        print "%s is written by %s " % (self.title, self.author)


if __name__ == '__main__':
    pybook = Book("Core Python", "Wesley")
    print pybook    # 因为类中定义了__str__方法，此处打印出的内容是__str__的返回值。
    pybook()        # 有了__call__方法，pybook 创建的对象就可以调用了。