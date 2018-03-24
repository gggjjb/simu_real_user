#coding=utf-8
'''
Created on 2018��3��23��

@author: gjb
'''
import os
from uiautomator import Device
import time
import random
from simu_common import *
import sys


def traversal_sharearticle(aDeviceId,aGroupName):
    #点击群组
    if aDeviceId(text=aGroupName).exists:
        aDeviceId(text=aGroupName).click()
    else:
        out_error("can not find group")
        return
    
    #阅读文章
    for j in range(0,5):
        #阅读当屏的4篇文章
        share_art_list=aDeviceId(className='android.widget.LinearLayout',resourceId='com.tencent.mm:id/ad9')
        share_art_num=share_art_list.count
        for i in range(0,share_art_num):
            share_art_list[i].click()#点击文章
            if aDeviceId(resourceId='com.tencent.mm:id/he',className='android.widget.ImageButton')\
                .wait.exists(timeout=COMMON_WAIT_TIME):
                out_log("article is opened")
                read_share_art(aDeviceId)
                #返回文章列表
                if aDeviceId(resourceId='com.tencent.mm:id/hx').wait.exists(timeout=COMMON_WAIT_TIME):
                    aDeviceId(resourceId='com.tencent.mm:id/hx').click()
                    time.sleep(3)
            else:
                out_error("open article fail")
                continue
        #在文章列表向上滑动
        if aDeviceId(className='android.widget.ListView',resourceId='com.tencent.mm:id/c5x').wait.exists(timeout=COMMON_WAIT_TIME):
            out_log("swipe down the article list")
            aDeviceId(className='android.widget.ListView',resourceId='com.tencent.mm:id/c5x')\
              .swipe.down(steps=80)

def read_share_art(aDeviceID):
    #停留在文章开始处几秒钟，模仿用户看文章
    time.sleep(READ_ARTICAL_BEGIN_WAIT_TIME)
    #随机滑动次数
    random_read_article_swipe_num=random.randint(7,15)
    for i in range(0,random_read_article_swipe_num):
        if aDeviceID(descriptionContains='展开全文').exists:
            out_log("find:expand all")
            aDeviceID(descriptionContains='展开全文').click()

        if aDeviceID(className='android.widget.FrameLayout',resourceId='android:id/content').wait.exists(timeout=COMMON_WAIT_TIME):
            aDeviceID(className='android.widget.FrameLayout',resourceId='android:id/content')\
              .swipe.up(steps=80)
        else:
            out_error("article body not found")
            return


    

def launch_app(aDeviceID):
    aDeviceID.screen.on()
    aDeviceID.wakeup()    
    #启动app
    execCmd(CMD_CLEAN_WEIXIN)
    time.sleep(1)
    execCmd(CMD_LAUNCH_WEIXIN)
    if aDeviceID(text='发现').wait.exists(timeout=COMMON_WAIT_TIME):
        out_log("Launch app finished")
    else:
        out_log("ERROR:Launch app fail")
    
    
d = Device('410bd4f4')

#launch_app(d)
traversal_sharearticle(d,'阳光100')
#read_share_art(d)
