#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015-homework/day2/stringtie/SRR072893/t_data.ctab"

#files are iterables - they can be used in a for loop
f = open( filename )

"""
line_count = 0
for data in f:
    if line_count <= 10:
        pass 
    elif line_count <=15:
        print data,
    else:
        break
    line_count += 1
    
    instead use enumerate:
"""
    
for line_count, data in enumerate( f ):
    if line_count <= 10:
        pass 
    elif line_count <=15:
        print data,
    else:
        break