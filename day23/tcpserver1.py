#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/8/19 21:48
# @File    :tcpserver1.py

import socket

host = ''
port = 12345
addr = (host, port)

s = socket.socket(socket.AT_INET, socket.SOCK_STERAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:
    cli_sock, cli_addr = s.accept()
    print "Got connection from:", cli_addr
    data = cli_sock.recv(4096)
    print data
    cli_sock.send("I love you!\n")
    cli_sock.close()

s.close()