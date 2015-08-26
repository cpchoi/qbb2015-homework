#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table( annotation, comment = '#', header = None )

df.columns = [ "chromosome", "database", "type", "start", "end", "score", "strand", "frame", "attributes" ]


roi = df["attributes"].str.contains( "Sxl" )
other_roi = df["type"].str.contains( "transcript" )


plt.figure()
plt.title("plotted start positions")
plt.plot(df[roi][other_roi]["start"])#this is saying plot the starts with the two sets of conditions set out in roi and other roi 
plt.xlabel("gene")
plt.ylabel("sxl start position that are transcripts")
plt.savefig("start_sxl_transcript.png") # in terminal you can open all the files by open *.png
