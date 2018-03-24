#coding=utf-8
'''
Created on 2018��3��24��

@author: gjb
'''
from simu_common import * 
from test.simu_common import out_log

def eastfirst_pushNews_watcher(aDeviceID):
    if aDeviceID(text='取消',resourceId='com.songheng.eastnews:id/ut',className='android.widget.Button').exists:
        out_log("EastFirst Push news,click the cancel button")
        aDeviceID(text='取消',resourceId='com.songheng.eastnews:id/ut',className='android.widget.Button').click()
    return True  



