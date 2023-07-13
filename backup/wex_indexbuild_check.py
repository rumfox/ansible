#!/usr/bin/python2.7

import re

f = open('/home/esadmin/ansible_wex/wex_idxcheck.log')
w = open('/home/esadmin/ansible_wex/wex_idxcheck.dat','w+')

p = re.compile('(?<=<Status>)(.*)(?=<\/Status>)')
q = re.compile('(?<=NumberOfInsertedRecords>)(.*)(?=<\/NumberOfInsertedRecords)')
r = re.compile('(?<=NumberOfUpdatedRecords>)(.*)(?=<\/NumberOfUpdatedRecords)')
chkstr = ''
chkval = 0

while True:
    line = f.readline()
    m = p.search(line)
    n = q.search(line)
    o = r.search(line)

    if m :
        chkstr = chkstr + m.group()
    elif n :
        chkval = chkval + int(n.group())
    elif o :
        chkval = chkval + int(o.group())
        
    if not line: break
        
if chkstr == '2' and chkval > 0 :
   w.write('EXIST')
elif chkstr == '1' :
   w.write('READY')
elif chkstr == '2' and chkval == 0 :
   w.write('PASS')
else :
   w.write('PASS')
    
f.close()
w.close()
