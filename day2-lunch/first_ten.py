#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015-homework/day2/mappedReads.SAM"

#files are iterables - they can be used in a for loop
f = open( filename )


for line in f:
    if "SRR072893" in line:
        field = line.split()
        if "*" not in field[2]:
            chromosome = field[2]
            print chromosome
            
        