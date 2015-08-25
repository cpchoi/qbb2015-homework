#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015-homework/day2/mappedReads.SAM"

f = open( filename )


line_count = 0
for data in f:
    if "NM:i:0" in data:
        line_count+=1  
print line_count,