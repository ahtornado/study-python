#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/22 19:39
# @File    :addressbook3.py


class AddrBook(object):
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def update_phone(self, newph):
        self.phone = newph
        print "Now, %s phone number is: %s" % (self.name, self.phone)


class EmplAddrBook(AddrBook):
    def __init__(self, nm, ph, em, eid):
        AddrBook.__init__(self, nm, ph)
        self.email = em
        self.eid = eid

    def get_email(self):
        return self.email


if __name__ == '__main__':
    bob = EmplAddrBook("Bob Green", "13377558899", "bob.qq.com", "35099")
    print bob.get_phone()
    print bob.get_email()
    print bob.eid
