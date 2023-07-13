#!/usr/bin/python2.7

import re

f = open('/home/esadmin/ansible_wex/wex_parsrch.log')
w = open('/home/esadmin/ansible_wex/wex_parsrch.dat','w+')
p = re.compile('(?<=<Status>)(.*)(?=</Status>)')

while True:
    line = f.readline()
    m = p.search(line)
    if m:
        #print 'Match found: ', m.group()
        w.write(m.group())  
    if not line: break
        
f.close()
w.close()

