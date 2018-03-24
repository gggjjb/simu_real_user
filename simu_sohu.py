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
import sys

#d = Device('410bd4f4')
#d=Device()

    

#签到和领红包
def simu_sohu_signandrebbag(aDeviceID):
    out_log("enter simu_signandrebbag")
    go_apphome(aDeviceID)
    if aDeviceID(text='我的',resourceId='com.sohu.infonews:id/item_title').wait.exists(timeout=COMMON_WAIT_TIME):
        aDeviceID(text='我的',resourceId='com.sohu.infonews:id/item_title').click()
    else:
        out_error("can not find mine tab,return")
        return
    if aDeviceID(text='签到',resourceId='com.sohu.infonews:id/task_button').wait.exists(timeout=COMMON_WAIT_TIME):
        aDeviceID(text='签到',resourceId='com.sohu.infonews:id/task_button').click()
    if aDeviceID(text='立即抢',resourceId='com.sohu.infonews:id/task_button').exists:
        aDeviceID(text='立即抢',resourceId='com.sohu.infonews:id/task_button').click()
        #点击开红包按钮
        if aDeviceID(resourceId='com.sohu.infonews:id/redbag_open').wait.exists(timeout=COMMON_WAIT_TIME):
            aDeviceID(resourceId='com.sohu.infonews:id/redbag_open').click()
            aDeviceID.press.back()
    out_log("exit simu_signandrebbag")
   

#切换频道
def simu_sohu_channel(aDeviceID):
    out_log("enter simu_channel")
    chanle_list=SOHU_CHANNEL_NAME_LIST[random.randint(0,len(SOHU_CHANNEL_NAME_LIST)-1)]
    out_log("Will enter follwing channel "+chanle_list)
    for i in range(0,len(chanle_list)):
        go_apphome(aDeviceID)
        #进入频道编辑页
        if aDeviceID(resourceId='com.sohu.infonews:id/channel_more').wait.exists(timeout=COMMON_WAIT_TIME):
            aDeviceID(resourceId='com.sohu.infonews:id/channel_more').click()
        else:
            out_error("channel more button not found,continue")
            continue
        #点击频道并进入
        if aDeviceID(text='我的频道').wait.exists(timeout=COMMON_WAIT_TIME):
            aDeviceID(text=chanle_list[i]).click() 
            out_log("enter channel:%s"%chanle_list[i])
            channel_readartical(aDeviceID)    
        else:
            out_error("channel:%s not found"%chanle_list[i])
            continue
    out_log("exit simu_channel")         

#频道观看
def channel_readartical(aDeviceID):
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
            if aDeviceID(resourceId='com.sohu.infonews:id/article_title')[random_read_articl_index].wait.exists(timeout=COMMON_WAIT_TIME):
                aDeviceID(resourceId='com.sohu.infonews:id/article_title')[random_read_articl_index].click()
                read_article(aDeviceID)
                aDeviceID.press.back()                
            else:
                out_error("article not found")
                continue
        except:
            out_error("click article title exception")
            continue
        else:
            out_log("not exception")    

#点击热门搜索文章        
def simu_sohu_search(aDeviceID):
    out_log("enter simu_search")
    go_apphome(aDeviceID)
    #进入搜索页
    if aDeviceID(resourceId='com.sohu.infonews:id/search_bg').wait.exists(timeout=COMMON_WAIT_TIME):
        aDeviceID(resourceId='com.sohu.infonews:id/search_bg').click()
    else:
        out_error("can not find search button")
        return
    
    #点击随机数量热搜词、阅读随机频道、随机数量文章
    random_search_num=random.randint(1,3)
    out_log("search num = %d"%random_search_num)
    for i in range(0,random_search_num):
        #点击随机热搜词
        random_hotwords_index=random.randint(0,9)
        out_log("click the  %d hot words"%random_hotwords_index)
        hotsearch_obj=aDeviceID(resourceId='com.sohu.infonews:id/recyclerview_hot_words',className='android.support.v7.widget.RecyclerView')\
         .child(resourceId='com.sohu.infonews:id/item_search_text',className='android.widget.TextView',instance=random_hotwords_index)
        if hotsearch_obj.wait.exists(timeout=COMMON_WAIT_TIME):
            out_log("find hot word and begin click")
            hotsearch_obj.click()
        else:
            out_error("can not find hot word")
            continue
        
        #点击随机数量文章
        random_search_hotkey_article_num=random.randint(1,4)
        out_log("need to read %d article"%random_search_hotkey_article_num)
        for j in range (0,random_search_hotkey_article_num):
            #滑动随机几屏寻找文章
            for k in range(0,random.randint(1,2)):
                aDeviceID(scrollable=True).swipe.up(steps=80)
            
            #点击随机文章并阅读
            random_search_read_articl_index=random.randint(0,4)
            out_log("read %d article"%random_search_read_articl_index)
            if aDeviceID(resourceId='com.sohu.infonews:id/article_img',instance=random_search_read_articl_index).wait.exists(timeout=COMMON_WAIT_TIME):
                aDeviceID(resourceId='com.sohu.infonews:id/article_img',instance=random_search_read_articl_index).click()
                read_article(aDeviceID)
                aDeviceID.press.back()                
            else:
                out_error("article not found")
                continue
        #返回热词陈列页面
        search_clear_btn=aDeviceID(resourceId='com.sohu.infonews:id/search_clear',className='android.widget.ImageView')
        if (search_clear_btn.wait.exists(timeout=COMMON_WAIT_TIME)):
            search_clear_btn.click()
        
    out_log("exit simu_search")

