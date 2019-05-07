#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

mode = ""
usage = True

# options / usage
if 2 == len(sys.argv):
    mode = sys.argv[1]

if "mount" == mode or "umount" == mode or "fstab" == mode:
    usage = False

if True == usage:
    print "USAGE:\n"
    print "  {}  mount | umount | fstab \n".format(sys.argv[0])
    print "NOTE:\n"
    print "  mount and umount require root privilege"
    sys.exit()
    

# resources
src = '//NAS_01/'
mpoint = '/mnt/nas_01/'
subdirs = [ 'admin', 'renkei_user', 'イラスト', 'バックアップ', 'プレゼンテーション', '共有', '写真', '動画', '文書', '進行中の業務', '運営', '音楽' ]

# mount, umount or fstab
for trg in subdirs:
    sp = src + trg
    mp = mpoint + trg

    if "fstab" == mode:
        print sp, "\t", mp, "\t", "drvfs\tdefaults\t0 0"
        continue
    elif "mount" == mode:
        if True == os.path.isdir(mp):
            print "exist: " + mp
        else:
            os.makedirs(mp)

        cmd = 'mount -t drvfs' + ' ' + sp + ' ' + mp
    else:
        cmd = 'umount' + ' ' + mp
    
    #print cmd
    subprocess.call(cmd.split())
