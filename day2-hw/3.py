#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/rawdata/samples.csv"

df = pd.read_csv(annotation) # reads out csv and spits out an DataFrame File.

roi = df["sample"] #isolate all the sample columns or hte SRR...etc files

for sample in roi:
    ctab_file = "/Users/cmdb/qbb2015-homework/day2/stringtie/" + sample + "/t_data.ctab"
    df2 = pd.read_table(ctab_file)
    roi2 = df2["t_name"].str.contains("FBtr0331261")
    print df2[roi2]