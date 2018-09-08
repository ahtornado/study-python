#!/usr/bin/env python
# _*_coding:utf_8_*_
# Author:Alvin.xie


f = open('data.txt', 'w')
f.write('hello\n')
f.write('world\n')
f.close()

f = open('data.txt', "r")
print f

bytes1 = f.read()
print bytes1
print bytes1.split()


class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay *= (1.0+percent)


bob = Worker('Bob Smith', 50000)
sue = Worker('sue Jone', 60000)
print bob.lastname()

print sue.lastname()
print sue.giveraise(0.1)
print sue.pay
