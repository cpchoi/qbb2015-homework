#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import numpy as np - you can find out hte source code for panda plots by googling gallery

female = pd.read_table("~/qbb2015-homework/day2/stringtie/SRR072905/t_data.ctab")
male = pd.read_table("~/qbb2015-homework/day2/stringtie/SRR072893/t_data.ctab")

fnon_zero_FPKM = female["FPKM"] > 0
mnon_zero_FPKM = male["FPKM"] > 0

#log2 of each of the non zero fpkm values in the male and female data frames
flog_FPKM = np.log2(female[fnon_zero_FPKM]["FPKM"])

mlog_FPKM = np.log2(male[mnon_zero_FPKM]["FPKM"])


# creating a list of M and A values for the M A Plot
M = flog_FPKM - mlog_FPKM

A = (flog_FPKM + mlog_FPKM) / 2

plt.figure()
plt.plot(A, M, 'o')
plt.title("Male vs Female Stage 10")
plt.xlabel("M")
plt.ylabel("A")
plt.savefig("ma_plot.png")

