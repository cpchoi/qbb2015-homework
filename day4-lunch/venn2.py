#!/usr/bin/env python

from __future__ import division

import chrombits

import sys
import numpy
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles


arr = chrombits.ChromosomeLocationBitArrays( fname=sys.argv[1] )


ctcf = arr.copy()
beaf = arr.copy()
suhw = arr.copy()


beaf.set_bits_from_file( sys.argv[2] )
ctcf.set_bits_from_file( sys.argv[3] )
suhw.set_bits_from_file( sys.argv[4] )

combination = ctcf.union( beaf.union( suhw ) )



first_array = beaf

second_array = ctcf

third_array = suhw



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

print "BEAF: %d. CTCF: %d, Su(HW): %d, BEAF and CTCF: %d, BEAF and suHW: %d, CTCF and suHW: %d, bind to all 3: %d, total: %d"% (A, B, C, AB, AC, BC, ABC, total)

plt.figure()
v = venn3(subsets = (A, B, AB, C, AC, BC, ABC), set_labels = ('BEAF','CTCF','suHW'))
plt.savefig("venndiagram2.png")
