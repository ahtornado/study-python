#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alvin.xie
# 使用类实现从本机ping 远程主机


class Server(object):
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname

    def set_ip(self, ip):
        self.ip = ip

    def set_hostname(self, hostname):
        self.hostname = hostname

    def ping(self, ip_addr):
        print "Pinging %s from %s (%s)" % (ip_addr, self.ip, self.hostname)


if __name__ == '__main__':
    server = Server('10.89.3.1', 'alvin')
    server.ping('10.89.1.3')

