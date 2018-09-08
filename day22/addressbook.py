#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/22 17:53
# @File    :addressbook.py


class AddrBook(object):
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        self.city = 'Beijing'

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def update_phone(self, newph):
        self.phone = newph
        print "Now, %s phone number is: %s" % (self.name, self.phone)


if __name__ == '__main__':
    bob = AddrBook("Bbo Green", "18098641234")
    alice = AddrBook("Alice Smith", "15398646789")
    print "%s: %s" % (bob.get_name(), bob.get_phone())
    print "%s: %s" % (alice.get_name(), alice.get_phone())
    bob.update_phone('18612345678')
    print "%s: %s" % (bob.get_name(), bob.get_phone())
    #print "%s: %s" % (bob.name, bob.phone)