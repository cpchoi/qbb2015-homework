#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015-homework/day2/stringtie/SRR072893/t_data.ctab"

df= pd.read_table(annotation)
order = df.sort(columns="FPKM",ascending=False)
roi = order["FPKM"] > 0

print df[roi]

count = 0
for value in df["FPKM"]:
    if value > 0:
        count += 1
print count

one_third = count/3
two_third = (2*count)/3
three_third = count
 #df [a:b]
 #df [b:c]
 #df [c:d]
 
 

bottom_third= order[roi]["FPKM"][0:one_third]
middle_third= order[roi]["FPKM"][one_third:two_third]
top_third= order[roi]["FPKM"][two_third:count]

plt.figure()
plt.title("boxplot")
plt.boxplot([bottom_third, middle_third, top_third])
plt.xlabel("Bottom, Middle, Top")
plt.ylabel("FPKM")
plt.savefig("box_plots.png")