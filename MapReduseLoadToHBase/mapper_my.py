#!/usr/bin/python
 
import sys 
import re
import happybase
 
err=0
errF=0
corF=0
corR=0

connection = happybase.Connection('node2.newprolab.com')
table = connection.table('roman.smirnov')

for line in sys.stdin: 
    try:
        uid,ts,url = line.strip().split("\t")
        if (re.match('[0-9]+', uid) != None and
		re.match('[0-9]{10,10}.[0-9]+', ts) != None and
			re.match('http', url)!= None):

	     corF=corF+1
#            print(uid + "\t" + ts + "\t" + url)
	     if (int(uid)%256==170):
    	         print str(uid)+' '+str(int(uid)%256)
                 try:
		     table.put(uid, {'data:url': url}, timestamp=int(float(ts)*1000))
		     corR=corR+1
        	 except:
            	     print('Error')
        else:
            errF=errF+1
#            print(uid + "\t" + ts + "\t" + url) + ' error form'
 
    except:
	err=err+1
#        print line + 'error value'

print 'Num Corect Rows: ' + str(corR)
print 'Num CorectForm: ' + str(corF)
print 'Num ErrorValues: ' + str(err)
print 'Num ErrorFormat: ' + str(errF)

