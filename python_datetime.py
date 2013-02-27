# -*- coding: utf-8 -*-

__author = [
    '"YangFei" <yangf_sky@163.com>'
]

import time
import datetime
import calendar

def getCurrentTimeZone():
    return time.timezone/3600

def getUTCTime():
    return datetime.datetime.utcnow().strftime('%Y-%m-%d %X')
    
def calculateTime(originalTime,seconds):
    return time.strftime('%Y-%m-%d %X', time.localtime(time.mktime(time.strptime(str(originalTime),'%Y-%m-%d %X'))+int(seconds)))
    
def getWeekday():
    return time.strftime('%w')
    
def getLastDayofMonth(year,month):
    return calendar.monthrange(int(year), int(month))[1]
