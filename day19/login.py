#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/8 22:21
# @File    :login.py

import getpass
db = {}


def new_user():
    user = raw_input("Username: ")
    pwd = raw_input("Password: ")

    if pwd == db.setdefault(user, pwd):
        print "Register successful."
    else:
        print "%s already exists." % user


def old_user():
    user = raw_input("Username: ")
    pwd = getpass.getpass("Password: ")
    if db.get(user) != pwd:
        print "Login incorrect."
    else:
        print "Login successful."


def show_menu():
    CMDs = {'0': new_user, '1': old_user}
    prompt = '''(0) new user
(1) old user
(2) quit
Please input your choice(0/1/2/):'''
    while True:
        choice = raw_input(prompt).strip()[0]
        if choice not in '012':
            print "Invalid choice,Try again."
            continue

        if choice == '2':
            break

        CMDs[choice]()


if __name__ == '__main__':
    show_menu()