#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author   :Alvin.Xie
# @Time    :2018/7/22 13:37
# @File    :backup.py

import time
import os
import tarfile
import cPickle as p
import hashlib


def check_md5(fname):
    # 计算文件的md5值，为了防止文件太大，占用内存，每次读4096
    m = hashlib.md5()
    with open(fname) as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def full_backup(src_dir, dst_dir, md5file):
    '''
    切割源目录，将要备份的目录及其所在的目录分开
    目录名称是：demo_full_20180122.tar.gz 在生成绝对路径
    '''
    md5dict = {}
    base_dir, back_dir = os.path.split(src_dir.rstrip('/'))
    back_name = "%s_full_%s.tar.gz" % (back_dir, time.strftime('%Y%m%d'))
    full_path = os.path.join(dst_dir, back_name)

    os.chdir(base_dir)
    tar = tarfile.open(full_path, 'w:gz')
    tar.add(back_dir)
    tar.close()

    for path, dirs, files in os.walk(src_dir):
        for each_file in files:
            full_name = os.path.join(path, each_file)
            md5dict[full_name] = check_md5(full_name)

    with open(md5file, 'w') as fobj:
        p.dump(md5dict, fobj)


def incr_backup(src_dir, dst_dir, md5file):
    base_dir, back_dir = os.path.split(src_dir.rstrip('/'))
    back_name = "%s_incr_%s.tar.gz" % (back_dir, time.strftime('%Y%m%d'))
    full_path = os.path.join(dst_dir, back_name)

    new_md5 = {}
    with open(md5file) as fobj:
        old_md5 = p.load(fobj)

    for path, dirs, files in os.walk(src_dir):
        for each_file in files:
            full_name = os.path.join(path, each_file)
            new_md5[full_name] = check_md5(full_name)

    with open(md5file, 'w') as fobj:
        p.dump(new_md5, fobj)

    os.chdir(base_dir)
    tar = tarfile.open(full_path, 'w:gz')
    for key in new_md5:
        if old_md5.get(key) != new_md5[key]:  #key值是文件名，如果不在是新文件，如果value值不一样，是改的的。
            tar.add(key.split(base_dir)[1].lstrip('/'))  #压缩的是相对路径
    tar.close()


if __name__ == '__main__':
    src_dir = '/home/demo'
    dst_dir = '/home/dst'
    md5file = '/home/dst/md5.data'
    if time.strftime("%a") == "Mon":
        full_backup(src_dir, dst_dir, md5file)
    else:
        incr_backup(src_dir, dst_dir, md5file)

