#! /usr/bin/python
# coding: utf-8
"""
    根据keyword.cfg中的内容产生keywords_list
    --------------------------------
    create by wangtao   2017.08.04
"""
import sys
import os
import commands

#reload(sys)
#sys.setdefaultencoding('utf-8')

def make_keywords():
    keywords_list=[]
    keywords_list=['PROBLEM']
    return keywords_list