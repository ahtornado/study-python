#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/15 11:14
# @File    :game.py

import random
ch_list = ["石头","剪刀","布"]
win_list = [["石头","剪刀"],["剪刀","布"],["布","石头"]]
prompt = '''(0) 石头
(1) 剪刀
(2) 布
请选择（0/1/2）: '''

computer = random.choice(ch_list)

ind = int(raw_input(prompt))
player = ch_list[ind]


print "Your choice: %s,Computer's choice: %s" %(player,computer)

if [player,computer] in win_list:
    print "\033[31;1m你赢了!\033[0m"
elif player == computer:
    print "\033[32;1m平局\033[0m"
else:
    print "\033[31;1m你输了！\033[0m"
