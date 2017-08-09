#! /usr/bin/python
# coding: utf-8
"""
    input_list是个列表，在列表中包含读取到信息
    keywords_list是一个关键词列表
    用keyword过滤input_pool结果保存到care_list中
    --------------------------------
    create by wangtao   2017.08.04
"""
import sys
import os
import commands
import re

#reload(sys)
#sys.setdefaultencoding('utf-8')

def filter_words(input_list,keywords_list):
    care_list =[]
    for input_item in range (0, len(input_list)):
        for keywords in range (0, len(keywords_list)):
            m = re.search(keywords_list[keywords], input_list[input_item], re.IGNORECASE)
            if bool(m):
                care_list.append(input_list[input_item])

    return care_list