#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015-homework/day2/mappedReads.SAM"

#files are iterables - they can be used in a for loop
f = open( filename )

total = 0
count = 0
for line in f:
    if "SRR072893" in line:
        field = line.split()
        if "255" not in field[4]:
            MAPQ = float(field[4])
            total += MAPQ
            count += 1
            
        

real_count= int(count)
print "average MAPQ score:"
print float(total/count)