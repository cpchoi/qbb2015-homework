#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np - you can find out hte source code for panda plots by googling gallery
metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")
metadata2 = pd.read_csv("/Users/cmdb/qbb2015-homework/day3-lunch/replicates.csv")

Sxl_female = []
for sample in metadata[metadata["sex"] == "female"]["sample"]:
    new_table1 = pd.read_table("~/qbb2015-homework/day2/stringtie/" + sample + "/t_data.ctab")
    roi1 = new_table1["t_name"].str.contains("FBtr0331261")
    Sxl_female.append(new_table1[roi1]["FPKM"].values) #figure 3c in the corresponding pubmed paper - get close to this as possible
    
Sxl_male = []
for sample in metadata[metadata["sex"] == "male"]["sample"]:
    new_table2 = pd.read_table("~/qbb2015-homework/day2/stringtie/" + sample + "/t_data.ctab")
    roi2 = new_table2["t_name"].str.contains("FBtr0331261")
    Sxl_male.append(new_table2[roi2]["FPKM"].values) #figure 3c in the corresponding pubmed paper - get close to this as possible

Sxl_R= []
for sample in metadata2["sample"]:
    new_table3 = pd.read_table("~/qbb2015-homework/day2/stringtie/" + sample + "/t_data.ctab")
    roi3 = new_table3["t_name"].str.contains("FBtr0331261")
    Sxl_R.append(new_table3[roi3]["FPKM"].values)

print len(Sxl_R)
plt.figure()
plt.plot(Sxl_female, label = "female", color = "r" )
plt.plot(Sxl_male, label = "male", color = "b" )
plt.plot([4,5,6,7,4,5,6,7], Sxl_R, 'o', label = "replicate", color = "g")
plt.xticks( range(8), ['10', '11', '12', '13', '14A', '14B', '14C', '14D'] )
plt.yticks( range( 0,350,50 ))
plt.legend( bbox_to_anchor = (1.05, 1), loc=5, borderaxespad=0 )
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (FPKM)")

plt.savefig("timecourse.png")



