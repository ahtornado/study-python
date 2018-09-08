#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2017/11/11 9:19
# @File    :commands1.py

import commands

threshold = 10
flag = False

title=commands.getoutput("df -h|head -1")

''''' 
Check sda disk space usage like below format: 
/dev/sda2              20G  2.3G   17G  13% / 
/dev/sda6              20G  306M   19G   2% /var 
/dev/sda3              49G  2.8G   44G   7% /home 
/dev/sda5              49G  4.5G   42G  10% /opt 
/dev/sda1             194M   12M  172M   7% /boot 
'''

chkDiskList = commands.getoutput("df -h|grep sda").split('\n')
usedPercents = commands.getoutput("df -h|grep sda|awk '{print $5}'|grep -Eo '[0-9]+'").split('\n')

for i in range(0, len(usedPercents)):
    if int(usedPercents[i]) >= threshold:
        chkDiskList[i] += '    ----Caution!!! space usage >= ' + str(threshold)
        flag = True

''''' 
Check disk space usage like below format: 
/dev/mapper/backup-backup_lv 
                      751G   14G  699G   2% /backup 
/dev/mapper/data-data_lv 
                      751G  172G  540G  25% /data 
'''

chkDiskList_2 = commands.getoutput("df -h|grep -v sda|grep -v tmp|grep -v system").split('\n')
usedPercents_2 = commands.getoutput(
    "df -h|grep -v map|grep -v sda|grep -v tmp|grep -v system|awk '{print $4}'|grep -Eo '[0-9]+'").split('\n')

for i in range(0, len(usedPercents_2)):
    if int(usedPercents_2[i]) >= threshold:
        chkDiskList_2[i * 2 + 1] += '    ----Caution!!! space usage >= ' + str(threshold)
        flag = True


if flag == True:
    # combine tile, chkDiskList, chkDisklist_2
    result = [title, ]
    result.extend(chkDiskList)
    result.extend(chkDiskList_2)
    for line in result:
        print line