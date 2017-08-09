#! /usr/bin/python
# coding: utf-8
"""
    用于通过Email、WEB、SYSLOG、file等渠道读取信息
    并且可以根据关键字进行过滤，找到关心的信息
    最终通过树莓派的GPIO产生肉眼可见的光报警
    --------------------------------
    create by wangtao   2017.08.04
"""
import sys
import os
import commands

#reload(sys)
#sys.setdefaultencoding('utf-8')

from mail_exchange import *
from make_keyword_list import *
from filter_words import *
from light import *

def function(argv_a,argv_b):
    print argv_a+argv_b
    argv_c = argv_a+argv_b
    return argv_c

if __name__ == '__main__':
    #print "main"
    #function('aa','bb')
    input_list = mail_exchange()

    list = filter_words(input_list,make_keywords())
    #for n in list:
    #    print n
    if len(list)>2:
        print "FLASH!!!"
        light_flash(len(list))