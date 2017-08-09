#! /usr/bin/python
# coding: utf-8
"""
    读取Email的脚本
    在邮箱中建立两个文件夹
    L1ALART用于接收报警邮件
    L1ALART-readed用于存放已经读取的报警邮件（不知道怎么用python把邮件设置为“已读”）
    --------------------------------
    create by wangtao   2017.08.04
"""
import sys
import os
import commands

#reload(sys)
#sys.setdefaultencoding('utf-8')
from exchangelib import DELEGATE, Account, Credentials

def mail_exchange():
    credentials = Credentials(
        username='letv\\wangtao12',
        password='Yuelaiyu3ha0!'
    )
    account = Account(
        primary_smtp_address='wangtao12@le.com',
        credentials=credentials,
        autodiscover=True,
        access_type=DELEGATE
    )
    
    alart_folder = account.root.get_folder_by_name('L1ALART')
    alart_folder_readed = account.root.get_folder_by_name('L1ALART-readed')
    alart_folder.refresh()
    input_pool = []
    unread_counter = 0
    unread_counter = alart_folder.unread_count
    if unread_counter > 0:
        for item in alart_folder.all().order_by('-datetime_received')[:unread_counter]:
            #print(item.subject)
            input_pool.append(item.subject)
            item.move(alart_folder_readed)
    #for n in input_pool:
    #    print n
    #input_pool = ['a','b']
    #print "unread_counter"
    #print unread_counter
    return input_pool

