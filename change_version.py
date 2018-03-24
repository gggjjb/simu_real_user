#coding=utf-8
'''
Created on 2018年3月16日

@author: gjb
'''
import re
import getopt
import sys


def change_ver(aFile,aNewVC,aNewVN):
    f=open(aFile)
    lines=f.readlines()
    f.close()
    change_num=0
    
    for i in range(len(lines)):
        line_tmp=lines[i].strip()
        search_vc=re.match('versionCode', line_tmp)
        search_vn=re.match('versionName', line_tmp) 
        
        if search_vc:
            lines[i]='        versionCode  %s \n'%aNewVC
            change_num+=1
        elif search_vn:
            lines[i]='        versionName '+'"'+aNewVN+'"'+'   \n'
            change_num+=1
        
        if change_num>=2:
            break
    
    f=open(aFile,'w')
    f.writelines(lines)
    f.close()

if __name__=='__main__':
    vc=''
    vn=''
    opts, args = getopt.getopt(sys.argv[1:], "c:n:")
    for op, value in opts:
        if op=="-c":
            vc=value 
        if op=="-n":
            vn=value
    
    #检查参数
    print vc,vn
    if vc=='' or vn=='':
        print "argument is empty.vc=%s,vn=%s"%(vc,vn)
        sys.exit(1)
    if not re.match('^[1-9]+\d*$', vc):
        print "versioncode invalid %s"%vc
        sys.exit(1)
    if not re.match('^(\d+\.){3}\d+$', vn):
        print "versionname invalid %s"%vn
        sys.exit(1)
    change_ver('build.gradle','27','1.2.3.27')
    
    
