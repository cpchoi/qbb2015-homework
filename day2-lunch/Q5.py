#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015-homework/day2/mappedReads.SAM"

#files are iterables - they can be used in a for loop
f = open( filename )

chromosome_num ={"2L":0, "2R":0, "3L":0, "3R":0, "4":0, "X":0 }

for line in f:
    field = line.split()
    chromosome = field[2]
    if "@" in line:
       pass
    if chromosome in chromosome_num:
        chromosome_num[chromosome] += 1 #add 1 to the VALUE for the corresponding chromosome name KEY

            
print "Chromosome 2L", chromosome_num["2L"] 
print "Chromosome 2R", chromosome_num["2R"] 
print "Chromosome 3L", chromosome_num["3L"] 
print "Chromosome 3R", chromosome_num["3R"] 
print "Chromosome 4", chromosome_num["4"] 
print "Chromosome X", chromosome_num["X"] 


            

            