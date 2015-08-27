#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

annotation = "~/qbb2015-homework/day2/stringtie/SRR072893/t_data.ctab"

df = pd.read_table(annotation)
roi = df["FPKM"] > 0

log_FPKM = np.log(df[roi]["FPKM"])


just_log = log_FPKM.values

plt.figure()
log_FPKM.plot(kind = 'kde')
plt.savefig("kde.png")

