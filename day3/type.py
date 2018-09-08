# _*_coding:utf_8_*_
# Author:Alvin.xie
import math
from string import split
edward = ['Edward Gumby', 42]
john = ['Johe Smith', 50]
database = [edward, john]
print(database)
print database[1]

# 使用import 导入模块，函数调用的时候需要带上模块名称


print math.sqrt(4)
# 下面这种方式不需要带上模块名称

s = "abc,def,ddd,123,efg"
print split(s, ',')
# 分片提取
tag = '<a href="http://www.python.org">python web site</a>'
print tag[9:30]

number = [1, 5., 2, 6, 9, 5, 7, 4, 3, 0, 8]
print number[::2]
print number[1::2]
print number[8:2:-2]

# 序列乘法
# sentence = raw_input("Sentence: ")
sentence = "Python is very good tools!"
screen_width = 80
text_width = len(sentence)
box_width = text_width+6
left_margin = (screen_width-box_width)//2

print
print ' '*left_margin+"+"+'-'*(box_width-4)+'+'
print ' '*left_margin+"| "+' '*text_width + ' |'
print ' '*left_margin+"| " +    sentence     + ' |'
print ' '*left_margin+"| "+' '*text_width + ' |'
print ' '*left_margin+"+"+'-'*(box_width-4)+'+'
print
