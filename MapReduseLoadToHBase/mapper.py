#!/usr/bin/env python

import sys
import happybase

connection = happybase.Connection('node2.newprolab.com')
#connection.create_table('roman.smirnov', {'data': dict(max_versions = 4096)})
table = connection.table('roman.smirnov')

for l in sys.stdin:
	try:
	   uid, ts, url = l.strip().split('\t')
	except ValueError:
 		#logging.warn("Could not split line: %s", line)
 		continue
	if not uid.isdigit() or int(uid) % 256 <> 170:
		continue
	if ts == '-' or ts is None:
		continue
	if url == '-' or url is None:
		continue
	table.put(uid, {'data:url': url}, int(float(ts)*1000))