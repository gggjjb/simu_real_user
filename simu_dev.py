#coding=utf-8
'''
Created on 2018��3��20��

@author: gjb
'''
import getopt
import sys
from simu_sohu import sohu_simu
from uiautomator import Device
from simu_common import *
from simu_eastfirst import eastfirst_simu
from simu_watcher import *



if __name__=='__main__':
    device_id=''
    opts, args = getopt.getopt(sys.argv[1:], "i:n:")
    for op, value in opts:
        if op=="-i":
            device_id=value 
    
    #检查参数
    if device_id=='' :
        print "argument is empty.device_id=%s"%(device_id)
        device_id='410bd4f4'
        #sys.exit(1)    
    adb_devices_res=execCmd('adb devices')
    if adb_devices_res.find('410bd4f4')!=-1:
        out_log("find device,begin running")
    else:
        out_error("Device is not found.Exit")
        sys.exit(1)
    
    
    
    d = Device(device_id)
    d.handlers.on(eastfirst_pushNews_watcher(d))
    clean_apps(d)
    app_list=APP_RUN_ORDER[random.randint(0,len(APP_RUN_ORDER)-1)]
    for i in range(0,len(app_list)):
        if app_list[i]=='sohu':
            sohu_simu(d)
        elif app_list[i]=='eastfirst':
            eastfirst_simu(d)
        else:
            out_error("app name is invalid:%s"%app_list[i])
            continue    
    execCmd('adb reboot')
    
    