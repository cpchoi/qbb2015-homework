#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys

score = []
e_values =[]
for line in open( sys.argv[1] ):
    if "Score" and "Expect" in line:
       fields = line.split()
       score_f = float( fields[2] )
       expect_f = float( fields[7] )
       print "score: " + fields[2] + " expect: " + fields[7]
       print "\n"
       if expect_f != 0:
           score.append(score_f)
           e_values.append(expect_f)

log_score = np.log(score)

plt.figure()
plt.title("score")
plt.hist(log_score, bins = 500, label='x')
plt.savefig("score_histogram.png")

plt.figure()
plt.title("e_values")
plt.hist(e_values, bins = 500, label='x')
plt.savefig("e_histogram.png")

plt.figure()
plt.plot(log_score, e_values, 'o')
plt.title("log score vs. e values")
plt.xlabel("log score")
plt.ylabel("e values")
plt.savefig("scoreVsE.png")

