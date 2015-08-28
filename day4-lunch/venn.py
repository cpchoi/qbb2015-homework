#!/usr/bin/env python

# sys 1 len file
# sys 2 first region file BEAF
# sys 3 second region file CP190
# sys 4 third region file suHW
# sys 5 this is the number i type into terminal
"""
Very useful to put this in the begining to document what is happening
Count intersection of two BED files
"""
from __future__ import division
from matplotlib_venn import venn3, venn3_circles
import matplotlib.pyplot as plt
import numpy
import sys
import copy


def arrays_from_len_file( fname ):
    arrays = {}
    for line in open( fname ):
        fields = line.split()
        name = fields[0] # this is reading the first field in each line remember 1st field is 0 in python.
        size = int( fields[1] ) #this is the second field, but we want to convert the string field into an integer
        arrays[ name ] = numpy.zeros( size, dtype=bool ) # numpy.zeros(x,y), x is the number of items in array, and y is the type of items in the dictionary (your constraining), numpy.zeros is just making all the items default to 0. arrays[names] THisi s just defining our new dictionary with the KEY name.
            # we have a chromosome I  constrained position from 5 to 8 I want to mark that .And i want to mark that region
    return arrays

def set_bits_from_file( arrays, fname ):
    for line in open( fname ):
        fields = line.split()
            # parse ifelds
        chrom = fields [0]
        start = int( fields[1] )
        end = int( fields[2] )
        arrays[ chrom ][ start : end ] = 1 #so this is saying that replace this SPECIFIC KEY (which is chromosome), then from item start to item end to 1.

filled_array = arrays_from_len_file( sys.argv[1] ) # this has the name, but this is not referreing to the array in the for loop. You could name it completely different

first_array = copy.deepcopy(filled_array)
set_bits_from_file( first_array, sys.argv[2] )

second_array = copy.deepcopy(filled_array)
set_bits_from_file( second_array, sys.argv[3] )

third_array = copy.deepcopy(filled_array)
set_bits_from_file( third_array, sys.argv[4] )



#for key, value in arrays.iteritems():
    #print key, type( value ), value.shape, numpy.sum( value )
    
    # this creates list containing arrays. Each array has 0s, the number of 0s equal to the number of nucleotide the cromosome which is found from the length of the chromosome. 
        


A=0
B=0
C=0
AB=0
BC=0
AC=0
ABC=0
total = 0

for line in open ( sys.argv[2] ):
        fields = line.split()
        # parse ifelds
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] ) # for slice
        slA = first_array[chrom][start:end]
        sl1 = second_array[chrom][start:end]
        sl2 = third_array[chrom][start:end]

        total += 1
        
        
        
        if sl1.any()==False and sl2.any()==False and slA.any()==True:
            A += 1
            
        if sl1.any()==True and sl2.any()==False and slA.any()==True:
            AB += 1
            
        if sl1.any()==False and sl2.any()==True and slA.any()==True:
            AC += 1
            
        if sl1.any()==True and sl2.any()==True and slA.any()==True:
            ABC+= 1
            
for line in open ( sys.argv[3] ):
        fields = line.split()
        # parse ifelds
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] ) # for slice
        sl3 = first_array[chrom][start:end]
        slB = second_array[chrom][start:end]
        sl4 = third_array[chrom][start:end]
        total += 1
        
        if sl3.any()==False and sl4.any()==False and slB.any()==True:
            B += 1
            
        if sl3.any()==False and sl4.any()==True and slB.any()==True:
            BC += 1
            
        
            
for line in open ( sys.argv[4] ):
        fields = line.split()
        # parse ifelds
        chrom = fields[0]
        start = int( fields[1] )
        end = int( fields[2] ) # for slice
        slC = third_array[chrom][start:end]
        sl5 = first_array[chrom][start:end]
        sl6 = second_array[chrom][start:end]
        total += 1
        
        if sl5.any()==False and sl6.any()==False and slC.any()==True:
            C += 1

   
              
        #any_overlap += sl.any()# just looks at all positions in the slice if all are false, it returns false aka 0. if any are true it will come out true. sl.any() will print out a 1 or 0
        #all_overlap += sl.all()
        
    #for Array in [first_array, second_array, third_array]:
    #for line in Array:
        #total += 1
        #sl1 = first_array[chrom1][start1:end1].any & second_array[chrom1][start1:end1].any & [chrom1][start1:end1].any
        #sl2 = first_array[chrom2][start2:end2].any & second_array[chrom2][start2:end2].any & [chrom2][start2:end2].any
        #binds_3 += sl1
        #none_overlap += not sl.any()
        #percent = float(sys.argv[5])
        #half_overlap += ( numpy.sum(sl) / len(sl) > (percent/100) )

print "BEAF: %d. CP190: %d, suHW: %d, BEAF and CP190: %d, BEAF and suHW: %d, CP190 and suHW: %d, bind to all 3: %d, total: %d"% (A, B, C, AB, AC, BC, ABC, total)

plt.figure()
v = venn3(subsets = (A, B, AB, C, AC, BC, ABC), set_labels = ('BEAF','CP190','suHW'))
plt.savefig("venndiagram.png")


#grep "^chr2R" DM3_Kc_DNase.bed | ./intersect.py dm3.len DM3_phastCons.bed /dev/stdin
# you feed pre select one  chr2R into a program ->this is done in terminal