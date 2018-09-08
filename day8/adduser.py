# #!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alvin.Xie

import sys
import randpass
import os
import string
contents = """username: ${username}
password: ${password}
"""
t = string.Template(contents)


def adduser(user, passwd, email):
    os.system("useradd %s" % user)
    os.system("echo %s | passwd --stdin %s" % (passwd, user))
    data = t.substitute(username=user, password=passwd)
    os.system("echo -e '%s' | mail -s 'user info' %s" % (data, email))


if __name__ == '__main__':
    username = sys.argv[1]
    pwd = randpass.gen_pass()
    adduser(username, pwd, 'root@localhost')