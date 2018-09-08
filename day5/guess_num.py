#!/usr/bin/env python
# _*_coding:utf_8_*_
# Author:Alvin.xie
import random
retry_count = 0
# 随机产生一个10以内的数
real_num = random.randrange(10)
# while retry_count < 3:
for i in range(3):
    guess_num=raw_input("Please guess the real num: ").strip()
    # 判断长度是否为 0
    if len(guess_num) == 0:
        continue
    # 判断是否为数字
    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print "You need input num"
        continue
    if guess_num > real_num:
        print "Wrong ! you need try smaller!"
    elif guess_num < real_num:
        print "Wrong ! you need try bigger!"
    else:
        print "Congratulations! you successful!"
        break

else:
    print "The real num is :", real_num

