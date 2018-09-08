# -*- coding:utf-8 -*-
# Author:Alvin Xie


import string

print "hello world!"

data = "hello $name. I will see you ${day}"
t = string.Template(data)
print t.substitute(name='tom', day='tomorrow')
