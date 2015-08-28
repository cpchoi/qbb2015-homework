#!/usr/bin/env python

import sys

for line in open( sys.argv[1] ):
    if ">" in line:
        fields = line.split()
        name = fields[1]
        print name
        
    if "Gaps" in line:
       fields = line.split()
       identity = fields[2]
       gaps = fields[6] # 2 for identities and 7 for gaps
       print "Gaps: " + gaps + " Identity: " + identity
       print "\n"
       
       