#回到首页
def go_apphome(aDeviceID):    
    for i in range(0,3):
        aDeviceID.press.back()
        if aDeviceID(text='首页',resourceId='com.sohu.infonews:id/item_title').wait.exists(timeout=COMMON_WAIT_TIME):
            aDeviceID(text='首页',resourceId='com.sohu.infonews:id/item_title').click()
            break
    
#启动app
def launch_app(aDeviceID):
    aDeviceID.screen.on()
    aDeviceID.wakeup()    
    #启动app
    execCmd(CMD_CLEAN_SOHU)
    time.sleep(1)
    execCmd(CMD_LAUNCH_SOHU)
    if aDeviceID(className='android.widget.ImageView',resourceId='com.sohu.infonews:id/article_img').wait.exists(timeout=COMMON_WAIT_TIME):
        out_log("Launch app finished")
    else:
        out_log("ERROR:Launch app fail")
   

#阅读文章
def read_article(aDeviceID):
    time.sleep(READ_ARTICAL_BEGIN_WAIT_TIME)
    for i in range(0,READ_ARTICAL_MAXSWIPE):
        if aDeviceID(resourceId='com.sohu.infonews:id/body_bar',className='android.widget.ScrollView').wait.exists(timeout=COMMON_WAIT_TIME):
            aDeviceID(resourceId='com.sohu.infonews:id/body_bar',className='android.widget.ScrollView')\
              .swipe.up(steps=80)
        else:
            out_error("article body not found")
            return
        if aDeviceID(text='热门评论',resourceId='com.sohu.infonews:id/hot_comment_tip').exists:
            out_log("reach the article bottom,finish reading") 
            break

def sohu_simu(aDeviceID):
    launch_app(aDeviceID)
    if aDeviceID(className='android.widget.ImageView',resourceId='com.sohu.infonews:id/article_img').wait.exists(timeout=COMMON_WAIT_TIME):
        out_log("Launch sohu app finished")
    else:
        out_log("ERROR:Launch sohu app fail")

    action_list=SOHU_ACTION_LIST[random.randint(0,5)]
    for i in range(0,len(action_list)):
        if action_list[i]=='search':
            simu_sohu_search(aDeviceID)
        elif action_list[i]=='redbag':
            simu_sohu_signandrebbag(aDeviceID)           
        elif action_list[i]=='channel':
            simu_sohu_channel(aDeviceID)
        else:
            out_error('invalid action:%s'%action_list[i])
    execCmd(CMD_CLEAN_SOHU)
    

#simu_sohu_channel(d)
#simu_sohu_search(d)    
#d.press.back()
        
#sohu_simu()        
#launch_app()        
#search_act()
#get_signandrebbag()
#switch_channel()

#d(scrollable=True).swipe.up(steps=80)
#d(scrollable=True).scroll(steps=10)
#d(scrollable=True).scroll.vert.backward()
#read_article()
#go_apphome()
#search_act()

#run_test()
#switch_channel()

#位置上滑，向着顶部方向
#d(resourceId='com.sohu.infonews:id/body_bar',className='android.widget.ScrollView').swipe.down(steps=80)

#从文章开始位置上滑，向着底部方向
#d(resourceId='com.sohu.infonews:id/body_bar',className='android.widget.ScrollView').swipe.up(steps=80)


#到娱乐频道刷新一次
#d(scrollable=True).fling.vert.toBeginning(max_swipes=1)

#检查手机是否存在




