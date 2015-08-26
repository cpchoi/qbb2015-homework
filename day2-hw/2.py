#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table( annotation, comment = '#', header = None )

df.columns = [ "chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes" ]


#roi = df["attributes"].str.contains( "Sxl" )
#other_roi = df["type"].str.contains( "transcript" )

#print df[roi][other_roi] # this will give u a user warning - becuase the number of rows in roi and other_roi are different. 

# anothe way:

roi = df["attributes"].str.contains( "Sxl" )
df2 = df[roi]
roi2 = df2["type"].str.contains("transcript")
df3 = df2[roi2]
print df3



plt.figure()
plt.title("plotted start positions")
plt.plot(df2[roi2]["start"])
#plt.plot(df[roi][other_roi]["start"])#this is saying plot the starts with the two sets of conditions set out in roi and other roi 
plt.xlabel("gene")
plt.ylabel("sxl start position that are transcripts")
plt.savefig("start_sxl_transcript.png") # in terminal you can open all the files by open *.png
