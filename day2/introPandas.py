#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table( annotation, comment='#', header=None )

#print df
#print df.head()

#print df.describe()
#print df.info()
#print "\nthis is what happens to [1:5]\n"
#print df[1:5]
#use , end number is not inclusive
#print "\nthis is what happens to [0:5]\n"

#print df[0:5]

#i want 20 through 25 in 1 base
#print df [19:25]


df.columns = ["chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes"]

#print df.info()

#print df.sort("type", ascending=False)
# or -> two ways because first you can indicate what column, and have pandas figure out how to sort. Or you can assign stuff, then let it sort
#print df.sort(ascending=False, columns ="type")


#row based column based data - using df -> d for rows,f for columns

#print df["chromosome"]

#print df[["chromosome", "start", "end"]] # need to put another bracket - so that it knows its a list

#print df["start"][9:15]
#both are alright
#print df[9:15]["start"]

#print df.shape #this prints (number of rows, number of columns)
#df2 = df[["start", "end"]]
#print df2.shape # this prints the new shape, notice its now (number of rows, 2 columns)

#df2.to_csv("startColmn.txt", sep='\t', index=False) #this removes the lsit of of numbers next to the row
print df.shape
roi = df["start"] < 10 # 1 is less than ten, 2 is less than ten....etc -> regions of interest = roi

#print roi
#print type(roi) # type is a good way to figure out what type of object it is
print roi.shape
print df[roi].shape #~ is the not 


