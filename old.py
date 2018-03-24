#coding=utf-8
'''
Created on 2018��3��20��

@author: gjb
'''
    #点击第一篇文章并阅读
    if aDeviceID(resourceId='com.sohu.infonews:id/article_img').wait.exists(timeout=5000):
        aDeviceID(resourceId='com.sohu.infonews:id/article_img').click()
        read_article(aDeviceID)
    else:
        out_error("channel first article not found")
        return
    #点击第二篇文章
    aDeviceID.press.back()
    aDeviceID(scrollable=True).swipe.up(steps=80)
    if aDeviceID(resourceId='com.sohu.infonews:id/article_img').wait.exists(timeout=3000):
        aDeviceID(resourceId='com.sohu.infonews:id/article_img').click()
        read_article(aDeviceID)
    else:
        out_error("channel second article not found")
        return


    if aDeviceID(resourceId='com.sohu.infonews:id/item_search_text').wait.exists(timeout=3000):
        aDeviceID(resourceId='com.sohu.infonews:id/item_search_text').click()
    else:
        out_error("can not find search hot word")
        return        


def te():
    if d(resourceId='com.sohu.infonews:id/body_bar',className='android.widget.ScrollView').wait.exists(timeout=READ_ARTICAL_STEPS_WAIT_TIME):
        d(resourceId='com.sohu.infonews:id/body_bar',className='android.widget.ScrollView')\
          .swipe.up(steps=80)
    else:
        out_error("article body not found")
        return
def test_so():
    re_num=random.randint(5,9)
    re_num=1
    out_log('auto num is %d'%re_num)
    #切换到要闻
    if d(text='要闻', className='android.widget.TextView').wait.exists(timeout=3000):
        d(text='要闻', className='android.widget.TextView').click()
        
        for i in range(0,re_num):
            #找到文章
            if d(className='android.widget.ImageView',resourceId='com.sohu.infonews:id/article_img').wait.exists(timeout=3000):
                d(className='android.widget.ImageView',resourceId='com.sohu.infonews:id/article_img').click()
            time.sleep(2)
            #滑到文章最低部
            if d(className='android.widget.ImageView',resourceId='com.sohu.infonews:id/comment_icon').wait.exists(timeout=3000):
                d(scrollable=True).scroll.toEnd(steps=200, max_swipes=1000)
            time.sleep(1)
            #返回要闻频道
            d.press.back()
            #if d(text='要闻', className='android.widget.TextView').wait.exists(timeout=5000):
            #    d(scrollable=True).fling.vert.toBeginning()
