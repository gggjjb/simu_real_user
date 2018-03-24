#coding=utf-8
'''
Created on 2018��3��20��

@author: gjb
'''
import os
from uiautomator import Device
import time
import random

READ_ARTICAL_MAXSWIPE=15
READ_ARTICAL_BEGIN_WAIT_TIME=3
READ_ARTICAL_STEPS_WAIT_TIME=3

COMMON_WAIT_TIME=20000

CMD_LAUNCH_SOHU='adb shell am start -n com.sohu.infonews/com.sohu.quicknews.splashModel.activity.SplashActivity'
CMD_CLEAN_SOHU='adb shell am force-stop com.sohu.infonews'
SOHU_CHANNEL_NAME_LIST=[['要闻','健身','军事','国际','体育'],['娱乐','养生','美食','科技','汽车','时尚']\
                       ,['财经','文玩','美食','足球','数码','运势','文化'],['旅游','情感','动漫','篮球']\
                       ,['手机','育儿','娱乐','财经'],['财经','数码'],['国际','科技','要闻']]
SOHU_ACTION_LIST=[['search','redbag','channel'],['redbag','search','channel'],
                  ['channel','redbag','search'],['search','channel','redbag'],
                  ['channel','search','redbag'],['redbag','channel','search'],
                  ['channel'],['search'],['redbag'],['redbag']]

CMD_LAUNCH_EASTFIRST='adb shell am start -n com.songheng.eastnews/com.oa.eastfirst.activity.WelcomeActivity'
CMD_CLEAN_EASTFIRST='adb shell am force-stop com.songheng.eastnews'

EASTFIRST_ACTION_LIST=[['channel'],['channel']]
EASTFIRST_CHANNEL_NAME_LIST=[['娱乐','社会','健康','体育'],['财经','科技','军事','国际','幽默','星座']\
                       ,['汽车','NBA','时尚','游戏','段子','科学','互联网'],['数码','健身','饮食','减肥']\
                       ,['外汇','不动产','理财','基金'],['期货','保险'],['外汇','星座','家居']]


APP_RUN_ORDER=[['sohu','eastfirst'],['eastfirst','sohu'],['sohu','eastfirst'],['sohu','eastfirst']]

CMD_LAUNCH_WEIXIN='adb shell am start -n com.tencent.mm/com.tencent.mm.ui.LauncherUI'
CMD_CLEAN_WEIXIN='adb shell am force-stop com.tencent.mm'

WEIXIN_GROUPS=['阳光100']
SHARE_WEIXIN_COUNT=1

def out_log(aLogStr):
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+':'+aLogStr

def out_error(aLogStr):
    print time.strftime('%Y-%m-%d %H:%M:%S ERROR:',time.localtime(time.time()))+':'+aLogStr


def execCmd(cmd):  
    out_log( cmd)
    r = os.popen(cmd) 
    text = r.read()
    #print text  
    time.sleep(2)
    r.close()  
    return text  

def execCmd_NotBlock(cmd):
    out_log( cmd)
    os.popen(cmd)  

def clean_apps(aDeviceID):
    execCmd('adb shell input keyevent --longpress 3')
    del_btn=aDeviceID(resourceId='com.android.systemui:id/recents_delete')
    if del_btn.wait.exists(timeout=3000):
        del_btn.click()
    time.sleep(2)
    aDeviceID.press.home()

