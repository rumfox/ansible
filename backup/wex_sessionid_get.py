#!/usr/bin/python2.7

import datetime
import dateutil.relativedelta

today=datetime.date.today()
nowYYYYMM = datetime.date.today()
preYYYYMM = today + dateutil.relativedelta.relativedelta(months=-1)
preYYYY =  today+ dateutil.relativedelta.relativedelta(years=-1)
nowYYYY = nowYYYYMM.strftime('%Y')
preYYYY = preYYYY.strftime('%Y')
nowYYYYMM = nowYYYYMM.strftime('%Y%m')
preYYYYMM = preYYYYMM.strftime('%Y%m')
swcnt = 3

f = open('/home/esadmin/ansible_wex/wex_session.log')
w = open('/home/esadmin/ansible_wex/wex_session.dat', 'w')
p = open('/home/esadmin/ansible_wex/wex_session_pm.dat', 'w')
q = open('/home/esadmin/ansible_wex/wex_session_py.dat', 'w')

strCollectionID = ''
list_session=[]
strpassit_pm = ''
strfacebookreply_py = ''
list_session_main2_pm=[]
list_session_fbrep_py=[]

while True:
    line = f.readline()
    if not line: break

    if line.find('Session Id:') != -1 : 
        strtest = line.split(':')[1].split('.')
        if len(strtest) < 3 : 
           strSessionID = line.split(':')[1].split('.')
           strSessionID = ".".join(strSessionID[0:2]).strip()
    elif line.find('Display name:') != -1 : 
        strDisplayName = line.split(':')[1].split('.')[0].strip() 
    elif line.find('Collection Id:') != -1 :
        strCollectionID = line.split(':')[1].split('.')[0].strip() 

    swcnt = swcnt + 1

    if swcnt == 21 :
        if len(strtest) < 3 : 
            if strCollectionID == "Main2" and strDisplayName == nowYYYYMM and len(strSessionID) > 0 :
                list_session.insert(0, strSessionID)
            elif strCollectionID == "FACEBOOK" and len(strSessionID) > 0 :
                list_session.insert(2, strSessionID)        
            elif strCollectionID == "FACEBOOK-REPLY" and strDisplayName == nowYYYY and len(strSessionID) > 0 :
                list_session.insert(1, strSessionID)        
            elif strCollectionID == "Report" and len(strSessionID) > 0 :
                list_session.insert(3, strSessionID)
            elif strCollectionID == "Main2" and strDisplayName == preYYYYMM and len(strSessionID) > 0 :
                list_session_main2_pm.insert(0, strSessionID)
            elif strCollectionID == "FACEBOOK-REPLY" and strDisplayName == preYYYY and len(strSessionID) > 0 :
                list_session_fbrep_py.insert(0, strSessionID)     
        swcnt = 3 
        strSessionID = ''
        strCollectionID = ''

for item in list_session:
    w.write(item+'\n')  

for item in list_session_main2_pm:
    p.write(item+'\n')  

for item in list_session_fbrep_py:
    q.write(item+'\n')  

f.close()
w.close()
p.close()
q.close()


