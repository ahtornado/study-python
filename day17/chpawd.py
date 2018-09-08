#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/1 12:51
# @File    :chpawd.py

import sys
import paramiko
import threading

def remote_comm(host, pwd, comm):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username='root', password=pwd)
    stdin, stdout,stderr = ssh.exec_command(comm)
    print stdout.read(),
    print stderr.read(),
    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print "Usage: %s ipfile oldpas newpass" % sys.argv[0]
    else:
        ipfile = sys.argv[1]
        oldpass = sys.argv[2]
        newpass = sys.argv[3]
        ch_pwd = "echo %s | passwd --stdin root" % newpass
        fobj = open(ipfile)
        for line in fobj:
            ip = line.strip()
            t = threading.Thread(target=remote_comm,args=(ip, oldpass, ch_pwd))
            t.start()
        fobj.close()