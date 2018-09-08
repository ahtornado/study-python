#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/15 11:17
# @File    :game_try.py

import random
import sys


ch_list = ["石头","剪刀","布"]
win_list = [["石头","剪刀"],["剪刀","布"],["布","石头"]]
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请选择（0/1/2）: '''

try:
    ind = int(raw_input(prompt))
    player = ch_list[ind]
except (KeyboardInterrupt, EOFError):
    print "\nBye bye"
    sys.exit(1)
except (ValueError, IndexError):
    print "Invalid input"
    sys.exit(2)

computer = random.choice(ch_list)
print "Your choice: %s,Computer's choice: %s" %(player,computer)

if [player,computer] in win_list:
    print "\033[31;1m你赢了!\033[0m"
elif player == computer:
    print "\033[32;1m平局\033[0m"
else:
    print "\033[31;1m你输了！\033[0m"