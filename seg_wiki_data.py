#!/usr/bin/env python
# -*- coding: utf-8 -*-
# seg_wiki_data.py 用于分词

import logging
import os.path
import sys
import jieba
from langconv import *

def simple2tradition(line):
    line = Converter('zh-hant').convert(line.decode('utf-8'))
    line = line.encode('utf-8')
    return line

def tradition2simple(line):
    line = Converter('zh-hans').convert(line.decode('utf-8'))
    line = line.encode('utf-8')
    return line

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    filepath = os.path.basename(sys.argv[1])
    i = 0
    f = open(filepath, "r")
    for line in f:
        line = tradition2simple(line)
        i += 1
        seg_list = jieba.cut(line, cut_all=False)
        m = list(" ".join(seg_list))
        with open("segfile", "a+") as f_out:
            for word in m:
                f_out.write(word.encode("utf-8"))
                #print word
        if i%10000 == 0: print str(i)+" lines ok!"
    f.close()
