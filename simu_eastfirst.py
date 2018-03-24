#coding=utf-8
'''
Created on 2018年3月19日

@author: gjb
'''

import os
from uiautomator import Device
import time
import random
from simu_common import *




#切换频道
def simu_eastfirst_channel(aDeviceID):
    out_log("enter simu_eastfirst_channel")
    chanle_list=EASTFIRST_CHANNEL_NAME_LIST[random.randint(0,len(EASTFIRST_CHANNEL_NAME_LIST)-1)]
    out_log("channel count=%d"%len(chanle_list))
    for i in range(0,len(chanle_list)):
        go_eastfirst_apphome(aDeviceID)
        #进入频道编辑页
        if aDeviceID(resourceId='com.songheng.eastnews:id/age').wait.exists(timeout=COMMON_WAIT_TIME):
            out_log("find channel more button ,click it")
            aDeviceID(resourceId='com.songheng.eastnews:id/age').click()
        else:
            out_error("channel more button not found,continue")
            continue
        #点击频道并进入
        if aDeviceID(resourceId='com.songheng.eastnews:id/aem').wait.exists(timeout=COMMON_WAIT_TIME):#等待进入频道编辑
            aDeviceID(text=chanle_list[i]).click() 
            out_log("enter channel:%s"%chanle_list[i])
            channel_eastfirst_readartical(aDeviceID)   
        else:
            out_error("channel:%s not found"%chanle_list[i])
            continue
    out_log("exit simu_channel")         

#频道观看
def channel_eastfirst_readartical(aDeviceID):
    #点击随机数量文章
    random_read_article_maxnum=random.randint(1,3)
    out_log("need to read %d number of articles"%random_read_article_maxnum)
    for j in range (0,random_read_article_maxnum):
        #滑动随机几屏寻找文章
        for k in range(0,random.randint(1,2)):
            aDeviceID(scrollable=True).swipe.up(steps=80)
        
        #点击该页内随机第几篇文章并阅读
        random_read_articl_index=random.randint(0,3)
        out_log("read article index=%d"%random_read_articl_index)
        try:
            #检查是否是广告
            article_list=aDeviceID(resourceId='com.songheng.eastnews:id/kr',className='android.widget.ListView')
            article_selected=article_list.child_by_instance(random_read_articl_index)
            if article_selected.child(text='广告',className='android.widget.TextView').exists:
                out_error("the article is ad ,igonore it")
                continue
            else:
                out_log("the articel is not ad,read it")
                #aDeviceID(resourceId='com.songheng.eastnews:id/ou')[random_read_articl_index].wait.exists(timeout=5000):
                #aDeviceID(resourceId='com.songheng.eastnews:id/ou')[random_read_articl_index].click()
                article_selected.click()
                read_eastfirst_article(aDeviceID)
                out_log("finish read article")
                global SHARE_WEIXIN_COUNT
                if SHARE_WEIXIN_COUNT > 0:
                    share_weixin(aDeviceID)
                    SHARE_WEIXIN_COUNT=SHARE_WEIXIN_COUNT-1
                aDeviceID.press.back()            
        except:
            out_error("exception happend")
            continue
        else:
            out_log("exception not happened")    

#回到首页
def go_eastfirst_apphome(aDeviceID):    
    for i in range(0,3):
        aDeviceID.press.back()
        if aDeviceID(resourceId='com.songheng.eastnews:id/k0').wait.exists(timeout=COMMON_WAIT_TIME):
            aDeviceID(resourceId='com.songheng.eastnews:id/k0').click()
            break
    
#阅读文章
def read_eastfirst_article(aDeviceID):
    #停留在文章开始处几秒钟，模仿用户看文章
    time.sleep(READ_ARTICAL_BEGIN_WAIT_TIME)
    #随机滑动次数
    random_read_article_swipe_num=random.randint(7,15)
    for i in range(0,random_read_article_swipe_num):
        if aDeviceID(className='android.webkit.WebView').wait.exists(timeout=COMMON_WAIT_TIME):
            aDeviceID(className='android.webkit.WebView')\
              .swipe.up(steps=80)
        else:
            out_error("article body not found")
            return
        if aDeviceID(descriptionContains='展开全文').exists:
            out_log("find:expand all")
            aDeviceID(descriptionContains='展开全文').click()
            

def eastfirst_simu(aDeviceID):
#    aDeviceID.watcher("EastFirst_Push_News").when(text="头条新闻").when(text="查看") \
#                             .press.back()
                             
    launch_eastfirst_app(aDeviceID)
    action_list=EASTFIRST_ACTION_LIST[random.randint(0,1)]
    for i in range(0,len(action_list)):
        if action_list[i]=='channel':
            simu_eastfirst_channel(aDeviceID)
        else:
            out_error('invalid action:%s'%action_list[i])
    execCmd(CMD_CLEAN_EASTFIRST)

def share_weixin(aDeviceID,aGroupName='阳光100'):
    out_log("begin share to weixin")
    #点击页面上的分享按钮
    if aDeviceID(className='android.widget.ImageView',resourceId='com.songheng.eastnews:id/a9f').wait.exists(timeout=COMMON_WAIT_TIME):
        out_log("find share button,will share to weixin")
        aDeviceID(className='android.widget.ImageView',resourceId='com.songheng.eastnews:id/a9f').click()
    else:
        out_error("can not find share button,cancel")
        return
    #点击微信分享按钮
    if aDeviceID(className='android.widget.LinearLayout',resourceId='com.songheng.eastnews:id/ahj').wait.exists(timeout=30000):
        out_log("find weixin button,will share to weixin")
        aDeviceID(className='android.widget.LinearLayout',resourceId='com.songheng.eastnews:id/ahj').click()
    else:
        out_error("can not find share weixin button,cancel")
        return
    #点击群组
    if aDeviceID(text=aGroupName).wait.exists(timeout=COMMON_WAIT_TIME):
        out_log("find the weixin group %s"%aGroupName)
        aDeviceID(text=aGroupName).click()
    else:
        out_error("not found weixin group %s"%aGroupName)
        return
    
    #分享
    if aDeviceID(text='分享').wait.exists(timeout=COMMON_WAIT_TIME):
        out_log("share to weixin")
        aDeviceID(text='分享').click()
    else:
        out_error("share failed")
        return
    
    #返回东方头条
    if aDeviceID(text='返回东方头条').wait.exists(timeout=COMMON_WAIT_TIME):
        out_log("return to eastfirst")
        aDeviceID(text='返回东方头条').click()
    else:
        out_error("fail to return eastfirst")
        return
    
            
def launch_eastfirst_app(aDeviceID):
    aDeviceID.screen.on()
    aDeviceID.wakeup()    
    #启动app
    execCmd(CMD_CLEAN_EASTFIRST)
    time.sleep(1)
    execCmd(CMD_LAUNCH_EASTFIRST)
    if aDeviceID(resourceId='com.songheng.eastnews:id/aga').wait.exists(timeout=COMMON_WAIT_TIME):
        out_log("Launch eastfirst app finished")
    else:
        out_log("ERROR:Launch eastfirst app fail")


#d=Device('410bd4f4')
#eastfirst_simu(d)
#channel_eastfirst_readartical(d)
#dab= d(resourceId="com.songheng.eastnews:id/ou", instance=1)
#ddd=d(resourceId='com.songheng.eastnews:id/kr',className='android.widget.ListView')
#print ddd.info
#line_tmp=ddd.child_by_instance(0)
#if line_tmp.child(text='广告',className='android.widget.TextView').exists:
#    print "ad"
#    line_tmp.click()
#else:
#    print "not ad"


