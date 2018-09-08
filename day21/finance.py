#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/16 19:52
# @File    :finance.py

import os
import cPickle as p
import time


def spend_money(*args):
    with open(wallet) as fobj:
        balance = p.load(fobj) - amount
    with open(wallet, 'w') as fobj:
        p.dump(balance, fobj)

    with open(record, 'a') as fobj:
        fobj.write(
            "%-12s%-8s%-8s%-10s%-20s\n" % (date ,amount, 'N/A', balance, comment)
        )


def save_money(*args):
    with open(wallet) as fobj:
        balance = p.load(fobj) + amount
    with open(wallet, 'w') as fobj:
        p.dump(balance, fobj)

    with open(record, 'a') as fobj:
        fobj.write(
            "%-12s%-8s%-8s%-10s%-20s\n" % (date, 'N/A', amount, balance, comment)
        )


def query_money(*args):
    print "%-12s%-8s%-8s%-10s%-20s" % \
          ('data', 'spend', 'save', 'balance','comment')
    with open(record) as fobj:
        for line in fobj:
            print line
    with open(wallet) as fobj:
        print "New Balance:\n%s" % p.load(fobj)


def show_menu(wallet, record):
    CMDs = {'0':spend_money, '1':save_money, '2': query_money}
    prompt = '''(0) spend money
(1) save money
(2) query money
(3) quit
Please input your choice(0/1/2/3): '''
    while True:
        try:
            choice = raw_input(prompt).strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            choice == '3'

        if choice not in '0123':
            print "Invalid choice. Try again."
            continue
        if choice == '3':
            print "Bye-bye"
            break
        args = (wallet, record)
        if choice in '01':
            date = time.strftime("%Y%m%d")
            try:
                amount = int(raw_input("amount: "))
                comment = raw_input("comment: ")
            except ValueError:
                print "Invalid number,Try again."
                continue
            except (KeyboardInterrupt,EOFError):
                print "\nBye-bye."
                break
            args = (wallet, record, date, amount, comment)
        CMDs[choice](*args)


if __name__ == '__main__':
    wallet = "wallet.data"
    record = "record.txt"
    if not os.path.exists(wallet):
        with open(wallet, 'w') as fobj:
            p.dump(10000, fobj)

    if not os.path.exists(record):
        os.mknod(record)

    show_menu(wallet, record)
