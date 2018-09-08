#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/15 16:59
# @File    :mathgame.py

import random

#def add(x, y):
#    return x + y

#def sub(x, y):
#    return x - y


def probe():
    #CMDs = {'+': add, '-': sub}
    CMDs = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nums = [random.randint(1, 50) for i in range(2)]
    nums.sort(reverse=True)
    op = random.choice('+-')
    answer = CMDs[op](*nums)
    prompt = "%s %s %s = " % (nums[0], op, nums[1])

    tries = 0
    while tries < 3:
        try:
            result = int(raw_input(prompt))
        except:
            continue
        if answer == result:
            print 'Very good!'
            break
        print 'Wrong answer.'
        tries += 1
    else:
        print "\033[31;1m%s%s\033[0m" % (prompt, answer)


if __name__ == '__main__':
    while True:
        probe()
        try:

            yn = raw_input("Continue(y/n)?").strip()[0]
        except (KeyboardInterrupt,EOFError):
            print "\nBye-bye"
            yn = 'n'
        except IndexError:
            continue
        if yn in 'nN':
            break
