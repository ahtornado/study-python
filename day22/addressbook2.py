#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/22 19:15
# @File    :addressbook2.py


class Info(object):
    def __init__(self, ph, em, qq):
        self.phone = ph
        self.email = em
        self.myqq = qq

    def get_phone(self):
        return self.phone

    def update_phone(self, newph):
        self.phone = newph

    def get_email(self):
        return self.email

    def update_email(self, newem):
        self.email = newem

    def get_qq(self):
        return self.myqq

    def update_myqq(self, newqq):
        self.myqq = newqq


class AddrBook(object):
    def __init__(self, nm, ph, em, qq):
        self.name = nm
        self.info = Info(ph, em, qq)


if __name__ == '__main__':
    bob = AddrBook("Bob Green", "139667788", "bob@qq.com", "98702568")
    print bob.info.get_phone()
    print bob.info.get_email()
