#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015-homework/day2/stringtie/SRR072893/t_data.ctab"

#files are iterables - they can be used in a for loop
f = open( filename )

for data in f:
    fields = data.split() # makes a list by splitting all the white space in each string (line
    if "tRNA" in fields[9]: #column 10 - but python starts at 0. Count 10 columns in each string.
        print data, #the comma, prevents printing a brand new line. also data is just a variable - it can be anything you want.
    