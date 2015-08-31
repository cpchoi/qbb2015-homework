#!/usr/bin/env python

"""
Count intersection of two BED files
"""

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

ctcf.set_bits_from_file( sys.argv[2] )
beaf.set_bits_from_file( sys.argv[3] )
beaf.set_bits_from_file( sys.argv[4] )


combination = ctcf.union( beaf.union( suhw ) )
intervals = combination.start_stop()