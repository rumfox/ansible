#!/usr/bin/python2.7

import re

f = open('/home/esadmin/ansible_wex/wex_idxstatus.log')
w = open('/home/esadmin/ansible_wex/wex_idxstatus.dat','w+')
p = re.compile('(?<=The following result occurred: {\"indexStatisticsAll\":{},\"indexBuildStatusDetail\":{\"status\":\")(.*)(?=\",\"numberOfDocumentUpserted)')

while True:
    line = f.readline()
    m = p.search(line)
    if m:
        print m.group()
        w.write(m.group())
    if not line: break

f.close()
w.close()


