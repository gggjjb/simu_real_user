'''

@author: gjb
'''
print "adbddd"

def change_id(aIDFile,aContentFile,aKey,aFinalFile):
    id_dic=[]
    content_dic=[]
    res_final=''
    
    f=open(aContentFile)
    lines=f.readlines()
    for line in lines:
        content_tmp=line.strip()
        content_dic.append(content_tmp)
    f.close()
    
    f=open(aIDFile)
    lines=f.readlines()
    for line in lines:
        id_dic.append(line.strip())
    f.close()
    
    for i in range(0,len(content_dic)):
        for j in range(0,len(id_dic)):
            res_final+=(content_dic[i].replace(aKey,id_dic[j])+'\n')
    
    
    f=open(aFinalFile,'w')
    f.write(res_final)
    f.close()

change_id('id.txt','content.txt','XXXXX','res.txt')    
