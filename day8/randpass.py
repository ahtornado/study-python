# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alvin.Xie

import random
import string

all_chs = string.letters + string.digits


def gen_pass(num=8):
    pwd = []
    for i in range(num):
        ch = random.choice(all_chs)
        pwd.append(ch)
    return ''.join(pwd)


if __name__ == '__main__':
    print gen_pass()

