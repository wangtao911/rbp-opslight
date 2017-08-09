#! /usr/bin/python
# coding: utf-8
"""
    通过GPIO开启LED等
    --------------------------------
    create by wangtao   2017.08.04
"""
import RPi.GPIO as GPIO
import time
def light_flash(time):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    #print "LED on"
    for n in range(0,time):
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.3)
        pass
    #print "LED off"