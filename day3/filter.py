#!/usr/bin/env python

#filename = "/Users/cmdb/qbb2015-homework/day2/stringtie/SRR072893/t_data.ctab"

#files are iterables - they can be used in a for loop


import sys

#print sys.argv
#filename = sys.argv[1] #brings the path of hte file from the command line in terminal to process into your python program -> the 1 refers to the path 


f = sys.stdin # stdin and stdout - file handle objects. stdin - is already an open readable file handle from an upstream pipeline


# to use this in terminal - first cat file name | grep "CG" | ./filter.py | head 
# < is not so dangerous ./filter.py < /Users/cmdb/qbb2015-homework/day2/stringtie/SRR072893/t_data.ctab | head
# these two up above can do the same thing
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
    
name_counts ={} # make an empty dictionary

for line_count, data in enumerate( f ):
    fields = data.split()
    gene_name = fields[9]
    
    if gene_name not in name_counts:
        name_counts[ gene_name ] = 1 # name_counts{...  [gene_name]:1 ...}
    else:
        name_counts[ gene_name ] += 1
        
# iterate key, value pairs from the name counts dictionary
for key, value in name_counts.iteritems(): 
    #print gene name and count of isoforms of transcript
    print key, value
    
    