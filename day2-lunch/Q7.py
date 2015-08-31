#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015-homework/day2/mappedReads.SAM"

#files are iterables - they can be used in a for loop
f = open( filename )

count = 0
for line in f:
    field = line.split()
    if "@" == line[0]:    # Skips the header lines
        pass
    if field[2] == "2L" and 10000 <= int(field[3]) <= 20000:
            count += 1

print count            
        